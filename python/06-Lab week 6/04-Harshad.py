"""Harshad"""
def main():
    """Harshad"""
    for _ in range(10):
        num = abs(int(input()))
        sumnum = 0
        for i in range(len(str(num))):
            sumnum += int(str(num)[i])
        if sumnum and not num % sumnum :
            print("Yes")
        else :
            print("No")
main()
