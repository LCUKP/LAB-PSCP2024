"""Restaurant"""
def main():
    """Restaurant"""
    price = float(input())
    pro = float(input())
    dis = float(input())/100
    adv = float(input())
    pricepro = price + adv
    if price >= pro :
        price = price - (price * dis)
    if pricepro >= pro :
        pricepro = pricepro - (pricepro*dis)
    if price > pricepro :
        print(f"Yes {(price-pricepro):.3f}")
    elif pricepro > price :
        print(f"No {(pricepro-price):.3f}")
    else :
        print("Yes")
main()
