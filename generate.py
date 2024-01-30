from cvxpygen import cpg
from problem3 import prob3

cpg.generate_code(problem=prob3,code_dir='./problem3',solver=cpg.cp.CLARABEL)