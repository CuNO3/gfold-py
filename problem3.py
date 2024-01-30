import numpy as np
import cvxpy as cp

import variables as var
import parameters as par
import utility as util

# No warmings true
util.no_warnings()

# Length of time step for discretization.
d_t = par.t_f / (par.N - 1)

def cons() -> list:
    cons = [
        # Initial position and velocity
        var.x[0:3, 0] == par.r_0,
        var.x[3:6, 0] == par.v_0,
        # Final position
        var.x[0:3, -1] == par.q,
        # Final velocity equals to 0
        var.x[3:6, -1] == np.array([0, 0, 0]),

        # Final thrust equals to 0
        var.s[-1] == 0,
        # Thrust direction starts straight
        var.u[:, 0] == var.s[0, 0] * np.array([1, 0, 0]),
        # Thrust direction ends straight
        var.u[:, -1] == var.s[0, -1] * np.array([1, 0, 0]),
    ]

    for k in range(par.N - 1):
        cons.append(
            var.x[3:6, k+1] == par.A * var.x[k]
            + d_t * ( par.g + var.u[k] )
        )

        cons.append(
            var.x[0:3, k+1] == var.x[0:3, k]
            + d_t * (var.x[3:6, k] + var.x[3:6, k+1])
        )

        cons.append(
            cp.norm(var.x[1:3, k])
        )