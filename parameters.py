# params
import cvxpy as cp;

# Discretion timestep
# How many steps are gonna be used in discretion
N = 160

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

# Final time
# G-FOLD is fixed final time algorithm
# It's non-negative
t_f = cp.Parameter(shape=1, name="t_f", nonneg=True)

# Delta T * g
# Equals to t_f / (N - 1) * g
d_t_g = cp.Parameter(shape=3, name="t_f", nonneg=True)

# Initial mass and final mass
# Equals to m_wet
m_0 = cp.Parameter(shape=1, name="m_0")

# Mass depletion / fuel comsumption constant
alpha = cp.Parameter(shape=1, name="alpha", nonneg=True)

# Unit vector
# Includes et1, et2 and et3
# Should be [[ 1, 0, 0 ],
#           [ 0, 1, 0 ],
#           [ 0, 0, 1 ]]
E = cp.Parameter(shape=(3, 3), name="E")

# Planet angular velocity
# Should be [[ 0, -w3, w2 ],
#           [ w3, 0, -w1 ],
#           [ -w2, w1, 0 ]]
S = cp.Parameter(shape=(3, 3), name="S")

# B
# Defined as [[0],[I]]
B = cp.Parameter(shape=(3, 6), name="B")

# A
# Defined as [[0, I], [-S^2, -2*S]]
A = cp.Parameter(shape=(6, 6), name="A")

# Thrust unit vector
n_hat = cp.Parameter(shape=3, name="n_hat")

# Theta maximum tvc angle
theta = cp.Parameter(shape=1, name="theta")

# Glidescope cone constraint
# Where 0 < gamma_gs < pi/2
gamma_gs = cp.Parameter(shape=1, name="gamma_gs", nonneg=True)

# Maximum velocity
v_max = cp.Parameter(shape=1, name="v_max", nonneg=True)
