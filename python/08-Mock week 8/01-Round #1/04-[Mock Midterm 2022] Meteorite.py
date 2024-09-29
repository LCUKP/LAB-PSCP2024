"""[Mock Midterm 2022] Meteorite"""
def main():
    """[Mock Midterm 2022] Meteorite"""
    ukauka = float(input())
    tak = int(input())
    weight = float(input())
    countuka = 1
    count = 0
    while ukauka >= weight :
        count += countuka
        countuka *= tak
        ukauka /= tak
    print(count)
main()
