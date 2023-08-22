# `G-FOLD Python`
An implementation of G-FOLD (**G**uidance algorithm for **F**uel **O**ptimal **L**arge **D**iverts) in `python` with `cvxpy`.

![Photo: SpaceX](doc/fh_demo.jpg)
*Side boosters landing on the pads. Falcon Heavy Demo Mission, 2018. (Photo: SpaceX)*

![License](https://img.shields.io/github/license/CuNO3/gfold-py)

Copyright (C) 2022-present Unili (aka CuNO3). All rights reserved.  
Licensed under the Apache License, Version 2.0.

## Requirements
- Python 3.9
- cvxpy 1.3.2
- cvxpygen (when generating C code) 0.2.3

**Do not use python > 3.9 or you may met compatiblility problems**  

Personally, I recommend using [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html) to manage your python environment.  

**Warning**: `Conda` environment **may not work well with `cvxpy`**, especially the solver part. Sometimes you may receive a `SolverError` even if you have correctly installed the solver.  

About how to install `cvxpy` in `Conda` environment, please refer to [this page](https://www.cvxpy.org/install/index.html#conda).



## Usage
- `gfold_exec.py` Directly execute the cvxpy ECOS solver
- `gfold_exec_scs.py` Directly execute the cvxpy SCS solver
- `gfold_cgen.py` Generate C code of two problems with `cvxpygen`
- `gfold_plot.py` Used for testing the generated trajectories
- `gfold_params.py` Non executable, the g-fold parameters
- `gfold_vars.py` Non executable, the g-fold variables
- `gfold_prob3.py` Non executable, definition of problem 3
- `gfold_prob4.py` Non executable, definition of problem 4
- `gfold_tests.py` Non executable, test cases and auxiliary debug functions

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

