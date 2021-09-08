import sympy as sp


def calculateDerivative(function, variable):
    derivative = sp.diff(function, variable)
    print(derivative)
