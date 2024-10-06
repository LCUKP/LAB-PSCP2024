"""Coffee Shop"""
def main():
    """Coffee Shop"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    price1 = 0
    price2 = 0
    for i in range(e) :
        if not i :
            price1 += a
        else :
            price1 += a - ((a*b/100))
    if (e*a) >= d :
        price2 += (e*a) - (((e*a)*c)/100)
    else :
        price2 = e*a
    if not price1 and not price2 :
        print("2")
        print(f"{price2:.2f}")
    elif price1 >= price2 :
        print("2")
        print(f"{price2:.2f}")
    elif price2 > price1 :
        print("1")
        print(f"{price1:.2f}")
main()
