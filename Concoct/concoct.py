import scipy
import numpy


def calculate_Cost(specifications):
    #TODO
    multiplier = specifications["base_price"]
    (lambda: multiplier, lambda: multiplier *= calculate_basics(specifications["basics"], multiplier))[specifications["basics"]]();

    return multiplier

