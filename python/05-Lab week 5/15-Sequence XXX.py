"""Sequence XXX"""
def main() :
    """Sequence XXX"""
    numr = int(input())
    numc = int(input())
    for i in range(numr) :
        for _ in range(numc) :
            for j in range(numr) :
                if (not j) or (not i) or (i == j) or (i + j == numr - 1) :
                    print("*", end="")
                elif (j == numr - 1) or (i == numr - 1) :
                    print("*", end="")
                else:
                    print(" ", end="")
            print(end=" ")
        print()
main()
