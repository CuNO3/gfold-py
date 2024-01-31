# params
import cvxpy as cp;

# Discretion timestep
# How many steps are gonna be used in discretion
N = 120

# Initial position
r_0 = cp.Parameter(shape=3, name="r_0")
# Initial velocity
v_0 = cp.Parameter(shape=3, name="v_0")
# The result of problem 3 solving
# Used in problem 4 to find optimal solution
q_p3 = cp.Parameter(shape=3, name="q_p3")
# q denotes the final position
# equals to t_f
q = cp.Parameter(shape=3, name="q")
# Final velocity
v_f = cp.Parameter(shape=3, name="v_f")

# Feasible cone constraint
# Equals to [1, 0, 0] / tan(gamma_gs)
c = cp.Parameter(shape=3, name="c")
# c * q
c_q = cp.Parameter(shape=3, name="c_q")

# Final time
# G-FOLD is fixed final time algorithm
# It's non-negative
t_f = cp.Parameter(shape=1, name="t_f")

# Delta T * g
# Equals to t_f / (N - 1) * g
# d_t_g = cp.Parameter(shape=3, name="d_t_g")

# Gravity vector
g = cp.Parameter(shape=3, name="g")

# Initial mass and final mass
# Equals to m_wet
m_wet = cp.Parameter(shape=1, name="m_0")
# Final mass
m_0 = cp.Parameter(shape=1, name="m_0")
m_f = cp.Parameter(shape=1, name="m_f")

# Mass depletion / fuel comsumption constant
alpha = cp.Parameter(shape=1, name="alpha")

# Unit vector
# Includes et1, et2 and et3
# Should be [[ 1, 0, 0 ],
#           [ 0, 1, 0 ],
#           [ 0, 0, 1 ]]
# Without the 1st one.
# Means it should be
# [[0, 1, 0], [0, 0, 1]]
E = cp.Parameter(shape=(2, 3), name="E")

# Planet angular velocity
# Should be [[ 0, -w3, w2 ],
#           [ w3, 0, -w1 ],
#           [ -w2, w1, 0 ]]
S = cp.Parameter(shape=(3, 3), name="S")

# B
# Defined as [[0],[I]]
B = cp.Parameter(shape=(6, 3), name="B")

# A
# Defined as [[0, I], [-S^2, -2*S]]
A = cp.Parameter(shape=(6, 6), name="A")

# Thrust unit vector
n_hat = cp.Parameter(shape=3, name="n_hat")

# Theta maximum tvc angle
# theta = cp.Parameter(shape=1, name="theta")
theta_cos = cp.Parameter(shape=1, name="theta_cos")

# Glidescope cone constraint
# Where 0 < gamma_gs < pi/2
# gamma_gs = cp.Parameter(shape=1, name="gamma_gs", nonneg=True)
gamma_gs_tan = cp.Parameter(shape=1, name="gamma_gs_tan", nonneg=True)

# Rho_1 * exp(-z_0)
rho_1_exp_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0", nonneg=True)
# Rho_2 * exp(-z_0)
rho_2_exp_z_0 = cp.Parameter(shape=(1, N), name="rho_2_exp_z_0")
# Rho_1 * exp(-z_0) * z_0
rho_1_exp_z_0_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0_z_0")
# Rho_2 * exp(-z_0) * z_0
rho_2_exp_z_0_z_0 = cp.Parameter(shape=(1, N), name="rho_2_exp_z_0_z_0")
# Rho_1 * exp(-z_0) * z_0^2 / 2
rho_1_exp_z_0_sqaure_z_0 = cp.Parameter(shape=(1, N), name="rho_1_exp_z_0_z_0")

# Maximum velocity
v_max = cp.Parameter(shape=1, name="v_max")

# The lower bound on natural log of mass
z_0 = cp.Parameter(shape=(1, N), name="z_0")
# The upper bound on natural log of mass
z_u = cp.Parameter(shape=(1, N), name="z_u")

t_f_A = cp.Parameter(shape=(6,6), name="t_f_A")
t_f_B = cp.Parameter(shape=(6,3), name="t_f_B")
t_f_B_g = cp.Parameter(shape=(6,3), name="t_f_B_g")
E_q = cp.Parameter(shape=(2,3), name="E_q")