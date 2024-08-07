"""mod doc"""
def main():
    """doc"""
    num = int(input())
    tmp = 0
    x = 0
    price2, weight2 = 0,0
    for _ in range(num):
        price = float(input())
        weight = float(input())
        x = weight/price
        if x > tmp :
            price2 = price
            weight2 = weight
            tmp = x
        elif x == tmp :
            if price < price2:
                price2 = price
                weight2 = weight
                tmp = x
    print(f"{price2:.2f} {weight2:.2f}")
main()
