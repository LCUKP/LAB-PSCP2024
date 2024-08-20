"""Heron of Alexandria"""
def main():
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a+b+c)/2
    print("%.3f"%(s*(s-a)*(s-b)*(s-c))**0.5)
main()
