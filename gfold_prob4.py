# gf_prb3
import numpy as np
import cvxpy as cp

import gfold_params as prm
import gfold_vars as var

import gfold_tests as tst

# Just silence it
# Seems that cvxpy is confused by the parameters
tst.no_warnings()

# Delta t. Length of time step for discretization.
d_t = prm.t_f / (prm.N - 1)

def con() -> list:
    cons = [
        # Initial state
        var.x[0:3, 0] == prm.r_0,
        var.x[3:6, 0] == prm.v_0,
        # Final velocity
        var.x[3:6, -1] == prm.v_f,
        # Equals to p3 to get optimal solution
        var.x[0:3, -1] == prm.r_f_p3,

        # Thrust ends at the end of the trajectory
        var.s[-1] == 0,
        # Thrust direction starts straight
        var.u[:, 0] == var.s[0, 0] * np.array([1, 0, 0]),
        # Thrust direction ends straight
        var.u[:, -1] == var.s[0, -1] * np.array([1, 0, 0]),
        # Initial mass equals
        var.z[0] == prm.m_wet
    ]

    for k in range(prm.N - 1):
        # Velocity
        cons.append(
            var.x[3:6, k + 1] == var.x[3:6, k]
            # + d_t * prm.g # This line is not DPP
            + (d_t / 2) * (
                    var.u[:, k]
                    + var.u[:, k + 1]
            )
        )

        # Mass
        cons.append(
            var.x[0:3, k + 1] == var.x[0:3, k]
            + (d_t / 2) * (
                    var.x[3:6, k]
                    + var.x[3:6, k + 1]
            )
        )

        # Glideslope constraint
        cons.append(
            cp.norm(var.x[1:3, k])
            - prm.gamma_gs_cot
            * (var.x[0, k]) <= 0
        )

        # Maximum velocity constraint
        cons.append(
            cp.norm(var.x[3:6, k]) <= prm.v_max
        )

        # Mass decrease
        cons.append(
            var.z[0, k + 1] == var.z[0, k]
            - (
                # Use precalculated alpha * d_t
                # to avoid DPP error
                    prm.alpha_d_t / 2
            ) * (
                    var.s[0, k] + var.s[0, k + 1]
            )
        )

        # Thrust limit
        cons.append(
            cp.norm(var.u[:, k]) <= var.s[0, k]
        )

        # Thrust pointing constraint
        cons.append(
            var.u[:, k] >= prm.theta_cos * var.s[0, k]
        )

    for k in range(0, prm.N):
        cons.append(
            prm.z_0[0, k] <= var.z[0, k]
        )

        cons.append(
            prm.z_u[0, k] >= var.z[0, k]
        )

        # Linear upper bound
        # s(t) <= ρ2 * e ^ −z0 * ( 1 - ( z(t) - z0(t) ) )
        cons.append(
            var.s[0, k] <=
            prm.mu_2[0, k]
            * (
                    1 - var.z[0, k]
            )
            # Here we use rho_2 * exp(-z_0) * z_0
            # for DPP compatibility
            + prm.mu_2_z_0[0, k]
        )

        # SOC lower bound
        # Well...IDK how to trans a taylor expansion to SOC... :(
        # ρ1 * e ^ −z0 * ( 1 - ( z(t) - z0(t) ) + ( z(t) - z0(t) ) ^ 2 / 2 ] <= s(t)
        cons.append(
            prm.mu_1[0, k]
            * (
                    1 - var.z[0, k] +
                    cp.square(var.z[0, k]) / 2
            )
            + prm.mu_1_z_0[0, k]
            + prm.mu_1_z_0[0, k] * var.z[0, k]
            + prm.mu_2_square_z_0[0, k] / 2
            <= var.s[0, k]
        )
    
    return cons

obj = cp.Minimize(cp.norm(var.z[0, prm.N - 1]))
prob4 = cp.Problem(objective=obj, constraints=con())