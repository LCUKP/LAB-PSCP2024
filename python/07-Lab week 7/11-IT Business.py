"""IT Business"""
def main():
    """IT Business"""
    bank = float(input())
    money = float(input())
    error = 0
    want = input()
    while want!="end":
        if want[0] =="D":
            if money >= float(want[1:]):
                money -= float(want[1:])
                bank += float(want[1:])
                error = 0
            else:
                error += 1
        elif want[0] == "W":
            if bank >= float(want[1:]):
                bank -= float(want[1:])
                money += float(want[1:])
                error = 0
            else:
                error += 1
        if error >= 3:
            break
        want = input()
    print(f"{bank:.2f}")
    print(f"{money:.2f}")
main()
