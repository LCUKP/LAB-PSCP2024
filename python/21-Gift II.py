"""Gift II"""
def main():
    """main"""
    num = []
    i = 8
    while i > 0:
        num.append(int(input()))
        i -= 1
    for x in num :
        if not x % 2:
            print(x)
main()
