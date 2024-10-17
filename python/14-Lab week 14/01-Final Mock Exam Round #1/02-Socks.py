"""Socks"""
def main() :
    """Socks"""
    txt = input()
    counted = sorted(list(set(txt)))
    count = 0
    socks = ""
    for i in counted :
        tmp = txt.count(i) // 2
        socks += ((i*2)+" ")*tmp
        count += tmp
    print(socks if socks != "" else "None")
    print(count)
main()
