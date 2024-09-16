"""One For All"""
def main() :
    """One For All"""
    num = int(input())
    alumni = ""
    for i in range(1,num+1) :
        name = input()
        if i == num :
            alumni += name+"_"+str(i)
            break
        if not i % 2 :
            alumni += name+"-"*i
        else :
            alumni += name+"*"*i
    print(alumni)
main()
