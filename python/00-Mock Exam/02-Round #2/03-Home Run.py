"""Home Run"""
def main():
    """Home Run"""
    num = int(input())
    rang = float(input())
    count = 0
    for _ in range(num) :
        stadium = float(input())
        if rang > stadium :
            count+=1
    print(count)
main()
