"""BusStop I"""
def main() :
    """BusStop I"""
    length = int(input())
    delegates = int(input())
    runner = [input().split() for _ in range(delegates)]
    winner = 0
    speed = 0
    while winner == 0 :
        for i in range(delegates) :
            tmp = int(runner[i][0]) + int(runner[i][1])
            runner[i][1] = tmp
            if tmp >= length and int(runner[i][0]) >= speed :
                winner = i + 1
                speed = int(runner[i][0])
    print(winner)
main()
