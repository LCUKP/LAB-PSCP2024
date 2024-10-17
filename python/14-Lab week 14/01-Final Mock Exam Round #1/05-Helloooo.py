"""Helloooo"""
def main(txt) :
    """Helloooo"""
    newtxt = ""
    bol = True
    for i in txt[::-1] :
        if i in "aeiouAEIOU" and bol:
            newtxt += i*4
            bol = False
        else :
            newtxt += i
    print(newtxt[::-1])
main(input())
