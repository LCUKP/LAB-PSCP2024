"""Circular II"""
def main():
    """Circular II"""
    x = float(input())
    y = float(input())
    r1 = float(input())
    xn = float(input())
    yn = float(input())
    r2 = float(input())
    d = ((xn-x)**2+(yn-y)**2)**0.5
    if d < r1+r2:
        print("Yes")
    else :
        print("No")
main()
