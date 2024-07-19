"""WeightStation"""
def main():
    """main"""
    avg = float(input())
    lor1 = float(input())
    lor2 = float(input())
    lor3 = float(input())
    lor4 = (avg*4)-(lor1+lor2+lor3)
    havg = avg/2
    overall = lor1+lor2+lor3+lor4
    if overall > 15000:
        print("Overweight")
    elif abs(avg-lor1) >= havg or abs(avg-lor2) >= havg \
    or abs(avg-lor3) >= havg or abs(avg-lor4) >= havg:
        print("Unbalance")
    else:
        print(f"Pass {lor4:.2f}")
main()
