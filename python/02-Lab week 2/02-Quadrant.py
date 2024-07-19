"""Quadrant"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    if not x and not y:
        print("O")
    elif (x > 0 and not y) or (x < 0 and not y):
        print("X")
    elif (y > 0 and not x) or (y < 0 and not x):
        print("Y")
    elif x > 0 and y > 0 :
        print("Q1")
    elif y > 0 :
        print("Q2")
    elif x < 0 and y < 0 :
        print("Q3")
    elif y < 0 :
        print("Q4")
main()
