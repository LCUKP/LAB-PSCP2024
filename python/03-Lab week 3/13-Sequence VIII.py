"""Sequence VIII"""
def main():
    """Sequence VIII"""
    num = int(input())
    blankspace = num - 1 #Taylor Version
    for i in range(1,num+1) :
        for _ in range(0,blankspace) :
            print("  ",end=" ")
        for j in range(1,i+1):
            print(f"{j:>02}",end=" ")
        print()
        blankspace -= 1
main()
