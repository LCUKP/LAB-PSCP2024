"""EuclideanDistance2D"""
import math
def main():
    """main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    Euclidean_distance = math.sqrt(((q1-p1)**2)+((q2-p2)**2))
    print(Euclidean_distance)
main()
