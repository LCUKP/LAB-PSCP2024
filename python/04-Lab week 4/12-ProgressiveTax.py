"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    income = int(input())
    tax = 0
    if income > 4000000:
        income = income - 4000000
        tax += income*0.35
        income = 4000000
    if income > 2000000:
        income = income - 2000000
        tax += income*0.30
        income = 2000000
    if income > 1000000:
        income = income - 1000000
        tax += income*0.25
        income = 1000000
    if income > 750000:
        income = income - 750000
        tax += income*0.20
        income = 750000
    if income > 500000:
        income = income - 500000
        tax += income*0.15
        income = 500000
    if income > 300000:
        income = income - 300000
        tax += income*0.10
        income = 300000
    if income > 150000:
        income = income - 150000
        tax += income*0.05
    if income <= 150000:
        tax += 0
    print(int(tax))
main()
