"""import json"""
import json
def main() :
    """Filter"""
    score = json.loads(input())
    score = dict(sorted(score.items()))
    num = float(input())
    a = 1
    for i,v in score.items() :
        if v >= num :
            print(f"{i}\t{v:.2f}")
            a = 0
    if a :
        print("Nope")
main()
