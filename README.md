# `G-FOLD Python`
An implementation of G-FOLD (**G**uidance algorithm for **F**uel **O**ptimal **L**arge **D**iverts) in `python` with `cvxpy`.

## **WARNING: This project is deprecated due to infeasible result caused by unknown reason and an issue of cvxpygen caused generation of UTF-8 character (which cannot be recognized by GCC) in C header.**
---

![SpaceX FH Landing](doc/fh_demo.jpg)
*Side boosters landing on the pads. Falcon Heavy Demo Mission, 2018. (Credit: SpaceX)*

![Commit](https://img.shields.io/github/last-commit/CuNO3/gfold-py/main)
![Language](https://img.shields.io/github/languages/top/CuNO3/gfold-py)
![License](https://img.shields.io/github/license/CuNO3/gfold-py)

Copyright (C) 2022-present Unili (aka CuNO3). All rights reserved.  
Licensed under the Apache License, Version 2.0.

## Disclaimer
`G-FOLD Python` is designed for **DEMONSTRATION PURPOSES**. The developers **CANNOT GUARANTEE THE ALGORITHM WILL WORK AS EXPECTED**. The developers **SHALL NOT BE RESPONSIBLE FOR ANY LOSSES AND/OR DAMAGES DUE TO THE USAGE OF THE ALGORITHM**.

## TODO
- [ ] Solve the infeasible problem
- [X] Rewritten
- [ ] Cleaning the code
- [ ] Add more comments
- [ ] Add more test cases

The estimated time of completion is February 2024.

## Requirements
- Python 3.9
- cvxpy 1.3.2
- cvxpygen (when generating C code) 0.2.3

**Do not use python > 3.9, or you may meet compatibility problems**  

Personally, I recommend using [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) to manage your python environment.  

About how to install `cvxpy` in `Conda` environment, please refer to [this page](https://www.cvxpy.org/install/index.html#conda).



## Usage
- `solve_ecos.py` Solve the problem using the ecos solver
- `solve_scs.py` Solve the problem using the scs solver
- `solve_osqp.py` Solve the problem using the osqp solver
- `problem3.py` Defined the problem 3.
- `variables.py` Defined the variable of the problem

## References
["Lossless Convexification of Non-Convex Control Bound and Pointing Constraints of the Soft Landing Optimal Control Problem ."](https://doi.org/10.1109/TCST.2012.2237346)  

["G-FOLD: A Real-Time Implementable Fuel Optimal Large Divert Guidance Algorithm for Planetary Pinpoint Landing"](https://www.researchgate.net/publication/258676350_G-FOLD_A_Real-Time_Implementable_Fuel_Optimal_Large_Divert_Guidance_Algorithm_for_Planetary_Pinpoint_Landing)

["Convex Programming Approach to Powered Descent Guidance for Mars Landing"](https://dx.doi.org/10.2514/1.27553)

["Lossless Convexification of Powered-Descent Guidance with Non-Convex Thrust Bound and Pointing Constraints"](https://dx.doi.org/10.1109/ACC.2011.5990959)

["Lossless convexification of control constraints for a class of nonlinear optimal control problems"](http://dx.doi.org/10.1109/ACC.2012.6314722)

["Minimum-Landing-Error Powered-Descent Guidance for Mars Landing Using Convex Optimization"](http://dx.doi.org/10.2514/1.47202)

[thisisneal/G-FOLD](https://github.com/thisisneal/G-FOLD)

[jonnyhyman/G-FOLD-Python](https://github.com/jonnyhyman/G-FOLD-Python)

[xdedss/GFOLD_KSP](https://github.com/xdedss/GFOLD_KSP)

[caojohnny/gfold](https://github.com/caojohnny/gfold)

