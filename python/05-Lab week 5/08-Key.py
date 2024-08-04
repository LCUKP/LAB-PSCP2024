"""Key"""
def main():
    """Key"""
    key = input()
    som = 0
    for i in key :
        som += int(i)
    num2 = int(key[10:13]) * 10
    num3 = som + num2
    if num3 < 1000 :
        num3 += 1000
    if len(str(num3)) >= 5:
        print(str(num3)[1:5])
    else :
        print(num3)
main()
