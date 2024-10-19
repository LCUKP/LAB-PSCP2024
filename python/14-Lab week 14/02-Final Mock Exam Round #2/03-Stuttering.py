"""Stuttering"""
def main() :
    """Stuttering"""
    txt = input().split()
    new_txt = ""
    for i,v in enumerate(txt) :
        if v == txt[i-1] :
            continue
        new_txt += v+ " "
    if new_txt == "" :
        print(txt[0])
    else :
        print(new_txt)
main()
