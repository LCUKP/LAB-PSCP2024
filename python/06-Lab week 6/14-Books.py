"""Books"""
import math
def main() :
    """Books"""
    books = int(input())
    pages = int(input())
    x = int(input())
    y = int(input())
    d,cbooks,cpages = 0,0,0
    while True :
        j = math.ceil(((x+d)/(y+d))*pages)
        if j >= pages :
            break
        if cbooks == books :
            break
        cpages += j
        if cpages >= pages :
            cbooks += 1
            cpages = 0
        d += 1
    d += books-cbooks
    print(d)
main()
