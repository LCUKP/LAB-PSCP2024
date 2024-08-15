"""Sequence N"""
def main():
    """Sequence N"""
    num = int(input())
    for i in range(1,num+1):
        if i in (1,num):
            print("*"+" "*(num-2)+"*")
        else :
            print("*"+" "*(i-2)+"*"+" "*(num-(i+1))+"*")
main()
