"""mod doc"""
def main():
    """doc"""
    k = int(input())
    n = int(input())
    num = 0
    for i in range(0,n):
        print(" "*num + "*" * k)
        if i < n // 2 and num >=0:
            num += 1
        else:num -=1
main()
