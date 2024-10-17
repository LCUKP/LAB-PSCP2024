"""Classify"""
def main() :
    """Classify"""
    mystd = []
    tmp = ""
    while True :
        std = input()[0:4]
        if std == "END" :
            break
        mystd.append(std)
    mystd.sort()
    for i in list(dict.fromkeys(mystd)) :
        if i[:2] != tmp :
            print(i[:2], int(i[2:]), mystd.count(i))
        else :
            print("--", int(i[2:]), mystd.count(i))
        tmp = i[:2]
main()
