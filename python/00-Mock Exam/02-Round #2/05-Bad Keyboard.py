"""Bad Keyboard"""
def main():
    """Bad Keyboard"""
    text = input()
    newtext = ""
    for i in text :
        if i == "i" :
            newtext += "o"
        elif i == "I" :
            newtext += "O"
        elif i == "o" :
            newtext += "i"
        elif i == "O" :
            newtext += "I"
        else :
            newtext += i
    print(newtext)
main()
