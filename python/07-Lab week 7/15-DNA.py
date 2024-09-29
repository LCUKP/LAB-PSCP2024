"""DNA ทำไม่เสร็จจร้า Not yet"""
def main() :
    line1 = input()
    line2 = input()
    loop = max(len(line1),len(line2))
    for i in range(loop) :
        print(line2[i])
main()
