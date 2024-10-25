"""[Recommend] TicTacToe"""
def main() :
    """[Recommend] TicTacToe"""
    row = [input() for _ in range(3)]
    if row[0] in ("XXX","OOO") :
        print(row[0][0],"WIN")
    elif row[1] in ("XXX","OOO") :
        print(row[1][0],"WIN")
    elif row[2] in ("XXX","OOO") :
        print(row[2][0],"WIN")
    elif row[0][0] == row[1][0] == row[2][0] and row[0][0] != "-" :
        print(row[0][0],"WIN")
    elif row[0][1] == row[1][1] == row[2][1] and row[0][1] != "-" :
        print(row[0][1],"WIN")
    elif row[0][2] == row[1][2] == row[2][2] and row[0][2] != "-" :
        print(row[0][2],"WIN")
    elif row[0][0] == row[1][1] == row[2][2] and row[0][0] != "-" :
        print(row[0][0],"WIN")
    elif row[2][0] == row[1][1] == row[0][2] and row[0][2] != "-" :
        print(row[0][2],"WIN")
    else :
        print("DRAW")
main()
