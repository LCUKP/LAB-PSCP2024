"""MAC"""
def main() :
    """MAC"""
    mac = input()
    valid = 0
    if len(mac) == 14 and mac[4] == "." and mac[9] == "." :
        mac = mac.replace(".","",2)
        valid = 3
        for i in mac :
            if i not in ("a","b","c","d","e","f","A","B","C","D","E","F",\
                        "1","2","3","4","5","6","7","8","9","0") :
                valid = 0
                break
    elif len(mac) == 17 and mac[2] + mac[5] + mac[8] + mac[11] + mac[14] == ":::::" :
        mac = mac.replace(":","",5)
        valid = 2
        for i in mac :
            if i not in ("a","b","c","d","e","f","A","B","C","D","E","F",\
                        "1","2","3","4","5","6","7","8","9","0") :
                valid = 0
                break
    elif len(mac) == 17 and mac[2] + mac[5] + mac[8] + mac[11] + mac[14] == "-----" :
        mac = mac.replace("-","",5)
        valid = 1
        for i in mac :
            if i not in ("a","b","c","d","e","f","A","B","C","D","E","F",\
                        "1","2","3","4","5","6","7","8","9","0") :
                valid = 0
                break
    if valid :
        print(f"VALID {valid}")
    else :
        print("ERROR")
main()
