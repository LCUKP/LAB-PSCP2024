"""Median"""
import math
def main() :
    """Median"""
    num = int(input())
    num_list = []
    locate1 = 0
    locate2 = 0
    for _ in range(num) :
        num_list.append(float(input()))
    num_list = sorted(num_list)
    if not num % 2 :
        locate1 = int(math.floor((num+1)/2)-1)
        locate2 = int(math.ceil((num+1)/2)-1)
        print(f"{((num_list[locate1]+num_list[locate2])/2):.3f}")
    else :
        locate1 = int(((num+1)/2)-1)
        print(f"{(num_list[locate1]):.3f}")
main()
