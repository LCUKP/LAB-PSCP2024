"""Calculator"""
def main():
    """Calculator"""
    num = int(input())
    strg = ""
    for i in range(1,num+1):
        if num != 1:
            strg += str(i)+"+"
    cout = 0
    for _ in strg:
        cout += 1
    if num == 1 :
        print(1)
    else:
        print(cout)
main()
