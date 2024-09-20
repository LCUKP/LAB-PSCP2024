"""diamond"""
def main() :
    """diamond"""
    num = int(input())
    x = num//2
    for i in range(num):
        if i < (num//2) :
            if i :
                print(" "*(x-i)+"*"+" "*((2*i-1))+"*")
            else :
                print(" "*(x-i)+"*")
        elif i == (num//2) :
            print("*"*num)
        elif i > (num//2) :
            print(" "*((i-(num//2)))+"*",end="")
            if i != num-1 :
                print(" "*(((num-i)*2)-3)+"*")
main()
