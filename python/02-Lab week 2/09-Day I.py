"""day1"""
def main():
    """main"""
    year = int(input())
    if not year%4 :
        if year%100:
            print("Yes")
        elif not year % 400:
            print("Yes")
        else :
            print("No")
    else :
        print("No")
main()
