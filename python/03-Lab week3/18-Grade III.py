"""Grade III"""
def main():
    """main"""
    num = int(input())
    grade = 0
    for _ in range(0,num):
        score = float(input())
        if score >= 95 :
            grade += 4
        elif score >= 90 :
            grade += 3.5
        elif score >= 85 :
            grade += 3
        elif score >= 80 :
            grade += 2.5
        elif score >= 75 :
            grade += 2
        elif score >= 70 :
            grade += 1.5
        elif score >= 65 :
            grade += 1
        elif score >= 60 :
            grade += 0.5
        else :
            grade += 0
    gpa = grade/num
    print(f"{int(gpa*100)/100:.2f}")
main()
