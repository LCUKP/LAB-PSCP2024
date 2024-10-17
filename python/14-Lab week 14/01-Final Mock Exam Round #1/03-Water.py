"""Water"""
def main() :
    """Water"""
    n = int(input())
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    price = 0
    for _ in range(n) :
        tmp = 0
        water = float(input())
        k = water - b
        if water <= b :
            tmp += a*water
        if water > b :
            tmp += a*b
        if k > 0 :
            tmp += c*k
        if tmp <= d :
            tmp = 0
        price += tmp
    print(f"{price:.2f}")
main()
