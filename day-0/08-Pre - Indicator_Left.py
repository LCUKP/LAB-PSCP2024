"""Pre - Indicator_Left"""
import math
def main():
    """main"""
    width = int(input())
    height = int(input())
    num = math.floor(height/2)
    for i in range(1,height+1):
        print(" "*num+"*"*width)
        if i < math.ceil(height/2) and num >= 0:
            num -= 1
        else :
            num += 1
main()
