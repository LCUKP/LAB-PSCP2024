"""Sequence VI"""
def main():
    """Sequence VI"""
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,i+1):
            if j == i:
                print(j)
            else :
                print(j,end=" ")
main()
