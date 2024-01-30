import numpy as np
import cvxpy as cp

import variables as var
import parameters as par
import utility as util

# No warmings true
util.no_warnings()

def cons() -> list:
    cons = [
        # Initial position and velocity (8)
        var.x[0:3, 0] == par.r_0,
        var.x[3:6, 0] == par.v_0,
        # Final attitude and velocity (9)
        var.x[0, -1] == par.q[0],
        var.x[3:6, -1] == 0,

        # Final thrust equals to 0
        var.s[:, -1] == 0,
        # Thrust direction starts straight
        var.u[:, 0] == var.s[:, 0] * np.array([1, 0, 0]),
        # Thrust direction ends straight
        var.u[:, -1] == var.s[:, -1] * np.array([1, 0, 0]),

        # Initial mass equals
        var.z[0] == par.m_0,
        # Final mass constraint
        # var.z[-1] >= par.m_f
    ]

    for k in range(par.N - 1):
        # State (17)
        cons.append(
            var.x[:, k+1][:, None] == var.x[:, k][:, None] + 
            (
                (par.t_f_A * var.x[:, k][:, None])
                + (par.t_f_B * var.u[:, k][:, None])
                + par.t_f_B_g         
            ) / (par.N-1)
        )

        # Mass decrease (17)
        cons.append(
            var.z[:, k+1] == var.z[:, k] - 
            par.alpha * var.s[:, k]
        )

    for k in range(par.N):
        # # Mass limit
        # cons.append(
        #     par.z_0[:, k] <= var.z[:, k]
        # )
        # cons.append(
        #     par.z_u[:, k] >= var.z[:, k]
        # )

        # Thrust limit (34)
        cons.append(
            cp.norm2(var.u[:, k]) <= var.s[:, k]
        )

        # Thrust pointing constraint (34)
        cons.append(
            par.n_hat * var.u[:, k] >= par.theta_cos * var.s[:, k]
        )

        # Maximum velocity (12)
        cons.append(
            cp.norm2(var.x[3:6, k]) <= par.v_max
        )

        # Glidescope constraint (12),(13)
        cons.append(
            cp.norm2(var.x[0:3, k] - par.q) <= par.c.T * var.x[0:3, k] - par.c_q
        )

        # Thrust upper bound (36)
        cons.append(
            var.s[:, k] <= par.rho_2_exp_z_0[:, k] * (
                1 - var.z[:, k]
            ) + par.rho_2_exp_z_0_z_0[:, k]
        )

        # Thrust lower bound (36)
        cons.append(
            var.s[:, k] >= par.rho_1_exp_z_0[:, k] * (
                1 - var.z[:, k] + cp.square(var.z[:, k]) / 2
            ) + par.rho_1_exp_z_0_z_0[:, k]
            - par.rho_1_exp_z_0_z_0[:, k] * var.z[:, k]
            + par.rho_1_exp_z_0_sqaure_z_0[:, k]
        )
    
    return cons

# Make cvxpy happy
obj = cp.Minimize(cp.norm2(var.x[:3, par.N - 1][:, None]- par.q[:, None]))
prob3 = cp.Problem(objective=obj, constraints=cons())

# # Some debug info
# print("Problem 3:")
# print("---------------------")
# print("Minimize:", obj)
# util.print_prob_type(prob3)
# print("---------------------")
# print("Subject to:")
# for c in cons():
#     print(c)
#     print("DCP:", c.is_dcp())
#     print("DPP:", c.is_dpp())
#     print("---------------------")
# print("Variables:")
# print("x:", var.x, " shape:", var.x.shape)
# print("u:", var.u, " shape:", var.u.shape)
# print("z:", var.z, " shape:", var.z.shape)
# print("s:", var.s, " shape:", var.s.shape)
# print("---------------------")