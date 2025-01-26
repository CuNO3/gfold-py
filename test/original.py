import numpy as np

# Make python happy by adding the path to the gfold module
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gfold')))

import gfold as gf

r0 = np.array([2400, 960, -450])
v0 = np.array([-10,-40,10])
m0 = 2000
mf = 300
rho1 = 0.1 * 24000
rho2 = 1.0 * 24000
alpha = 5 * 10**-4
g0 = 9.81
omega = np.array([2.53*10**-5,0,6.62*10**-5])
gamma_gs = 45

p = gf.Problem(90, 39, 3)
p.constraints()
p.value(
    r0, np.array([0,0,0]), v0, np.array([0,0,0]),
    np.array([-3.71,0,0]),g0,m0,mf,90,rho1,rho2,360,
    120,gamma_gs
)
# We force the value of alpha to be the same as the one in the original code
p.alpha.value = np.array([alpha])

# Disable warnings
import warnings
warnings.filterwarnings("ignore")

#p.info()

import cvxpy as cp
(s, x, u, z, s) = p.solve(cp.SCS)
# print(s)
print("Optimal value:")
for k in range(p.N):
    print("x:", x[0:3, k])
    print("v:", x[3:6, k])
    print("u:", u[0:3, k])
    print("z:", z[0, k])
    print("s:", s[0, k])

# Call matplotlib to plot the results
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set DPI for high resolution
plt.rcParams['figure.dpi'] = 300

# In 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
# Set the view angle (elevation, azimuth)
ax.view_init(elev=20, azim=45)
ax.plot(x[2, :], x[1, :], x[0, :], linewidth=2)

max_range = 4200  # Use maximum of data or 50
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(0, 3200)

# Add grid and labels
ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y') 
ax.set_zlabel('Z')

# Export the plot in high resolution
plt.savefig('test/original.png', dpi=300, bbox_inches='tight')
plt.show()