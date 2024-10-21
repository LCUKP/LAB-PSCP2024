"""[Mock Midterm 2023] Distribute"""
def main() :
    """[Mock Midterm 2023] Distribute"""
    money = int(input())
    child = int(input())
    count = 0
    tmp = 1
    if money > child*8 :
        count = -1
    if money < child :
        tmp = 0
    
    print(count if tmp else "Error")
main()
