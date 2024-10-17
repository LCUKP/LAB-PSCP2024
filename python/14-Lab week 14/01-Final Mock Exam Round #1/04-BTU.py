"""BTU"""
def main() :
    """BTU"""
    area = int(input())
    height = int(input())
    people = int(input())
    room = input()
    sun = input()
    btu = 0
    if 100 <= area <= 150 :
        btu = 5000
    elif area <= 250 :
        btu = 6000
    elif area <= 300 :
        btu = 7000
    elif area <= 350 :
        btu = 8000
    elif area <= 400 :
        btu = 9000
    elif area <= 450 :
        btu = 10000
    elif area <= 550 :
        btu = 12000
    else :
        btu += ares(area)
    btu += (high(height)*1000) + (person(people)*600) + (rooms(room))
    btu += (sunsu(sun,btu))
    print(f"{btu:.0f}")
def high(num) :
    """high"""
    if num > 8 :
        return num - 8
    return 0
def person(num) :
    """person"""
    if num > 2 :
        return num - 2
    return 0
def rooms(txt) :
    """kitchen"""
    if txt == "kitchen" :
        return 4000
    return 0
def sunsu(txt,btu) :
    """sun"""
    if txt == "facing the sun" :
        return btu*.1
    elif txt == "shaded" :
        return -btu*.1
    return 0
def ares(num) :
    """ares"""
    if num <= 700 :
        return 14000
    elif num <= 1000 :
        return 18000
    elif num <= 1200 :
        return 21000
    elif num <= 1400 :
        return 23000
    elif num <= 1500 :
        return 24000
    elif num <= 2000 :
        return 30000
    elif num <= 2500 :
        return 34000
main()
