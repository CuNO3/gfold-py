# variables
import cvxpy as cp
import parameters as prm

# x = (r, \dot{r}) = (r, v)
x = cp.Variable((6, prm.N), name='x')  # State (position and velocity)
u = cp.Variable((3, prm.N), name='u')  # Mass-normalized unified thrust state
z = cp.Variable((1, prm.N), name='z')  # Natural log of mass
s = cp.Variable((1, prm.N), name='sigma')  # Mass-normalized thrust-magnitude slack variable
