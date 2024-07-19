"""BrickBridge"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())
    if (b*5) + a < goal or b%5 > a:
        print(-1)
    else:
        if b*5 >= goal:
            print(goal%5)
        else:
            print(goal-(b*5))
main()
