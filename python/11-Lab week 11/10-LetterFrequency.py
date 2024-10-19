"""LetterFrequency"""
def main() :
    """LetterFrequency"""
    txt = input().replace(" ","").lower()
    strg = ""
    count = 0
    for i in list(set(txt)) :
        if txt.count(i) > count :
            strg = i
            count = txt.count(i)
    print(strg)
main()
