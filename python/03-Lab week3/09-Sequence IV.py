"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    numn = num**2
    for i in range(1,numn+1):
        if not i % num:
            print(f"{i}")
        else:
            print(i,end=" ")
main()
