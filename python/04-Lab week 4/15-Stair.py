"""Stair"""
def main():
    """Stair"""
    y = int(input())
    n = int(input())
    count, tmp = 0,0
    code = 0
    for _ in range(n):
        x = int(input())
        tmp = tmp+x
        if x > y :
            code = 1
        elif tmp == y:
            count += 1
            tmp = 0
        elif tmp > y :
            count += 1
            tmp = x
    if tmp > 0 :
        count += 1
    if code :
        print("NO")
    else :
        print(count)
main()
