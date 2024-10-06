"""[Midterm 2024] 100 meters"""
import math
def main():
    """[Midterm 2024] 100 meters"""
    gold = math.inf
    silver = math.inf
    copper = math.inf
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(1,9) :
        time = float(input())
        if time < gold :
            copper = silver
            silver = gold
            gold = time
            num3 = num2
            num2 = num1
            num1 = i
        if gold < time < silver :
            copper = silver
            silver = time
            num3 = num2
            num2 = i
        if silver < time < copper :
            copper = time
            num3 = i
    print(num1,num2,num3)
main()
