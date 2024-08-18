"""Sequence IX"""
def main():
    """Sequence IX"""
    num = int(input())
    blankspace = num - 1 #Taylor Version
    tmp = 0
    for i in range(1,num+1) :
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
        print()
        tmp = 0
        blankspace -= 1
main()
