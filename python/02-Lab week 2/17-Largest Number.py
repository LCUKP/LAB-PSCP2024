"""Largest Number"""
def sauce(num1,num2) :
    """sauce"""
    if num1 < num2:
        return num2
    return num1
def main():
    """main"""
    num1 = input()
    num2 = input()
    num3 = input()
    mak = sauce(num1+num2+num3,num1+num3+num2)
    mak = sauce(mak,num2+num3+num1)
    mak = sauce(mak,num2+num1+num3)
    mak = sauce(mak,num3+num1+num2)
    mak = sauce(mak,num3+num2+num1)
    print(int(mak))
main()
