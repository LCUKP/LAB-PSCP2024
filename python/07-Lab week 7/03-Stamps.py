"""Stamps"""
def main() :
    """Stamps"""
    num = int(input())
    pro = int(input())      #a
    stamp = int(input())    #b
    exch = int(input())     #c
    dis = int(input())      #d
    tmpstamps = 0
    sumprice = 0
    for _ in range(num) :
        price = int(input())
        if tmpstamps > 0 :
            if tmpstamps >= exch :
                while True :
                    if tmpstamps < exch or price <= 0 :
                        break
                    tmpstamps -= exch
                    price -= dis
        if price > 0 :
            sumprice += price
        if price >= pro :
            tmpstamps += stamp*(price//pro)
    print(sumprice)
    print(tmpstamps)
main()
