"""Seeker"""
def main(txt, count = 0, tmp = "0") :
    """Seeker"""
    for i in txt :
        if i.isnumeric() :
            tmp += i
        else :
            count += int(tmp)
            tmp = "0"
    print(count+int(tmp))
main(input())
