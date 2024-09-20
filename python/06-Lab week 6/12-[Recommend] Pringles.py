"""[Recommend] Pringles"""
def main():
    """[Recommend] Pringles"""
    up = input()
    pringles = input()
    bott = input()
    fingle = int(input())
    count = 0
    n,k = 0,1
    for i,v in enumerate(pringles) :
        if fingle > 0 :
            if v == ")" :
                count += 1
                pringles = pringles.replace(pringles[i]," ",1)
            fingle -= 1
    print(count)
    for j in pringles :
        if j == ")" :
            n,k = 1,0
    print("There are still some left."*n+"None."*k)
    print(up)
    print(pringles)
    print(bott)
main()
