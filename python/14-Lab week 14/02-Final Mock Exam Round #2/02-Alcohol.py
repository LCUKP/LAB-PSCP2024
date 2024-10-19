"""Alcohol ผิดสองเคส"""
def main() :
    """Alcohol"""
    sex = 0.68 if input() == "Male" else 0.55
    weight = float(input())
    diver = input()
    drink = float(input())
    al = float(input())
    can = int(input())
    rest = int(input())
    all_al = (al * (drink * can))/100
    al_per = all_al / (weight * sex * 10)
    al_per = al_per - ((al_per*0.015) * rest)
    if al_per >= 0.05 or diver == "No" :
        print("Not Safe")
    else :
        print("Safe")
main()
