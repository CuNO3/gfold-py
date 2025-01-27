# `gfold-py` ***`neo`***
A fresh ***neo*** implementation of G-FOLD (**G**uidance algorithm for **F**uel **O**ptimal **L**arge **D**iverts) algorithm in `python` with `cvxpy`.

It is a new start and a complete rewrite of the original project `gfold-py`(2022-2024), the goal is to make it *harder, better, faster and stronger* than ever before.

![SpaceX Booster Landing](asset/starship_demo.jpg)
*Booster caught by "Mechazilla" (aka "Chopsticks"). Starship IFT-7, 2025. (Credit: SpaceX)*

![Commit](https://img.shields.io/github/last-commit/CuNO3/gfold-py/neo)
![Language](https://img.shields.io/github/languages/top/CuNO3/gfold-py)
![License](https://img.shields.io/github/license/CuNO3/gfold-py)
[![Build](https://github.com/CuNO3/gfold-py/actions/workflows/build.yml/badge.svg)](https://github.com/CuNO3/gfold-py/actions/workflows/build.yml)

Copyright (C) 2022-present CuNO3.  
Licensed under the BSD 3-Clause License.

## Goals

- [x] Implement the basic G-FOLD algorithm
- [ ] Code generation for C with `cvxpygen`
- [ ] Documentation and examples
- [ ] Line search to determine $t_f$ as described in the original paper

## Requirements
- Python 3.10
- cvxpy 1.3.2
- ~~cvxpygen (when generating C code) 0.2.3~~
*\*Will be back sometime in the future*

## References
["Lossless Convexification of Non-Convex Control Bound and Pointing Constraints of the Soft Landing Optimal Control Problem ."](https://doi.org/10.1109/TCST.2012.2237346)  

["Convex Programming Approach to Powered Descent Guidance for Mars Landing"](https://doi.org/10.2514/1.27553)

["Lossless Convexification of Powered-Descent Guidance with Non-Convex Thrust Bound and Pointing Constraints"](https://doi.org/10.1109/ACC.2011.5990959)

["Lossless convexification of control constraints for a class of nonlinear optimal control problems"](http://doi.org/10.1109/ACC.2012.6314722)

["Minimum-Landing-Error Powered-Descent Guidance for Mars Landing Using Convex Optimization"](http://doi.org/10.2514/1.47202)

## Thanks

As of January 2025, the project has been fully tested and validated; the remaining work consists of minor improvements and documentation.

My field of study is *completely* irrelevant to control theory or convex optimization, so I have learned everything from scratch and made many mistakes along the way.

I could not have finished this project without the support and encouragement from *my family and friends*. It's been a long journey since I first started this project in 2022. I still remember the first version of the project in July 2023 (during the summer break after an important exam) (of course, it was a disaster `:(`). I never thought I could finish it someday.

The first time I saw SpaceX landing a Falcon 9 booster was in 2019, and it really amazed me. Five years later, they landed a Starship booster on "Mechazilla". All these achievements are truly inspiring.

Started in 2022 and finished in 2025, it's been a long journey, but it's worth it for someone who loves the stars.

I would also like to thank the authors of the original papers and the authors of `cvxpy` and `cvxpygen`.