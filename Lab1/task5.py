from scipy import integrate
import sympy as sp
from scipy.integrate import quad


def calculateIntegralBySym(function, variable):
    integral = sp.integrate(function, variable)
    print(integral)


def calculateDefiniteIntegralBySci(function, startPoint, finishPoint):
    integral, _ = quad(function, startPoint, finishPoint)
    print(integral)
