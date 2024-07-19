"""Triangle I"""
def main():
    """main"""
    numA = float(input())
    numB = float(input())
    numC = float(input())
    if round(numA)+0.01 == numA:
        numA = round(numA)
    if round(numB)+0.01 == numB:
        numB = round(numB)
    if round(numC)+0.01 == numC:
        numC = round(numC)
    num = (numA**2)+(numB**2)
    if num == numC **2:
        print("Yes")
    else :
        print("No")
main()
# False
