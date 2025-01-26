import cvxpy as cp
import numpy as np

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

        self.vmax = cp.Parameter(1, name='v_max', nonneg=True)

        self.rho1 = cp.Parameter(1, name='rho_1', nonneg=True)
        self.rho2 = cp.Parameter(1, name='rho_2', nonneg=True)

        self.alpha = cp.Parameter(1, name='alpha', nonneg=True)
        self.n_hat = cp.Parameter(3, name='n_hat')
        self.theta_cos = cp.Parameter(1, name='theta_cos', nonneg=True)
        self.E = cp.Parameter((2, 3), name='E')
        self.c = cp.Parameter(3, name='c')
        self.z0 = cp.Parameter((1, N), name='z_0', nonneg=True)
        self.zc = cp.Parameter((1, N), name='z_c', nonneg=True)
        self.zl = cp.Parameter((1, N), name='z_l', nonneg=True)
        self.zq = cp.Parameter((1, N), name='z_q', nonneg=True)
        self.zul = cp.Parameter((1, N), name='z_ul', nonneg=True)
        self.zuc = cp.Parameter((1, N), name='z_uc', nonneg=True)

        self.cons = []

    def constraints(self):
        self.cons += [
            self.x[0:3, 0] == self.r0,
            self.x[3:6, 0] == self.v0,

            self.z[:, 0] == self.m0,
            self.z[:, -1] >= self.m0 - self.mf,

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

                # Relaxation of control vector (34)
                cp.norm2(self.u[:, k]) <= self.s[:, k],

                # Maximum velocity constraint (12)
                cp.norm2(self.x[3:6, k]) <= self.vmax,

                # Thrust pointing constraint (34)
                self.n_hat @ self.u[:, k] >= self.theta_cos * self.s[:, k],
                # self.u[:, k] >= self.theta_cos * self.s[:, k],
                
                # Cone constraint
                #cp.norm2(self.E @ (self.x[0:3, k] - self.q)) <= self.c @ (self.x[0:3, k] - self.q)
                cp.norm2(self.E @ (self.x[0:3, k] - self.x[0:3,-1])) - self.c @ (self.x[0:3, k] - self.x[0:3,-1]) <= 0
                #cp.norm2((self.x[0:3, k] - self.x[0:3,-1])[1:3]) <= self.c @ (self.x[0:3, k] - self.x[0:3,-1])
            ]

            # if k > 0:
            #     self.cons += [
            #         self.zc[:, k] - self.zl[:, k] * self.z[:, k] + self.zq[:, k] * self.z[:, k]**2 <= self.s[:, k] ,
            #         self.s[:, k] <= self.zuc[:, k] - self.zul[:, k] *self.z[:, k],
            #     ]
 
    
    def value(self, r0, q, v0, vf, g, g0, m0, mf, vmax, rho1, rho2, isp, theta, gamma_gs):
        self.r0.value = r0
        self.q.value = q
        self.v0.value = v0
        self.vf.value = vf
        self.g0 = g0
        self.g.value = g
        assert m0 - mf > 0, 'm0 must be greater than mf'
        self.m0.value = np.array([m0])
        self.mf.value = np.array([mf])
        self.vmax.value = np.array([vmax])
        self.rho1.value = np.array([rho1])
        self.rho2.value = np.array([rho2])
        alpha =  1 / (isp * self.g0)
        self.alpha.value = np.array([alpha])
        self.n_hat.value = np.array([1, 0, 0])
        #assert (np.angle() > 0 and gamma_gs < np.pi/2), 'gamma_gs must be in (0, pi/2)'
        self.theta_cos.value = np.array([np.cos(theta)])
        self.E.value = np.array([[0, 1, 0], [0, 0, 1]])
        self.c.value = np.array([1, 0, 0]) / np.tan(gamma_gs)
        # Prepare z0
        z0 = np.zeros((1, self.N))
        zc = np.zeros((1, self.N))
        zl = np.zeros((1, self.N))
        zq = np.zeros((1, self.N))
        zul = np.zeros((1, self.N))
        zuc = np.zeros((1, self.N))
        for k in range(self.N):
            tmp_z0 = np.log(m0 - alpha * rho2 * k * self.dt)
            z0[0, k] = tmp_z0
            tmp_z02 = tmp_z0 ** 2 / 2
            zc[0, k] = (tmp_z0 + tmp_z02 + 1) * rho1 * np.exp(-tmp_z0)
            zl[0, k] = (tmp_z0 + 1) * rho1 * np.exp(-tmp_z0)
            zq[0, k] = rho1 * np.exp(-tmp_z0) / 2
            zul[0, k] = rho2 * np.exp(-tmp_z0)
            zuc[0, k] = rho2 * np.exp(-tmp_z0) * (1+tmp_z0)
        self.z0.value = z0
        self.zc.value = zc
        self.zl.value = zl
        self.zq.value = zq
        self.zul.value = zul
        self.zuc.value = zuc
        

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
        prob.solve(solver, verbose = True)
        return prob.status, self.x.value, self.u.value, self.z.value, self.s.value
        #return prob.status
