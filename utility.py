def no_warnings():
    import warnings
    warnings.filterwarnings("ignore")

def print_prob_type(prob):
    print("----Problem type----")
    print("DCP:", prob.is_dcp())
    print("DPP:", prob.is_dpp())
    print("--------------------")