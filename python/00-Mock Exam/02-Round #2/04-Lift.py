"""Lift"""
def main():
    """Lift"""
    num = int(input())
    w = float(input())
    allw = 0
    saftornot = "Not Safe"
    for _ in range(num):
        years = int(input())
        weight = float(input())
        allw += weight
        if years >= 12:
            saftornot = "Safe"
    if allw > w :
        saftornot = "Not Safe"
    if num != 0 :
        print(saftornot)
    else :
        print("Safe")
main()
