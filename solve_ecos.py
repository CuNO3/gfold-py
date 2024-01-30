# ecos
import cvxpy as cp
import numpy as np

from problem3 import prob3
import parameters as par

# Paper landing data
N = 160
t_f = 60
g = np.array([-3.711, 0, 0])
# unit vectors
e1 = np.array([1,0,0]).T
e2 = np.array([0,1,0]).T
e3 = np.array([0,0,1]).T
n_hat = e1
# E matrix 
E = np.array([e2.T, e3.T])
ω = np.array([2.53e-5, 0, 6.62e-5]).T 
# S matrix
S = np.array([ [0, -ω[2], ω[1]],  [ω[2], 0, -ω[0]], [ω[1], ω[0], 0]  ])
# A matrix
A = np.block([ [np.zeros((3, 3)), np.eye(3)],  [-S**2, -2*S] ])
# B matrix
B = np.block([ [np.zeros((3, 3))], [np.eye(3)] ])
m_wet = 2300
m_f = 2000
rho_1 = 24000 * 0.1
rho_2 = 24000 * 1.2
theta_cos = np.cos(np.radians(15))
gamma_gs_tan = np.tan(np.radians(45))
alpha = 5 * 0.0001
v_max = 120
r_0 = np.array([2400, 450, -330])
v_0 = np.array([-10, -40, 10])
v_f = np.array([0, 0, 0])
z_0 = np.zeros((1, N))
q = np.array([0, 0, 0])
c = e1 / gamma_gs_tan
c_q = e1 / gamma_gs_tan * q
z_u = np.zeros((1, N))
rho_1_exp_z_0 = np.zeros((1, N))
rho_2_exp_z_0 = np.zeros((1, N))
rho_1_exp_z_0_z_0 = np.zeros((1, N))
rho_2_exp_z_0_z_0 = np.zeros((1, N))
rho_1_exp_z_0_square_z_0 = np.zeros((1, N))
for k in range(N):
    z_0[:, k] = np.log(m_wet - alpha * rho_2 * k)
    z_u[:, k] = np.log(m_wet - alpha * rho_1 * k)
    rho_1_exp_z_0[:, k] = rho_1 * np.exp(-z_0[:,k])
    rho_2_exp_z_0[:, k] = rho_2 * np.exp(-z_0[:,k])
    rho_1_exp_z_0_z_0[:, k] = rho_1 * np.exp(-z_0[:,k]) * z_0[:,k]
    rho_2_exp_z_0_z_0[0, k] = rho_2 * np.exp(-z_0[:,k]) * z_0[:,k]
    rho_1_exp_z_0_square_z_0[0, k] = rho_1 * np.exp(-z_0[:,k]) * z_0[:,k] ** 2 / 2

par.c.value = c
par.c_q.value = c_q
par.q.value = q
par.r_0.value = r_0
par.v_0.value = v_0
par.m_f.value=np.array([m_f])
par.v_f.value = v_f
par.v_max.value=np.array([v_max])
par.t_f.value = np.array([t_f])
par.g.value = g
par.m_0.value = np.array([m_wet])
par.alpha.value = np.array([alpha])
par.E.value = E
par.S.value = S
par.B.value = B
par.A.value = A
par.n_hat.value = n_hat
par.z_0.value = z_0
par.z_u.value = z_u
par.theta_cos.value = np.array([theta_cos])
par.gamma_gs_tan.value = np.array([gamma_gs_tan])
par.rho_1_exp_z_0.value = rho_1_exp_z_0
par.rho_2_exp_z_0.value = rho_2_exp_z_0
par.rho_1_exp_z_0_sqaure_z_0.value = rho_1_exp_z_0_square_z_0
par.rho_1_exp_z_0_z_0.value = rho_1_exp_z_0_z_0
par.rho_2_exp_z_0_z_0.value = rho_2_exp_z_0_z_0

prob3.solve(verbose=True, solver=cp.ECOS)