"""Sequence XII"""
def main() :
    """Sequence XII ลองผิดลองถูกไปมา ถูกเฉย"""
    num = int(input())
    for i in range(-num,num+1):
        # ไม่ทำแถว 1 กับ 0
        if i and i != 1:
            for j in range(-num,num+1):
                # ไม่ทำคอลัม 1 กับ 0
                if j and j != 1:
                    if abs(j)>=abs(i):
                        #abs j มากกว่าหรือเท่ากับ abs i ให้ abs j - abs i + num
                        print(f"{abs(i)-abs(j)+num:>02}",end=" ")
                    else :
                        #ให้ abs j - abs i - num
                        print(f"{abs(abs(i)-abs(j)-num):>02}",end=" ")
            print()
main()
