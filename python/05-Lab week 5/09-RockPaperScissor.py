"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    text = input()
    lenght = len(text)
    scoreA = 0
    scoreB = 0
    for i in range(0, lenght, 2):
        text2 = text[i: i + 2]
        if text2 == "RP":
            scoreB += 1
        elif text2 == "RS":
            scoreA += 1
        elif text2 == "SR":
            scoreB += 1
        elif text2 == "SP":
            scoreA += 1
        elif text2 == "PR":
            scoreA += 1
        elif text2 == "PS":
            scoreB += 1
    if scoreA > scoreB:
        print(f"A win {scoreA}-{scoreB}")
    elif scoreA < scoreB:
        print(f"B win {scoreB}-{scoreA}")
    else:
        print("DRAW",scoreA)
main()
