"""Circular I"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    r = int(input())
    xn = int(input())
    yn = int(input())
    d = ((xn-x)**2+(yn-y)**2)**0.5
    if d > r:
        print("No")
    else :
        print("Yes")
main()
