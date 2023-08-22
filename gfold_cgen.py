# gf_cgen
from cvxpygen import cpg
import gfold_prob3 as prb3
import gfold_prob4 as prb4

cpg.generate_code(prb3.prob3, code_dir="prob3", solver="ECOS")
cpg.generate_code(prb4.prob4, code_dir="prob4", solver="ECOS")
