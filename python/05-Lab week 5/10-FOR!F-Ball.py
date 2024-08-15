"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    swap = input()
    posball = 1
    for i in swap:
        if i == "A":
            if posball == 1 :
                posball = 2
            elif posball == 2 :
                posball = 1
        elif i == "B":
            if posball == 2 :
                posball = 3
            elif posball == 3 :
                posball = 2
        elif i == "C":
            if posball == 1 :
                posball = 3
            elif posball == 3 :
                posball = 1
    print(posball)
main()
