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
        # Final altitude because position may not feasible
        var.x[2, -1] == prm.r_f[2],

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

obj = cp.Minimize(cp.norm(var.x[0:3, prm.N - 1] - prm.r_f))
prob3 = cp.Problem(objective=obj, constraints=con())

# Some debug info
# Turn off the debug info 
# with test[0] = False
# at the beginning of the script.
if tst.test[0]:
    print("Problem 3:")
    print("---------------------")
    print("Minimize:", obj)
    print("---------------------")
    if tst.test[1]:
        print("Subject to:")
        for c in con():
            print(c)
            if tst.test[5]:
                print("DCP:", c.is_dcp())
                print("DPP:", c.is_dpp(dpp=True))
                print("---------------------")
        print("---------------------")
    if tst.test[2]:
        print("Parameters:")
        print("d_t:", d_t, " shape:", d_t.shape)
        print("r_0:", prm.r_0, " shape:", prm.r_0.shape)
        print("v_0:", prm.v_0, " shape:", prm.v_0.shape)
        print("v_f:", prm.v_f, " shape:", prm.v_f.shape)
        print("r_f:", prm.r_f, " shape:", prm.r_f.shape)
        print("rho_1:", prm.rho_1, " shape:", prm.rho_1.shape)
        print("rho_2:", prm.rho_2, " shape:", prm.rho_2.shape)
        print("gamma_gs_cot:", prm.gamma_gs_cot, " shape:", prm.gamma_gs_cot.shape)
        print("theta_cos:", prm.theta_cos, " shape:", prm.theta_cos.shape)
        print("v_max:", prm.v_max, " shape:", prm.v_max.shape)
        print("g:", prm.g, " shape:", prm.g.shape)
        print("---------------------")
    if tst.test[3]:
        print("Variables:")
        print("x:", var.x, " shape:", var.x.shape)
        print("u:", var.u, " shape:", var.u.shape)
        print("z:", var.z, " shape:", var.z.shape)
        print("s:", var.s, " shape:", var.s.shape)
        print("z_0:", prm.z_0, " shape:", prm.z_0.shape)
        print("---------------------")
    print("Problem type:")
    print("DCP:", prob3.is_dcp())
    print("DPP:", prob3.is_dpp())
    print("QP:", prob3.is_qp())
    print("---------------------")
    if tst.test[4]:
        with open("prob3_test.txt", "w") as f:
            for c in con():
                f.write(str(c) + "\n")
                if tst.test[6]:
                    f.write("DCP: " + str(c.is_dcp()) + "\n")
                    f.write("DPP: " + str(c.is_dpp()) + "\n")
                    f.write("\n")
            f.write(str(obj) + "\n")
