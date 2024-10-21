"""Easy Histogram ยังไม่ถูก"""
def main() :
    """Easy Histogram"""
    txt = input()
    dick = dict()
    for i in txt :
        if i != " " :
            dick.update({i:txt.count(i)})
    dick = dict(sorted(dick.items(),key=ord))
    for k,v in dick.items() :
        print(f"{k} = {v}")
main()
