# gf_test

# Turn it to False when production
test = [
    False,  # Test the problem
    False,  # Test the constraints
    False,  # Test the parameters
    False,  # Test the variables
    False,  # Print constraints to file
    False,  # Print constraint is_dcp() and is_dpp()
    False  # Print constraint is_dcp() and is_dpp() to file
]


def no_warnings():
    import warnings
    warnings.filterwarnings("ignore")


def expr_info(expr):
    print("Curvature: ", expr.curvature)
    print("Is DCP: ", expr.is_dcp())
    print("Is DPP: ", expr.is_dpp())


def expr_curvature(expr):
    print("Curvature: ", expr.curvature)


def expr_dcp(expr):
    print("Is DCP: ", expr.is_dcp())


def expr_dpp(expr):
    print("Is DPP: ", expr.is_dpp())


def con_info(con):
    print(con)
    print("Is DCP: ", con.is_dcp())
    print("Is DPP: ", con.is_dpp())


def con_dcp(con):
    print("DCP:", con.is_dcp())


def con_dpp(con):
    print("DPP:", con.is_dpp())
