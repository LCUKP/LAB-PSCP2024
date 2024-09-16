"""iPhone 13 Again"""
iphone = input()
rom = input()
if iphone == "iPhone 13 mini" :
    if rom == "128 GB" :
        print("25900")
    elif rom == "256 GB" :
        print("29900")
    elif rom == "512 GB" :
        print("37900")
    else :
        print("Not Available")
elif iphone == "iPhone 13" :
    if rom == "128 GB" :
        print("29900")
    elif rom == "256 GB" :
        print("33900")
    elif rom == "512 GB" :
        print("41900")
    else :
        print("Not Available")
elif iphone == "iPhone 13 Pro" :
    if rom == "128 GB" :
        print("38900")
    elif rom == "256 GB" :
        print("42900")
    elif rom == "512 GB" :
        print("50900")
    elif rom == "1 TB" :
        print("58900")
    else :
        print("Not Available")
elif iphone == "iPhone 13 Pro Max" :
    if rom == "128 GB" :
        print("42900")
    elif rom == "256 GB" :
        print("46900")
    elif rom == "512 GB" :
        print("54900")
    elif rom == "1 TB" :
        print("62900")
    else :
        print("Not Available")
else :
    print("Not Available")
