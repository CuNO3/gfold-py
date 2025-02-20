# Monte Carlo simulation for landing
import numpy as np
import warnings
import sys
import os
import cvxpy as cp
import matplotlib.pyplot as plt
import matplotlib as mpl

warnings.filterwarnings("ignore")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gfold')))

import gfold as gf

# Function to generate random parameters
def generate_random_parameters():
    r0 = np.random.uniform(low=[1000, -1500, -1500], high=[2000, 1500, 1500])
    v0 = np.random.uniform(low=[-15, -15, -15], high=[15, 15, 15])
    m0 = np.random.uniform(low=1800, high=2200)
    mf = np.random.uniform(low=200, high=400)
    rho1 = np.random.uniform(low=0.05, high=0.15) * 24000
    rho2 = np.random.uniform(low=0.9, high=1.2) * 24000
    return r0, v0, m0, mf, rho1, rho2

# Monte Carlo simulation
num_simulations = 42
results = []

for i in range(num_simulations):
    r0, v0, m0, mf, rho1, rho2 = generate_random_parameters()
    alpha = 5 * 10**-4
    g0 = 9.81
    omega = np.array([2.53*10**-5,0,6.62*10**-5])
    gamma_gs = 45

    tf = np.random.uniform(low=81, high=96)

    p = gf.Problem(120, tf, 3)
    p.constraints()
    p.value(
        r0, np.array([0,0,0]), v0, np.array([0,0,0]),
        np.array([-3.71,0,0]),g0,m0,mf,90,rho1,rho2,alpha,
        120,gamma_gs
    )

    (s, x, u, z, s) = p.solve(cp.ECOS)
    results.append(x)

# Plotting the results
plt.rcParams['figure.dpi'] = 300
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=20, azim=45)

for k in results:
    if k is None:
        continue
    else:
        ax.plot(k[2, :], k[1, :], k[0, :], linewidth=2)

max_range = 1800
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(0, 3200)

ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig('test/monte_carlo.png', dpi=300, bbox_inches='tight')
plt.show()
