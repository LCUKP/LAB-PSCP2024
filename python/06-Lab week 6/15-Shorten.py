"""Shorten"""
def main() :
    """Shorten"""
    strg = ""
    lowr = None
    highr = None
    while True :
        num = int(input())
        if num == -1 :
            break
        if lowr is None :
            lowr = num
            highr = num
        else :
            if highr != num-1 :
                if lowr == highr :
                    strg += f"{lowr}, "
                else :
                    strg += f"{lowr}-{highr}, "
                lowr = num
                highr = num
            else :
                highr = num
    if lowr is not None :
        if lowr == highr :
            strg += f"{lowr}"
        else :
            strg += f"{lowr}-{highr}"
    print(strg)
main()
