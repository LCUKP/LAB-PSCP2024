"""Cat Parade"""
def main() :
    """Cat Parade"""
    parade = []
    count = []
    while True :
        pat = input()
        if pat == "END" :
            break
        if pat != "IT'S A DOG" :
            for i in pat.split(", ") :
                parade.append(i)
                if i not in count :
                    count.append(i)
        elif pat == "IT'S A DOG" :
            parade.pop()
            count.pop()
    count.sort()
    for meow in count :
        print(meow, parade.index(meow)+1, parade.count(meow))
main()
