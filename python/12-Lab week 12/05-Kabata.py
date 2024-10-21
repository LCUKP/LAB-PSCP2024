"""Kabata"""
def main():
    """Kabata"""
    r=[]
    for _ in range(int(input())):
        n = input()
        if "baka" in n:
            r.append("no")
            continue
        n=n.replace("bakka","baka")
        m = len(n)
        s=""
        for i,j in zip(n,range(m)):
            if not j%2 and j:
                s+=" "
            s+=i
        s=s.split()
        for i in s:
            if not i in ("ka","ba","ta"):
                r.append("no")
                break
            if i==s[-1] and i in ("ka","ba","ta"):
                r.append("yes")
                break
    for i in r:
        print(i)
main()
