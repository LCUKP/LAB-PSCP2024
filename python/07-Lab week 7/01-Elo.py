"""Elo"""
def main(ra,rb,select):
    """Elo"""
    if select == "A" :
        return 1/(1+(10**((rb-ra)/400)))
    return 1/(1+(10**((ra-rb)/400)))
print(f"{main(int(input()),int(input()),input()):.2f}")
