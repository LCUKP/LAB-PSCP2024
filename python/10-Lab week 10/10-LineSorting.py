"""LineSorting"""
def main():
    """LineSorting"""
    num = int(input())
    texts = []
    for _ in range(num) :
        texts.append(input())
    texts.sort(key=len)
    for i in texts :
        print(i)
main()
