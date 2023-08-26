# gf_data.py

# This script includes the test data for the G-FOLD algorithm.

import numpy as np

g_0 = 9.80665
# Preconfigured data
# gamma = 30
gamma_gs_cot = 1.732
g = np.array([-3.711, 0, 0])

# Paper landing data
N = 160
t_f = 80
m_wet = 2300
rho_1 = 24000 * 0.1
rho_2 = 24000 * 1.2
theta_cos = -0.5
alpha = 5 * 0.0001
alpha_d_t = 5 * 0.0001 * t_f / N
V_max = 250
r_f = np.array([0, 0, 0])
r_0 = np.array([900, 900, 0])
v_0 = np.array([-45, 0, 0])
v_f = np.array([0, 0, 0])
z_0 = np.zeros((1, N))
z_u = np.zeros((1, N))
mu_1 = np.zeros((1, N))
mu_2 = np.zeros((1, N))
mu_1_z_0 = np.zeros((1, N))
mu_2_z_0 = np.zeros((1, N))
mu_1_square_z_0 = np.zeros((1, N))
for k in range(N):
    print("--------------")
    z_0[0, k] = np.log(m_wet - alpha * rho_2 * k)
    z_u[0, k] = np.log(m_wet - alpha * rho_1 * k)
    mu_1[0, k] = rho_1 * np.exp(-z_0[0,k])
    mu_2[0, k] = rho_2 * np.exp(-z_0[0,k])
    mu_1_z_0[0, k] = rho_1 * np.exp(-z_0[0,k]) * z_0[0,k]
    mu_2_z_0[0, k] = rho_2 * np.exp(-z_0[0,k]) * z_0[0,k]
    mu_1_square_z_0[0, k] = rho_1 * np.exp(-z_0[0,k]) * z_0[0,k] ** 2
    # print("k: ", k)
    # print("alpha: ", alpha)
    # print("rho1: ", rho_1)
    # print("rho2: ", rho_2)
    # print("z_0 at ",k,": ",np.log(m_wet - alpha * rho_2 * k))
    # print("z_u at ",k,": ",np.log(m_wet - alpha * rho_1 * k))
    # print("mu_1: ", mu_1[0, k])
    # print("mu_2: ", mu_2[0, k])
    # print("mu_1_z_0: ", mu_1_z_0[0, k])
    # print("mu_2_z_0: ", mu_2_z_0[0, k])
    # print("mu_2_square_z_0: ", mu_1_square_z_0[0, k])

# Print all the parameters
# For debug
# print("N: ", N)
# print("t_f: ", t_f)
# print("m_wet: ", m_wet)
# print("rho_1: ", rho_1)
# print("rho_2: ", rho_2)
# print("theta_cos: ", theta_cos)
# print("alpha: ", alpha)
# print("alpha_d_t: ", alpha_d_t)
# print("V_max: ", V_max)
# print("r_f: ", r_f)
# print("r_0: ", r_0)
# print("v_0: ", v_0)
# print("v_f: ", v_f)
# print("z_0: ", z_0)
# print("z_u: ", z_u)
# print("mu_1: ", mu_1)
# print("mu_2: ", mu_2)
# print("mu_1_z_0: ", mu_1_z_0)
# print("mu_2_z_0: ", mu_2_z_0)
# print("mu_1_square_z_0: ", mu_1_square_z_0)

# Falcon 9 landing data
# t_f = 36 * 60
# T_max = 854000
# m_wet = 
# Isp = 282
# V_max = 100
# G_max = 3
# theta = 15
# theta_cos = 0.259


# New Shepard landing data

# Xombie landing data
'''
T_max = 4000
'''

# Grasshopper landing data

# MOD landing data
