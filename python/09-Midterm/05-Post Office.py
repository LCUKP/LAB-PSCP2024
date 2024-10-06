"""Post Office"""
def main():
    """Post Office"""
    n = int(input())
    m = int(input())
    price = 0
    for _ in range(n) :
        env = float(input())
        if env <= 10 :
            price += 16
        elif env <= 20 :
            price += 18
        elif env <= 100 :
            price += 23
        elif env <= 250 :
            price += 28
        elif env <= 500 :
            price += 33
        elif env <= 1000 :
            price += 48
        elif env > 1000 :
            price += 68
        price += 13
    for _ in range(m) :
        env = float(input())
        if env <= 500 :
            price += 45
        elif env <= 1000 :
            price += 55
        elif env > 1000 :
            price += 70
        price += 15
    print(price)
main()
