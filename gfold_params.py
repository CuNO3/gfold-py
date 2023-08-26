# gf_prms
import cvxpy as cp

# Parameters for G-FOLD
# ---------------------
# Described in https://dx.doi.org/10.2514/1.47202 and
#              https://doi.org/10.1109/TCST.2012.2237346

# Discrete steps
N = 160

# The time of vehicle to land
t_f = cp.Parameter(shape=1, name="t_f", nonneg=True)

# Gravity constant
g_0 = cp.Parameter(shape=1, name="g_0", nonneg=True)

# Wet mass of the vehicle
m_wet = cp.Parameter(shape=1, name="m_wet", nonneg=True)

# Minimum and maximum throttle
rho_1 = cp.Parameter(shape=1, name="rho_1", nonneg=True)
rho_2 = cp.Parameter(shape=1, name="rho_2", nonneg=True)

# Mass depletion / Fuel consumption constant
# alpha = 1 / isp * g_0
# alpha = cp.Parameter(shape=1, name="alpha")
# isp = cp.Parameter(shape=1, name="isp")
# alpha = 1 / (isp * g_0)

# Use precalculated alpha-d_t
# because isp, N, t_f and g_0 are constants
# alpha_d_t = 1 / (isp * g_0) * t_f / N
alpha_d_t = cp.Parameter(shape=1, name="alpha_d_t", nonneg=True)
# Use precalculated alpha-rho_1 and alpha-rho_2
# because isp, g_0, rho_1 and rho_2 are constants
# alpha_rho_1 = 1 / (isp * g_0) * rho_1
alpha_rho_1 = cp.Parameter(shape=1, name="alpha_rho_1", nonneg=True)
# alpha_rho_2 = 1 / (isp * g_0) * rho_2
alpha_rho_2 = cp.Parameter(shape=1, name="alpha_rho_2", nonneg=True)

# The lower bound on natural log of mass
z_0 = cp.Parameter(shape=(1, N), name="z_0")
# The upper bound on natural log of mass
z_u = cp.Parameter(shape=(1, N), name="z_u")
# The exp of -z0
# exp_z0 = cp.Parameter(shape=(1, N), name="exp_z0")

# rho_1 * exp(-z0)
# Always non-negative because rho_1 >= 0, and 1/mass >= 0
mu_1 = cp.Parameter(shape=(1, N), name="mu_1", nonneg=True)
# rho_2 * exp(-z0)
mu_2 = cp.Parameter(shape=(1, N), name="mu_2", nonneg=True)
# rho_1 * exp(-z0) * z0
mu_1_z_0 = cp.Parameter(shape=(1, N), name="mu_1_z_0")
# rho_2 * exp(-z0) * z0
mu_2_z_0 = cp.Parameter(shape=(1, N), name="mu_2_z_0")
# rho_1 * exp(-z0) * z0 ^ 2
mu_1_square_z_0 = cp.Parameter(shape=(1, N), name="mu_2_square_z_0")

# Glideslope cone angle
# gamma_gs = cp.Parameter(shape=1, name="gamma_gs")
# Use precalculated cot
gamma_gs_cot = cp.Parameter(shape=1, name="gamma_gs_cot")

# Maximum thrust pointing angle
# from the thrust unit vector
# theta = cp.Parameter(shape=1, name="theta")
# Use the precalculated cosine
theta_cos = cp.Parameter(shape=1, name="theta_cos")

# Maximum allowable velocity
v_max = cp.Parameter(shape=1, name="v_max", nonneg=True)

# The gravitational acc of the planet
g = cp.Parameter(shape=3, name="g")

# Unit vector of thrust
# n_hat = cp.Parameter(shape=3, name="n_hat")

# Initial position
r_0 = cp.Parameter(shape=3, name="r_0")
# Initial velocity
v_0 = cp.Parameter(shape=3, name="v_0")

# Final position calc by prob3
# Used in p4 to find optimal solution
r_f_p3 = cp.Parameter(shape=3, name="r_f_p3")
# Final position
r_f = cp.Parameter(shape=3, name="r_f")
# Final velocity
v_f = cp.Parameter(shape=3, name="v_f")
