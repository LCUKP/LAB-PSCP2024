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
    for i in passwort :
        if i.isnumeric :
            digit = 1
        if i.islower :
            lower = 1
        if i.isupper :
            upper = 1
        if i.isprintable :
            printable = 1
    if digit :
        r += 10
    if lower :
        r += 26
    if upper :
        r += 26
    if printable :
        r += 32
    e = math.log2(r**2)
    print(r,e)
main()