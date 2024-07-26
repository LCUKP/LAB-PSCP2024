"""Triangle I"""
def triangle(a,b,c) :
    """find triangle"""
    if (a**2+b**2)**0.5 == c :
        return True
    return False
def main():
    """main"""
    numA = float(input())
    numB = float(input())
    numC = float(input())
    if triangle(numA,numB,numC) or triangle(numB,numC,numA) or triangle(numC,numA,numB) :
        print("Yes")
    else :
        print("No")
main()
