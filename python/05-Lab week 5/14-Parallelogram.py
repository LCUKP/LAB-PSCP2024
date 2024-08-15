"""Parallelogram"""
def main():
    """Parallelogram"""
    txt = input()
    for i in range(len(txt)-1,-len(txt),-1) :
        print(" "*(i),end="")
        if i > 0 :
            print(txt[-len(txt):-i])
        else :
            print(txt[-i:])
main()
