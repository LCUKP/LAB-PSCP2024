"""Duplicate I"""
def main() :
    """Duplicate I"""
    num1 = int(input())
    num2 = int(input())
    list1 = []
    list2 = []
    dup = []
    for _ in range(num1) :
        list1.append(input())
    for _ in range(num2) :
        list2.append(input())
    for i in list1 :
        if i in list2 :
            dup.append(i)
    dup = sorted(dup,reverse=True)
    if dup != [] :
        for x in dup :
            print(x)
    else :
        print("Nope")
main()
