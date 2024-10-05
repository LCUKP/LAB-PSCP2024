"""Password"""
import math
def main() :
    """main"""
    passwort = input()
    digit = 0
    lower = 0
    upper = 0
    printable = 0
    r = 0
    l = len(passwort)
    for i in passwort :
        if i.isnumeric() :
            digit = 1
        elif i.islower() :
            lower = 1
        elif i.isupper() :
            upper = 1
        elif i in "~`!@#$%&^*()-_+={ }[\\]|/:;’”<>,.?" :
            printable = 1
    if digit :
        r += 10
    if lower :
        r += 26
    if upper :
        r += 26
    if printable :
        r += 32
    e = math.floor(math.log2(r**l))
    print(e)
    check(e)
def check(e) :
    """check"""
    if e < 28 :
        print("Very Weak")
    elif 28 <= e <= 35 :
        print("Weak")
    elif 36 <= e <= 59 :
        print("Reasonable")
    elif 60 <= e <= 127 :
        print("Strong")
    else :
        print("Very Strong")
main()
