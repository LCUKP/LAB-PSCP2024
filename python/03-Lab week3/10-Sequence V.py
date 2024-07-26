"""Sequence V"""
def main():
    """main"""
    num = int(input())
    count = 1
    for i in range(num,0,-1):
        if count < 7 :
            print(i,end=" ")
            count += 1
        elif count == 7:
            print(i)
            count = 1
main()
