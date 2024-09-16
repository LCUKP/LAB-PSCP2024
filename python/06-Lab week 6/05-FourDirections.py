"""FourDirections"""
def up(i):
    """up"""
    if not i :
        print("  *  ",end=" ")
    elif i == 1 :
        print(" *** ",end=" ")
    elif i == 2 :
        print("* * *",end=" ")
    elif i == 3 :
        print("  *  ",end=" ")
    elif i == 4 :
        print("  *  ",end=" ")
def down(i):
    """down"""
    if not i :
        print("  *  ",end=" ")
    elif i == 1 :
        print("  *  ",end=" ")
    elif i == 2 :
        print("* * *",end=" ")
    elif i == 3 :
        print(" *** ",end=" ")
    elif i == 4 :
        print("  *  ",end=" ")
def left(i):
    """left"""
    if not i :
        print("  *  ",end=" ")
    elif i == 1 :
        print(" *   ",end=" ")
    elif i == 2 :
        print("*****",end=" ")
    elif i == 3 :
        print(" *   ",end=" ")
    elif i == 4 :
        print("  *  ",end=" ")
def right(i):
    """right"""
    if not i :
        print("  *  ",end=" ")
    elif i == 1 :
        print("   * ",end=" ")
    elif i == 2 :
        print("*****",end=" ")
    elif i == 3 :
        print("   * ",end=" ")
    elif i == 4 :
        print("  *  ",end=" ")
def main() :
    """FourDirections"""
    side = input()
    for i in range(5):
        for j in side:
            if j == "U":
                up(i)
            elif j == "D":
                down(i)
            elif j == "L":
                left(i)
            elif j == "R":
                right(i)
        print()
main()
