"""Sequence XI"""
def main():
    """Sequence XI"""
    num = int(input())
    for i in range(-num+1,num):
        for j in range(-num+1,num):
            if abs(i) > abs(j):
                print(f"{num-abs(i):>02}",end=" ")
            else :
                print(f"{num-abs(j):>02}",end=" ")
        print()
main()
