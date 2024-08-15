"""BTSMRT"""
def main():
    """BTSMRT"""
    day = input()
    years = float(input())
    h = float(input())
    if years < 14 and h < 90 :
        print("FREE")
    elif years < 14 and h <= 140 and day == "Children Day":
        print("FREE")
    elif years >= 60 and day == "Senior Day":
        print("FREE")
    else :
        print("PAY")
main()
