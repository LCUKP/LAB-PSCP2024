"""Parity"""
def main():
    """Parity"""
    bits = input()
    parity = input()
    num = 0
    for i in bits:
        if i == "1" :
            num+=1
    if parity == "Even" :
        if not num % 2 :
            bits += "0"
        else :
            bits += "1"
    elif parity == "Odd":
        if not num % 2 :
            bits += "1"
        else :
            bits += "0"
    print(bits)
main()
