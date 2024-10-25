"""[Recommend] VerticalHistogram"""
def main() :
    """[Recommend] VerticalHistogram"""
    txt = input()
    listtxt = sorted(list(set(txt)))
    dick = {}
    most = 0
    for i in listtxt :
        if i.isalpha() :
            dick.update({i:list("*"*txt.count(i))})
            if txt.count(i) > most :
                most = txt.count(i)
    for ii in range(most,0,-1) :
        print(f"{ii:>2}",end="  ")
        for v in listtxt :
            if v.isalpha() :
                print(" " if dick[v][ii-1:ii] == [] else "*",end=" ")
        print()
    print(end="    ")
    for iii in listtxt :
        if iii.isalpha() :
            print(iii,end=" ")
main()
