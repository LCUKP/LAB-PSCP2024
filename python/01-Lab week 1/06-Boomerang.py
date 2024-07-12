"""Boomerang"""
import math
numx = int(input())
numy = int(input())
numz = int(input())
def f1(x):
    """f1"""
    print(x + 1)
def f2(y):
    """f2"""
    print((7*(y**3)) + (2*(y**2)) - (31*y) + 1)
def f3(z):
    """f3"""
    print(-z)
def f4(x, y):
    """f4"""
    print((x + y) * (x - y))
def f5(x, y , z):
    """f5"""
    print((y - math.sqrt(y**2 - 4*x*z)) / (2*x))
f1(numx)
f2(numy)
f3(numz)
f4(numx, numy)
f5(numx, numy , numz)
