"""[Recommend] Blackjack"""
def main(num = int(input())):
    """[Recommend] Blackjack"""
    bsckjack = 0
    tmp = ""
    for _ in range(num):
        pai = input()
        if pai == "A":
            tmp += pai
            continue
        if pai.isnumeric():
            bsckjack += int(pai)
        else :
            bsckjack += 10
    if len(tmp) > 1 :
        bsckjack += 1
        tmp = tmp[:-1]
    for i in tmp :
        if i == "A" and 11 + bsckjack <= 21 :
            bsckjack += 11
        elif i == "A" and 11 + bsckjack > 21 :
            bsckjack += 1
    print(bsckjack)
main()
