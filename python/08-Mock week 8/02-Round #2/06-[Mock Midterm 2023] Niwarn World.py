"""Niwarn World"""
import math
def x(n):
    """func x"""
    values = 2 + ((math.log2(n**2))/((2*n)*(math.log2(n))))
    return values
def y(n,s) :
    """func y"""
    values = (math.sin(math.radians(30))+math.sqrt(2*s))/(x(n)+3)
    return values
def z(k):
    """func z"""
    values = (y(k,k))**2 + ((8456*((x(k))**4))/(24*k))
    return values
def main():
    """main"""
    n = float(input())
    s = float(input())
    k = float(input())
    print(f"X: {x(n):.1f}, Y: {y(n,s):.1f}, Z: {z(k):.1f}")
main()
