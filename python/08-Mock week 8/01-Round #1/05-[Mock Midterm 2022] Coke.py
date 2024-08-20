"""Coke"""
def main():
    """Coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    price = 0
    for i in range(1,d):
        if not b :
            price = (d*a)-a
            break
        if not i % b :
            price += c
        else :
            price += a
    if not d:
        print(0)
    else :
        print(price+a)
main()
