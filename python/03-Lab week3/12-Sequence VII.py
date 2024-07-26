"""Sequence VII"""
import math
def main():
    """Sequence VII"""
    num = int(input())
    row = (num*2)-1
    col = math.floor(row/2)
    n = col
    for i in range(1,row+1):
        if i <= col+1 :
            for j in range(1,i+1):
                if j == i:
                    print(j)
                else :
                    print(j,end=" ")
        elif i > col :
            #เงื่อนไขนี้กลับมาอ่านแล้วน่าจะงง
            j = 1
            while j <= n:
                if j == n:
                    print(j)
                else :
                    print(j,end=" ")
                j += 1
            n -= 1
main()
