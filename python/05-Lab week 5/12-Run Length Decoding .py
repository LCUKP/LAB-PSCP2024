"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    decodetxt = ""
    tmp = ""
    for i in text:
        if i.isnumeric() :
            tmp += i
        else :
            decodetxt += i * int(tmp)
            tmp = ""
    print(decodetxt)
main()
