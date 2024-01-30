# variables
import cvxpy as cp
import parameters as par

# x = (r, \dot{r}) = (r, v)
x = cp.Variable((6, par.N), name='x')  # State (position and velocity)
u = cp.Variable((3, par.N), name='u')  # Mass-normalized unified thrust state
z = cp.Variable((1, par.N), name='z')  # Natural log of mass
s = cp.Variable((1, par.N), name='sigma')  # Mass-normalized thrust-magnitude slack variable
