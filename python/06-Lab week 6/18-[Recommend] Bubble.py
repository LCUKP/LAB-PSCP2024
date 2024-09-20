"""[Recommend] Bubble ไม่ผ่าน 5 เทสเคส"""
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
            b += 3
            count+=1
        elif bubble[b] == "|":
            count+=1
            break
        elif bubble[b] == " ":
            if bubble[b-3] == "O" :
                code = b-2
            else :
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
