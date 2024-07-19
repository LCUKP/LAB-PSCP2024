"""foodgrade"""
def main(i=24,count = 0) :
    """input"""
    if i  > 0:
        kai = int(input())
        if 50 <= kai <= 70:
            count += 1
        main(i-1,count)
    else :
        print(count)
main()
