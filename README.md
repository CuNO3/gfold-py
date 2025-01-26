# `gfold-py` ***`neo`***
A fresh ***neo*** implementation of G-FOLD (**G**uidance algorithm for **F**uel **O**ptimal **L**arge **D**iverts) algorithm in `python` with `cvxpy`.

It is a new start and a complete rewrite of the original project `gfold-py`(2022-2024), the goal is to make it *harder, better, faster and stronger* than ever before.

![SpaceX Booster Landing](asset/starship_demo.jpg)
*Booster caught by "Mechazilla" (aka "Chopsticks"). Starship IFT-7, 2025. (Credit: SpaceX)*

![Commit](https://img.shields.io/github/last-commit/CuNO3/gfold-py/main)
![Language](https://img.shields.io/github/languages/top/CuNO3/gfold-py)
![License](https://img.shields.io/github/license/CuNO3/gfold-py)

Copyright (C) 2022-present CuNO3.  
Licensed under the BSD 3-Clause License.

<!-- Also see `gfold-py`'s sister project [`lcgfd-rs`]-->

## Goals

- [x] Implement the basic G-FOLD algorithm
- [ ] Code generation for C with `cvxpygen`
- [ ] Documentation and examples
- [ ] Line search to determine $t_f$ as described in the original paper

## Requirements
- Python 3.9
- cvxpy 1.3.2
- ~~cvxpygen (when generating C code) 0.2.3~~
*\*Will be back sometime in the future*

## Problem

We solves the following optimal control problem:
$$\begin{gather}
\min \, \| E \, r(t_f) - q \| \\
\dot{x}(t) = A(\omega)x(t) + B\left(g + u(t)\right) \quad \forall t \in [0, t_f] \\
\dot{z}(t) = -\alpha\sigma(t) \quad \forall t \in [0,t_f] \\
z(0) = m_0 \\
z(t_f) \ge m_0 - m_f \gt 0 \\
e^T_1r(t_f) = 0\\
\dot{r}(t_f) = 0 \\
\rho_1e^{-z_0}\left[1 - (z(t)-z_0(t)) + \frac{(z(t)-z_0(t))^2}{2}\right] \le \sigma(t) \\
\sigma(t) \le \rho_2e^{-z_0}\left[1 - (z(t)-z_0(t))\right] \\
\|u(t)\|\le\sigma(t) \\ 
\hat{n}^Tu(t) \ge \cos\theta\sigma(t) \\
\|\dot{r}\|\le V_{max} \\
\| E(r-r(t_f))\| \le c^T(r-r(t_f))
\end{gather}$$


## References
["Lossless Convexification of Non-Convex Control Bound and Pointing Constraints of the Soft Landing Optimal Control Problem ."](https://doi.org/10.1109/TCST.2012.2237346)  

["Convex Programming Approach to Powered Descent Guidance for Mars Landing"](https://doi.org/10.2514/1.27553)

["Lossless Convexification of Powered-Descent Guidance with Non-Convex Thrust Bound and Pointing Constraints"](https://doi.org/10.1109/ACC.2011.5990959)

["Lossless convexification of control constraints for a class of nonlinear optimal control problems"](http://doi.org/10.1109/ACC.2012.6314722)

["Minimum-Landing-Error Powered-Descent Guidance for Mars Landing Using Convex Optimization"](http://doi.org/10.2514/1.47202)
