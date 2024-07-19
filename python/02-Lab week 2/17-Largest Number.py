"""Largest Number"""
def sauce(num1,num2) :
    """sauce"""
    if num1 < num2:
        return num1,num2
    return num2,num1

def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    ant = int(input())
    mid, giant = sauce(num1,num2)
    if ant > giant:
        backup = ant
        ant = mid
        mid = giant
        giant = backup
    elif ant > mid:
        mid,ant = ant,mid
    print(f"{giant}{mid}{ant}")
main()
# False
