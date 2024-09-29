"""[Mock Midterm 2022] Volleyball"""
def main() :
    """[Mock Midterm 2022] Volleyball"""
    score = input()
    sets = 0
    winA = 0
    winB = 0
    scoreA = 0
    scoreB = 0
    win = 25
    for i in score :
        if i == "A" :
            scoreA += 1
        elif i == "B" :
            scoreB += 1
        if scoreA == win and (abs(scoreA - scoreB) >= 2) :
            sets += 1
            winA += 1
            print(f"Set {sets}: A ({scoreA}) | B ({scoreB})")
            scoreA = 0
            scoreB = 0
            if sets == 4 :
                win = 15
            else :
                win = 25
        elif scoreB == win and (abs(scoreA - scoreB) >= 2) :
            sets += 1
            winB += 1
            print(f"Set {sets}: A ({scoreA}) | B ({scoreB})")
            scoreA = 0
            scoreB = 0
            if sets == 4 :
                win = 15
            else :
                win = 25
        if (win in (scoreA, scoreB)) and not abs(scoreA - scoreB) >= 2 :
            win += 1
    if winA > winB and sets >= 3 and winA >= 3 :
        print(f"A won {winA}:{winB} set")
    elif winA < winB and sets >= 3  and winB >= 3 :
        print(f"B won {winB}:{winA} set")
    else :
        sets += 1
        print(f"Set {sets}: A ({scoreA}) | B ({scoreB})")
        print("The game has not finished yet.")
main()
#PEP-8 = 2, 0: Too many branches (13/12)
