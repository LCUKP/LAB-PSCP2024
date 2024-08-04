"""Align"""
import math
def main():
    """Align"""
    num = int(input())
    side = input()
    txt = input()
    lenght = len(txt)
    if side == "left":
        print(txt + " " * (num - lenght))
    elif side == "right":
        print(" " * (num - lenght) + txt)
    elif side == "center":
        delete = num - lenght
        left = math.ceil(delete / 2)
        right = math.floor(delete / 2)
        print(" " * left + txt + " " * right)
main()
