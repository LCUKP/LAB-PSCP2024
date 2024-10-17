"""RemoveTag"""
def main() :
    """RemoveTag"""
    tag = input()
    while tag.count("<") and tag.count(">") :
        tmp = tag[tag.find("<"):tag.find(">")+1]
        tag = tag.replace(tmp," ")
    print(tag.split())
main()
