"""SecondConverter"""
def main():
    """SecondConverter"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    sec = k
    mins = sec//s
    sec = sec%s
    hour = mins//m
    mins = mins%m
    hour = hour%h
    print(hour,mins,sec,sep=":")
main()
