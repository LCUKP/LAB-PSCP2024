"""[Mock Midterm 2022] Palindrome"""
def main() :
    """[Mock Midterm 2022] Palindrome"""
    num = int(input())
    time = input()
    count = 0
    while count != num :
        natee = int(time[-2:].replace(":","")) + 1
        hour = int(time[:2].replace(":",""))
        if not natee % 60 :
            natee = 0
            hour += 1
        if hour == 24 :
            hour = 0
        if natee < 10 :
            time = f"{str(hour)}:0{str(natee)}"
        else :
            time = f"{str(hour)}:{str(natee)}"
        if time.replace(":","") == time[::-1].replace(":","") :
            print(time)
            count += 1
main()
