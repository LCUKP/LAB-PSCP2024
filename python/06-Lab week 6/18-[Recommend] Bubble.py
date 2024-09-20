"""[Recommend] Bubble ไม่ผ่าน 4 เทสเคส"""
def main():
    """[Recommend] Bubble"""
    bubble = input()
    count = 0
    b = 1
    code = 0
    while len(bubble) > b :
        if bubble[b] == "o" :
            b += 1
            count+=1
        elif bubble[b] == "O":
            a = 1
            if bubble[b+2] in ("O","o","|") :
                a = 2
            if bubble[b+3] in ("O","o","|") :
                a = 3
            b += a
            count+=1
        elif bubble[b] == "|":
            count+=1
            break
        elif bubble[b] == " ":
            code = b
            break
    if code :
        print("IMPOSSIBLE")
        print(len(bubble)-code)
    else:
        print("POSSIBLE")
        print(count)
main()
#พัก มาเอารัย ;-;
