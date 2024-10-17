"""AlmostMean"""
import math
def main():
    """AlmostMean"""
    num = int(input())
    student = []
    score = []
    total = 0
    min_list = math.inf
    a = 0
    c = 0
    for _ in range(num):
        data = input()
        student.append(data[:8])
        score.append(float(data[8:]))
    for i in score:
        total += i
    avg = total/num
    for i in score:
        if i > avg:
            a += 1
            continue
        x = avg - i
        if x < min_list:
            c = a
            min_list = x
        a += 1
    print(f"{student[c]}\t{score[c]}")
main()
