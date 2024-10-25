"""[Recommend] MultiplyMatrixPQR"""
def main() :
    """[Recommend] MultiplyMatrixPQR"""
    p = int(input())
    q = int(input())
    r = int(input())
    a = []
    b = []
    for _ in range(p) :
        tmp = []
        for _ in range(q) :
            tmp.append(int(input()))
        a.append(tmp)
    for _ in range(q) :
        tmp = []
        for _ in range(r) :
            tmp.append(int(input()))
        b.append(tmp)
    ab = []
    for _ in range(r) :
        for i in range(p) :
            tmp = []
            for j in range(q) :
                num1 = a[i][j]
                num2 = b[j][i]
                tmp.append(num1*num2)
            ab.append(sum(tmp))
    print(ab)
main()
