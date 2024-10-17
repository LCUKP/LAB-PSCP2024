"""WordSequence II"""
def main(txt1, txt2) :
    """WordSequence II"""
    for i in range(max(len(txt1), len(txt2))+1) :
        print(f"{txt2[:i]}{txt1[i:]}")
main(input(), input())
