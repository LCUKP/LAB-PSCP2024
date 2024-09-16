"""Lotto"""
def main():
    """Lotto"""
    win = input()
    num2 = input()
    num3_1 = input()
    num3_2 = input()
    butt3_1 = input()
    butt3_2 = input()
    lotto = input()
    money = 0
    if win in ("000000","999999") :
        if lotto in ("000001","999999","999998","000000") :
            money += 100000
    else :
        win1 = str("%06d"%(int(win)+1))
        win2 = str("%06d"%(int(win)-1))
        if lotto == win1 or lotto == win2 :
            money += 100000
    if lotto == win :
        money += 6000000
    if lotto[4:] == num2 :
        money += 2000
    if lotto[:3] == num3_1 :
        money += 4000
    if lotto[:3] == num3_2 :
        money += 4000
    if lotto[3:] == butt3_1 :
        money += 4000
    if lotto[3:] == butt3_2 :
        money += 4000
    print(money)
main()
