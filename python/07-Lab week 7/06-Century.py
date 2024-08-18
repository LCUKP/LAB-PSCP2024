"""Century"""
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        year = input()
        if year[0] == "B":  #เช็คสตริงตัวแรก ว่าเป็น พ.ศ. หรือ ค.ศ.
            result = math.ceil((int(year[5:])-543)/100)
            if result <= 0 :
                print("ERROR")
            else :
                print(result)
        elif year[0] =="A": #เช็คสตริงตัวแรก
            result = math.ceil(int(year[5:])/100)
            if result <= 0 :
                print("ERROR")
            else :
                print(result)
main()
