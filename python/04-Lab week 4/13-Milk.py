"""Milk"""
def main():
    """Milk"""
    price = int(input())
    pro = int(input())
    add = int(input())
    money = int(input())
    count = 0
    milk = 0
    if pro > 0 :
        while money >= price or count >= pro:
            if count >= pro > 0:
                milk += add
                count = add
            else :
                money-=price
                milk += 1
                count += 1
    else :
        while money >= price:
            money-=price
            milk += 1
            count += 1
    print(milk)
main()
