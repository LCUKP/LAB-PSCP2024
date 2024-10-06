"""Digital"""
def main():
    """Digital"""
    name = input()
    thai = input()
    home = input()
    age = float(input())
    income = float(input())
    deposit = float(input())
    con1 = thai in ("Yes", "True")
    con2 = age >= 16
    con3 = income <= 840000
    con4 = deposit <= 500000
    con5 = home in ("Yes", "True")
    if con1 and con2 and con3 and con4 and con5 :
        print(f"Congratulations! {name} is qualified to receive a digital wallet" \
              " amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else :
        print(f"Unfortunately, {name} is not qualified.")
main()
