"""CaesarV1"""
def main():
    """CaesarV1"""
    n = int(input())
    t = input()
    s=""
    for i in t:
        if i.isalpha():
            if i.islower():
                y=ord(i)+n
                if y<97:
                    y+=26
                elif y>122:
                    y-=26
                s+=chr(y)
            else:
                y=ord(i)+n
                if y<65:
                    y+=26
                elif y>90:
                    y-=26
                s+=chr(y)
        else:
            s+=i
    print(s)
main()
