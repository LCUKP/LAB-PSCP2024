"""Tuple's Sad life """
def main() :
    """Tuple's Sad life """
    tup = tuple(input().split())
    num = input()
    count = tup.count(num)
    index = tup.index(num)
    for _ in range(count):
        for _ in range(count):
            print(index, end=" ")
        print()
main()
