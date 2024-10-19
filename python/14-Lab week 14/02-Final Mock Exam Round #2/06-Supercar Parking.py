"""Supercar Parking"""
def main() :
    """Supercar Parking"""
    txt = input()
    count = 0
    i = 0
    while i < len(txt) :
        if len(txt) == 1 and txt == "0":
            count += 1
        elif not i :
            if txt[i] == "0" and txt[i+1] == "0" :
                txt = txt[:i]+"1"+txt[i+1:]
                count += 1
        elif i == len(txt)-1 :
            if txt[i] == "0" and txt[i-1] == "0" :
                txt = txt[:i]+"1"+txt[i+1:]
                count += 1
            break
        elif txt[i] == "0" and txt[i-1] == "0" and txt[i+1] == "0" :
            txt = txt[:i]+"1"+txt[i+1:]
            count += 1
        i += 1
    print(count)
main()
