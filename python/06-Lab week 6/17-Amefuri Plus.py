"""Amefuri Plus"""
H = int(input())
state = input()
WET = 8
DAY = 0
for i in state :
    if 6 <= H < 18 :
        DAY = 1
    elif 0 <= H < 6 or 18 <= H <= 24 :
        DAY = 0
    if i in ("C","c") :
        WET -= 0.5 if DAY else 0.25
    elif i in ("N","n") :
        WET -= 1 if DAY else 0.50
    elif i in ("W","w") :
        WET -= 1.50 if DAY else 0.75
    elif i in ("R","r") :
        WET += 2
    elif i in ("S","s") :
        WET += 3
    elif i in ("H","h") :
        WET = -69
        break
    if not WET :
        break
    if WET > 16 :
        WET = 16
    H += 1
    if H > 24 :
        H = 1
if WET == -69 :
    print("Lost")
elif not WET :
    print("Dry")
elif WET > 0 :
    print(f"Still Wet (Wet Level: {WET:.2f})")
