"""[Recommend] ISBN"""
def main() :
    """[Recommend] ISBN"""
    num = input().replace("-","")[::-1]
    isbn = 0
    for i,v in enumerate(num) :
        if i != 0 :
            isbn += int(v)*(i+1)
    if (-isbn % 11) == int(num[0]) :
        print("Yes")
    else :
        if (-isbn % 11) == 10 :
            print("No X")
        else :
            print(f"No {-isbn % 11}")
main()
