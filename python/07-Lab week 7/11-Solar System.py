"""Solar System ทำไม่เสร็จจร้า Not yet"""
def main() :
    """Solar System"""
    txt = input()
    lentxt = txt.count(" ")
    lenstr = len(txt) - 1
    isun = txt.find("Sun") + 4
    if txt.index("Sun") == 0 :
        print("Hot: "+txt[isun :][ :txt[isun:].find(" ")])
        print(f"Cool: {txt[lenstr]}")
    # elif txt.index("Sun") == lentxt : 
    #     print(f"Hot: {txt[lentxt - 1]}")
    #     print(f"Cool: {txt[0]}")
    # elif 0 < txt.index("Sun") < lentxt :
    #     i = txt.index("Sun")
    #     print(f"Hot: {txt[i-1]} {txt[i+1]}")
    #     if abs(i - lentxt) > i :
    #         print(f"Cool: {txt[-1]}")
    #     elif abs(i - lentxt) < i :
    #         print(f"Cool: {txt[0]}")
    #     else :
    #         print(f"Cool: {txt[0]} {txt[-1]}")
    print(txt[isun:].find(" "))
main()
