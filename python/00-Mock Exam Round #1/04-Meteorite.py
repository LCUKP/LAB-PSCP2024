"""Meteorite"""
def main():
    """Meteorite"""
    a = float(input())
    b = int(input())
    c = float(input())
    cout = 1
    ukauka = 1
    if a == 0 or a < c:
        print(0)
    else :
        while a >= c:
            a = a / (ukauka * b)
            if a < c:
                break
            cout +=  ukauka
            ukauka += b * ukauka
        print(cout)
main()
# Not Passed
