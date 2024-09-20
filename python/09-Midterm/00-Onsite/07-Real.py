"""Real"""
def digig(dis1):
    """digig"""
    text = ""
    if dis1 == "on on on on on on off ":
        text = "0"
    elif dis1 == "off on on off off off off ":
        text = "1"
    elif dis1 == "on on off on on off on ":
        text = "2"
    elif dis1 == "on on on on off off on ":
        text = "3"
    elif dis1 == "off on on off off on on ":
        text = "4"
    elif dis1 == "on off on on off on on ":
        text = "5"
    elif dis1 == "on off on on on on on ":
        text = "6"
    elif dis1 == "on on on off off off off ":
        text = "7"
    elif dis1 == "on on on on on on on ":
        text = "8"
    elif dis1 == "on on on on off on on ":
        text = "9"
    else :
        text = "Error"
    return text
def main():
    """Real"""
    dis1, dis2, dis3 = "","",""
    text1,text2,text3 = 0,0,0
    dot1,dot2,dot3 = "","",""
    for i in range(8) :
        t = input()
        if i <= 6 :
            dis1 += t+" "
            continue
        dot1 += t
    for j in range(8) :
        u = input()
        if j <= 6 :
            dis2 += u+" "
            continue
        dot2 += u
    for k in range(8) :
        v = input()
        if k <= 6 :
            dis3 += v+" "
            continue
        dot3 += v
    if digig(dis1) == "Error" or digig(dis2) == "Error" or digig(dis3) == "Error":
        print("Error")
    else :
        if dot1 == "on" :
            print(f"{digig(dis1)}.{digig(dis2)}{digig(dis3)}")
        elif dot2 == "on" :
            print(f"{digig(dis1)}{digig(dis2)}.{digig(dis3)}0")
        elif dot2 == "on" :
            print(f"{digig(dis1)}{digig(dis2)}{digig(dis3)}.00")
        else :
            print(f"{digig(dis1)}{digig(dis2)}{digig(dis3)}.00")
main()
#ไม่ถูกต้อง ไม่ได้คะแนน