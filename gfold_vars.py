# gf_vars
import cvxpy as cp
import gfold_params as prm

x = cp.Variable((6, prm.N), name='x')  # State vector
u = cp.Variable((3, prm.N), name='u')  # Unified thrust state
z = cp.Variable((1, prm.N), name='z')  # Natural log of mass
s = cp.Variable((1, prm.N), name='sigma')  # Mass-normalized thrust-magnitude slack variable

# The lower bound on natural log of mass
# z_0 = cp.Parameter(shape=1, name="z_0")
