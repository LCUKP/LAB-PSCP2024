"""mod doc"""
def main():
    """doc"""
    ball = float(input())
    count = 0
    while ball >= 0.01:
        count += 1
        ball = ball*(0.6)
    print(count-1)
main()
