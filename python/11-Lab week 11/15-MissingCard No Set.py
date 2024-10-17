"""MissingCard No Set"""
def main() :
    """MissingCard No Set"""
    listt = ["A", "K", "Q", "J", "10", "9", "8", "7","6", "5", "4", "3", "2"]
    phai = [j+i for i in "SHDC" for j in listt]
    tmp = []
    for _ in range(51) :
        tmp.append(input())
    for i in phai :
        if i not in tmp :
            print(i)
            break
main()
