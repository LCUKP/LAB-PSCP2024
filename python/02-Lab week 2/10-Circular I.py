"""Circular I"""
def main():
    """main"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    d = ((xn-x)**2+(yn-y)**2)**0.5
    if d > r:
        print("No")
    else :
        print("Yes")
main()
