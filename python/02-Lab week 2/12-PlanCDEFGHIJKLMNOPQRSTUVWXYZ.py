"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def sauce(num1,num2) :
    """ซอสจัดเรียงข้อมูล"""
    if num1 < num2:
        return num1,num2
    return num2,num1

def main():
    """main"""
    ramdub = input()
    num1 = float(input())
    num2 = float(input())
    ant = float(input())
    mid, giant = sauce(num1,num2)
    if ant > giant:
        backup = ant
        ant = mid
        mid = giant
        giant = backup
    elif ant > mid:
        mid,ant = ant,mid
    if ramdub == "Ascend":
        print(f"{ant:.2f}, {mid:.2f}, {giant:.2f}")
    elif ramdub == "Descend":
        print(f"{giant:.2f}, {mid:.2f}, {ant:.2f}")
main()
