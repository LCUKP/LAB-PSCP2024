"""BigFrame"""
def main():
    """BigFrame"""
    txt1 = input().strip()
    txt2 = input().strip()
    txt3 = input().strip()
    txt4 = input().strip()
    txt5 = input().strip()
    most = max(len(txt1),len(txt2),len(txt3),len(txt4),len(txt5))
    print("*"*(most+4))
    print("* "+txt1+" "*(most-len(txt1))+" *")
    print("* "+txt2+" "*(most-len(txt2))+" *")
    print("* "+txt3+" "*(most-len(txt3))+" *")
    print("* "+txt4+" "*(most-len(txt4))+" *")
    print("* "+txt5+" "*(most-len(txt5))+" *")
    print("*"*(most+4))
main()
