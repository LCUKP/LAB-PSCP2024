"""Diginity"""
def main():
    """Diginity"""
    num = int(input())
    digi = 0
    while num :
        while len(str(num)) > 1:
            for i in str(num) :
                digi += int(i)
            num, digi = digi, 0
        print(num)
        num = int(input())
main()
