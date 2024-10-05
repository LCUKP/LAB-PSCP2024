"""[Mock Midterm 2023] Ticket Fare"""
def main() :
    """[Mock Midterm 2023] Ticket Fare"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    price = 0
    if n >= f and n >= g :
        s = abs(f-g)
        if s <= a :
            price += b
        elif s <= a+c :
            s -= a
            price += b+((s*d))
        elif s > a+c :
            s -= a+c
            price += b + (c*d) + (s*e)
        print(price)
    else :
        print("Error")
main()
