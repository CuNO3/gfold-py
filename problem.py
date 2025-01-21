# Base class
# Data for problems
class Problem:
    def __init__(self, N, ptype):
        self.N = N
        self.ptype = ptype
        self.alpha = cp.Parameter(shape=1, name="alpha")
        self.E = cp.Parameter(shape=(2, 3), name="E")
        self.S = cp.Parameter(shape=(3, 3), name="S")
        self.B = cp.Parameter(shape=(6, 3), name="B")
        self.A = cp.Parameter(shape=(6, 6), name="A")
        self.n_hat = cp.Parameter(shape=3, name="n_hat")
        self.theta_cos = cp.Parameter(shape=1, name="theta_cos")
        self.gamma_gs_tan = cp.Parameter(shape=1, name="gamma_gs_tan", nonneg=True)
        self.rho_1_exp_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0", nonneg=True)
        self.rho_2_exp_z_0 = cp.Parameter(shape=(1, N), name="rho_2_exp_z_0")
        self.rho_1_exp_z_0_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0_z_0")
        self.rho_2_exp_z_0_z_0 = cp.Parameter(shape=(1, N), name="rho_2_exp_z_0_z_0")
        self.rho_1_exp_z_0_sqaure_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0_z_0")
        self.v_max = cp.Parameter(shape=1, name="v_max")
        self.z_0 = cp.Parameter(shape=(1, N), name="z_0")
        self.z_u = cp.Parameter(shape=(1, N), name="z_u")
        self.t_f_A = cp.Parameter(shape=(6,6), name="t_f_A")
        self.t_f_B = cp.Parameter(shape=(6,3), name="t_f_B")
        self.t_f_B_g = cp.Parameter(shape=(6,3), name="t_f_B_g")
        self.var = Variables(N, ptype)

    def variables(self):
        self.x = cp.Variable((6, self.N), name="x")
        self.u = cp.Variable((3, self.N), name="u")
        self.z = cp.Variable((3, self.N), name="z")
        self.s = cp.Variable((1, self.N), name="sigma")

    def constraints(self):
        self.cons = cons = [
            # Initial position and velocity (8)
            self.x[0:3, 0] == self.r_0,
            self.x[3:6, 0] == self.v_0,

            # Initial mass equals
            self.z[0] == self.m_wet,
            # Final mass constraint
            self.z[-1] >= self.m_f,

            # Final attitude and velocity (9)
            self.x[0, -1] == self.q[0],
            self.x[3:6, -1] == np.array([0, 0, 0]),

            # Final thrust equals to 0
            self.s[:, -1] == 0,
            # Thrust direction starts straight
            self.u[:, 0] == self.s[:, 0] * np.array([1, 0, 0]),
            # Thrust direction ends straight
            self.u[:, -1] == self.s[:, -1] * np.array([1, 0, 0]),
        ]