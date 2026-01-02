import cvxpy as cp
import numpy as np

def _ensure_cvxpygen_compat():
    """Compatibility shim for cvxpygen with cvxpy>=1.6 where upper_tri_to_full moved."""
    try:
        import cvxpy.expressions.variable as _cvx_var
        if not hasattr(_cvx_var, "upper_tri_to_full"):
            from cvxpy.atoms.affine.upper_tri import upper_tri_to_full as _upper_tri_to_full
            _cvx_var.upper_tri_to_full = _upper_tri_to_full
    except (ImportError, AttributeError):
        pass

class Problem:
    def __init__(self, N, tf, mode):
        # Assertions
        assert mode == 3 or mode == 4, 'mode must be 3 or 4'
        assert N > 0, 'N must be a positive integer'
        assert tf > 0, 'tf must be a positive number'

        # N: number of time steps
        # tf: final time
        # dt: time step length
        self.N = N
        self.tf = tf   

        self.dt = tf / N
        self.mode = mode

        self.x = cp.Variable(shape=(6, N), name='x')
        self.u = cp.Variable(shape=(3, N), name='u')
        self.z = cp.Variable(shape=(1, N), name='z', nonneg=True)
        self.s = cp.Variable(shape=(1, N), name='sigma', nonneg=True)

        self.r0 = cp.Parameter(3, name='r_0')
        self.q = cp.Parameter(3, name='q')

        self.v0 = cp.Parameter(3, name='v_0')
        self.vf = cp.Parameter(3, name='v_f')

        # Vectorized gravity
        self.g = cp.Parameter(3, name='g')
        self.g0 = 9.81

        # Initial mass
        self.m0 = cp.Parameter(1, name='m_0', nonneg=True)
        # Fuel mass
        self.mf = cp.Parameter(1, name='m_f', nonneg=True)
        self.log_m0 = cp.Parameter(1, name='log_m_0')
        self.log_m0_mf = cp.Parameter(1, name='log_m_0_minus_m_f')

        self.vmax = cp.Parameter(1, name='v_max', nonneg=True)

        self.rho1 = cp.Parameter(1, name='rho_1', nonneg=True)
        self.rho2 = cp.Parameter(1, name='rho_2', nonneg=True)

        self.alpha = cp.Parameter(1, name='alpha', nonneg=True)
        self.n_hat = cp.Parameter(3, name='n_hat')
        self.theta_cos = cp.Parameter(1, name='theta_cos', nonneg=True)
        self.E = cp.Parameter((2, 3), name='E')
        self.c = cp.Parameter(3, name='c')
        
        self.z0 = cp.Parameter((1, N), name='z_0', nonneg=True)
        self.mass_quad = cp.Parameter((1, N), name='mass_quad', nonneg=True)
        self.mass_lin = cp.Parameter((1, N), name='mass_lin')
        self.mass_const_lower = cp.Parameter((1, N), name='mass_const_lower')
        self.mass_upper_lin = cp.Parameter((1, N), name='mass_upper_lin')
        self.mass_upper_const = cp.Parameter((1, N), name='mass_upper_const')

        self.cons = []

    def constraints(self):
        self.cons += [
            self.x[0:3, 0] == self.r0,
            self.x[3:6, 0] == self.v0,

            self.z[:, 0] == self.log_m0,
            self.z[:, -1] >= self.log_m0_mf,

            self.x[0, -1] == self.q[0],
            self.x[3:6, -1] == self.vf,

            # Initial thrust equals to 0
            self.s[:, 0] == 0,
            self.u[:, 0] == np.array([0, 0, 0]),

            self.u[:, -1] == self.s[:, -1] * np.array([1, 0, 0]),
        ]

        for k in range(0, self.N - 1):
            # constraint on state variable x (position and velocity)
            # With leapfrog integration method
            self.cons += [
                # Position and velocity dynamics
                self.x[3:6, k+1] == self.x[3:6, k] + (self.dt * 0.5) * ((self.u[:, k] + self.g) + (self.u[:, k+1] + self.g)),
                self.x[0:3, k+1] == self.x[0:3, k] + (self.dt * 0.5) * (self.x[3:6, k] + self.x[3:6, k+1]),

                # Mass dynamics
                self.z[:, k+1] == self.z[:, k] - (self.alpha * self.dt * 0.5) * (self.s[:, k] + self.s[:, k+1]),
                #self.z[:, k+1] == self.z[:, k] - (self.alpha * self.dt) * (self.s[:, k]),

                # Relaxation of control vector (34)
                cp.norm2(self.u[:, k]) <= self.s[:, k],

                # Maximum velocity constraint (12)
                cp.norm2(self.x[3:6, k]) <= self.vmax,

                # Thrust pointing constraint (34)
                self.n_hat @ self.u[:, k] >= self.theta_cos * self.s[:, k],
                
                # Cone constraint
                cp.norm2(self.E @ (self.x[0:3, k] - self.x[0:3,-1])) - self.c @ (self.x[0:3, k] - self.x[0:3,-1]) <= 0
            ]

            # Mass-Thrust constraints
            if k > 0:
                # Precomputed coefficients replace rho*exp(-z0)*(1 - z + z0 + 0.5*(z - z0)^2) so the constraint remains DPP-compatible for cvxpygen.
                lower_bound = self.mass_quad[:, k] * cp.square(self.z[:, k]) + self.mass_lin[:, k] * self.z[:, k] + self.mass_const_lower[:, k]
                upper_bound = self.mass_upper_lin[:, k] * self.z[:, k] + self.mass_upper_const[:, k]
                self.cons += [
                    lower_bound <= self.s[:, k],
                    self.s[:, k] <= upper_bound,
                ]

    def _clear_parameter_sparsity(self, prob):
        """Reset parameter sparsity hints to avoid cvxpygen incompatibilities."""
        _ensure_cvxpygen_compat()
        for param in prob.parameters():
            attrs = getattr(param, 'attributes', None)
            if isinstance(attrs, dict) and 'sparsity' in attrs:
                attrs['sparsity'] = None

    def value(self, r0, q, v0, vf, g, g0, m0, mf, vmax, rho1, rho2, alpha, theta, gamma_gs):
        self.r0.value = r0
        self.q.value = q
        self.v0.value = v0
        self.vf.value = vf
        self.g0 = g0
        self.g.value = g
        assert m0 - mf > 0, 'm0 must be greater than mf'
        self.m0.value = np.array([m0])
        self.mf.value = np.array([mf])
        self.log_m0.value = np.array([np.log(m0)])
        self.log_m0_mf.value = np.array([np.log(m0 - mf)])
        self.vmax.value = np.array([vmax])
        assert rho1 < rho2, 'rho1 must be less than rho2'
        self.rho1.value = np.array([rho1])
        self.rho2.value = np.array([rho2])
        # alpha = 1 / (isp * self.g0)
        self.alpha.value = np.array([alpha])
        self.n_hat.value = np.array([1, 0, 0])
        self.theta_cos.value = np.array([np.cos(theta)])
        self.E.value = np.array([[0, 1, 0], [0, 0, 1]])
        self.c.value = np.array([1, 0, 0]) / np.tan(gamma_gs)

        z0 = np.zeros((1, self.N))
        for k in range(self.N):
            #z0[0, k] = np.log(m0 - alpha * (rho1 + rho2) * 0.5 * k * self.dt)
            z0[0, k] = np.log(m0 - alpha * rho2 * k * self.dt)
        self.z0.value = z0
        exp_neg_z0 = np.exp(-z0)
        rho1_exp = self.rho1.value * exp_neg_z0
        rho2_exp = self.rho2.value * exp_neg_z0
        # Expanding rho*exp(-z0)*(1 - z + z0 + 0.5*(z - z0)^2) (and its upper bound) moves parameter dependence into coefficients so the problem stays DPP-valid.
        self.mass_quad.value = 0.5 * rho1_exp
        self.mass_lin.value = -rho1_exp * (1 + z0)
        self.mass_const_lower.value = rho1_exp * (1 + z0 + 0.5 * np.square(z0))
        self.mass_upper_lin.value = -rho2_exp
        self.mass_upper_const.value = rho2_exp * (1 + z0)
        
    def info(self):
        p = cp.Problem(cp.Minimize(cp.norm(self.x[0:3,-1] - self.q)), self.cons)
        print('Problem information:')
        print('N: {}, delta t: {}'.format(self.N, self.dt))
        print('Is DCP:', p.is_dcp())
        print('Is DPP:', p.is_dcp(dpp=True))
        print('--------------------')
        for c in self.cons:
            print(c)
            print(c.is_dcp())
            print(c.is_dcp(dpp = True))

    def solve(self, solver = cp.SCS):
        self.constraints()
        prob = cp.Problem(cp.Minimize(cp.norm(self.x[0:3,-1] - self.q)), self.cons)
        self._clear_parameter_sparsity(prob)
        prob.solve(solver, verbose = True)
        return prob.status, self.x.value, self.u.value, self.z.value, self.s.value

    def problem(self):
        self.constraints()
        prob = cp.Problem(cp.Minimize(cp.norm(self.x[0:3,-1] - self.q)), self.cons)
        self._clear_parameter_sparsity(prob)
        return prob

    def data(self, solver = cp.ECOS):
        p = self.problem()
        return p.get_problem_data(solver)
