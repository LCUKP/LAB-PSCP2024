"""[Final 2020 + Recommend] Bus Seat"""
def main() :
    """[Final 2020 + Recommend] Bus Seat"""
    col = int(input())
    row = int(input())
    seat = int(input())
    all_seat = []
    i = 1
    while i < col*row :
        tmp = []
        for j in range(i,i+col) :
            tmp.append(j)
        i += col
        all_seat.append(tmp)
    for x in range(col-1,-1,-1) :
        for j in range(row) :
            if all_seat[j][x] == seat :
                print("XX",end=" ")
            else :
                print(f"{all_seat[j][x]:>02}",end=" ")
        print()
        if not x%2 and x :
            print()
main()
