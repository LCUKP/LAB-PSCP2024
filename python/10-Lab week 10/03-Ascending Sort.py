"""Ascending Sort"""
def main() :
    """Ascending Sort"""
    num = int(input())
    numlist = []
    for _ in range(num):
        numlist.append(int(input()))
    for i in sorted(numlist):
        print(i)
main()
