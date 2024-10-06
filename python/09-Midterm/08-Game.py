"""Game"""
def main():
    """Game"""
    ascore = int(input())
    bscore = int(input())
    if ascore%3 == bscore%3 :
        print(ascore%3)
    else :
        print("Error")
main()
