"""SurprisingVote"""
def main():
    """main"""
    sumvote = float(input())
    most = float(input())
    mn = 0
    if most*2 < sumvote:
        mn = abs(sumvote-most*2)
    if mn > (most+2) or mn < (most-2):
        print("Surprising")
    else :
        print("Not surprising")
main()
