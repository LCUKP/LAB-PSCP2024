"""Safe"""
def main() :
    """Safe"""
    code = input()
    encode = input()
    roter = 0
    for i,v in enumerate(code) :
        if v != encode[i] :
            if abs(ord(v) - ord(encode[i])) > 13 :
                roter += min(abs(ord(v) - (ord(encode[i])-26)), abs((ord(v)-26) - ord(encode[i])))
            else :
                roter += (abs(ord(v) - ord(encode[i])))
    print(roter)
main()
