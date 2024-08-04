"""mod doc"""
def main():
    """doc"""
    n = int(input())
    k = int(input())
    num = n-1
    num2 = 1
    for _ in range(0,n):
        print(" " * num +"*" * num2)
        num -= 1
        num2 += 2
    num2 = int((num2-3) / 2)-1
    for _ in range(0,k):
        print(" "*num2 + "---")
main()
