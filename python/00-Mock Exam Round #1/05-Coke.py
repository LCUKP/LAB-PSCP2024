"""Coke"""
def main():
    """Coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    price = 0
    for i in range(1,d):
        if b == 0 :
            price = (d*a)-a
            break
        else :
            if not i % b :
                price += c
            else :
                price += a
    if d == 0:
        print(0)
    else :
        print(price+a)
main()
