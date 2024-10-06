"""Real"""
def main():
    """Real"""
    num1 = check()
    num2 = check()
    num3 = check()
    dot = 0
    for i in num1+num2+num3:
        if i == '.':
            dot+=1
    if 'Error' in (num1+num2+num3) or dot>1:
        print('Error')
    elif '.' in num1:
        print(num1+num2+num3)
    elif num1 == '0' and num2 == '0' and num3 == '0': #000 -> 0.00
        print(num2+'.'+'00')
    elif num1 == '0' and num2 == '0' and num3 != '0' and not dot: #001 -> 1.00
        print(num3+'.00')
    elif num1 == '0' and num2 == '0' and num3 != '0' and '.' in num3: #001. -> 1.00
        print(num3+'00')
    elif '.' not in (num1,num2,num3) and num1 == '0' and not dot:
        print(num2+num3+'.00')
    elif num1 == '0' and '.' not in num1 and dot >0:
        print(num2+num3+'0')
    elif '.' in num2:
        print(num1+num2+num3+'0')
    elif '.' in num3:
        print(num1+num2+num3+'00')
    elif '.' not in (num1,num2,num3):
        print(num1+num2+num3+'.00')

def check():
    """check"""
    num = ''
    for _ in range(7):
        x = input()
        if x == 'on':
            x = '1'
            num+=x
        if x == 'off':
            x = '0'
            num+=x
    d = input()
    if d == 'on':
        return decode(num)+'.'
    return decode(num)

def decode(num):
    """decode"""
    if num == '1111110':
        num = '0'
    elif num == '0110000':
        num = '1'
    elif num == '1101101':
        num = '2'
    elif num == '1111001':
        num = '3'
    elif num == '0110011':
        num = '4'
    elif num == '1011011':
        num = '5'
    elif num == '1011111':
        num = '6'
    elif num == '1110000':
        num = '7'
    elif num == '1111111':
        num = '8'
    elif num == '1111011':
        num = '9'
    else:
        num = 'Error'
    return num
main()
