"""Number Message"""
def main():
    """Number Message"""
    text = input()
    newtext = ""
    i = 0
    if "12" in text :
       text = text.replace("12","R")
    if "13" in text:
         text = text.replace("13","B")
    for i in text :
        if i == "1" :
            newtext += "I"
        elif i == "3" :
            newtext += "E"
        elif i == "4" :
            newtext += "A"
        elif i == "5" :
            newtext += "S"
        elif i == "0" :
            newtext += "O"
        else :
            if i in ("2","6","7","8","9") :
                continue
            newtext += i
    print(newtext.upper())
main()