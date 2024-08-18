"""Squid Game 3 - Tug-of-War"""
def main():
    """Squid Game 3 - Tug-of-War"""
    team_a = 0
    team_b = 0
    for _ in range(10): #รับค่าทีมละ 10 ผู้เล่น
        team_a += int(input())
    for _ in range(10):
        team_b += int(input())
    if team_a < team_b: #ทีมไหนน้อยกว่าตาย
        print("A")
    elif team_b < team_a:
        print("B")
    else:
        print("AB")     #เท่ากันตายคู่
main()
