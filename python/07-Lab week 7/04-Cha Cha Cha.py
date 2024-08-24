"""Cha Cha Cha"""
import math
def main():
    """Cha Cha Cha"""
    day = int(input())
    hour = 0
    for _ in range(day):
        hour += math.ceil(float(input()))
    print(int(hour*8720))
main()
