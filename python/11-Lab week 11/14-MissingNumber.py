"""MissingNumber"""
def main(num) :
    """MissingNumber"""
    set1 = set(range(1, num + 1))
    set2 = set()
    while True :
        tmp = int(input())
        if not tmp :
            break
        set2.add(tmp)
    for i in sorted(list(set1-set2)) :
        print(i)
main(int(input()))
