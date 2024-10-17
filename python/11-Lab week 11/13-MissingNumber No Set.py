"""MissingNumber No Set"""
def main() :
    """MissingNumber No Set"""
    num = int(input())
    numlist = []
    while True :
        tmp = int(input())
        if not tmp :
            break
        numlist.append(tmp)
    for i in range(1,num+1) :
        if i not in numlist :
            print(i)
main()
