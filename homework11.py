# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0


from cmath import cos, sin
from math import cos, sin
from symtable import Symbol
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = Symbol('x')
y = -12*x **4 *sin (cos(x)) - 18*x**3+5*x**2 + 10*x - 30
plot (y,(x,-1,1))

