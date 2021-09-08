import sympy as sp
import numpy as np

import task1
import task2
import task3
import task4
import task5
import task6
import task7


task1.findRoots([1, 3 - 10, 5])

task2.readFileAndDuplicate('Files/test.txt')

task3.sort([3, 4, 1, 4, 5])

x = sp.symbols('x')
y = sp.symbols('y')
function = sp.sin(x) * sp.cos(x**2) * sp.tan(y) + sp.ln(x)
task4.calculateDerivative(function, x)


# 1st integral
x = sp.symbols('x')
function1 = x * sp.ln(x)
task5.calculateIntegralBySym(function1, x)

# 2nd integral


def function2(x): return sp.sin(x) / (x + 1)


task5.calculateDefiniteIntegralBySci(function2, 0, 1)

x = np.arange(0, 50, 0.1)
y = np.sin(x)**2 / (x + 1)
task6.drawGraph(x, y)

task7.drawHistogram([5, 4, 2, 7, 0, 3, 3, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8])
