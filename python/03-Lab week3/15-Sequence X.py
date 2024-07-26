"""Sequence X"""
def main():
    """Sequence X"""
    num = int(input())
    blankspace = num - 1 #Taylor Version
    tmp = 0
    num2 = num
    for i in range(1,(num*2)+1) :
        if i > num :
            blankspace += 1
            for _ in range(0,blankspace+1) :
                print("  ",end=" ")
            for m in range(1,num2):
                print(f"{m:>02}",end=" ")
                tmp += 1
            for n in range(tmp-1,0,-1) :
                if n == 1:
                    print(f"{n:>02}")
                else :
                    print(f"{n:>02}",end=" ")
            num2 -= 1
        else :
            for _ in range(0,blankspace) :
                print("  ",end=" ")
            for j in range(1,i+1):
                print(f"{j:>02}",end=" ")
                tmp += 1
            for x in range(tmp-1,0,-1) :
                if x == tmp:
                    print(f"{x:>02}")
                else :
                    print(f"{x:>02}",end=" ")
            blankspace -= 1
            print()
        tmp = 0
main()
#PEP-8
