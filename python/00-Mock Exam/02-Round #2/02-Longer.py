"""Longer"""
import math
def main():
    """Longer"""
    r = float(input())
    a = float(input())
    b = float(input())
    rd = 2*math.pi*r
    rtg = 2*(a+b)
    if rd == rtg:
        print("Equal")
    elif rd > rtg:
        print("Circle is longer")
    else :
        print("Rectangle is longer")
    print(f"{abs(rd-rtg):.5f}")
main()
