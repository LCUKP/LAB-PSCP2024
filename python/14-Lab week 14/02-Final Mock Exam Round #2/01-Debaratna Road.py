"""Debaratna Road"""
def main() :
    """Debaratna Road"""
    num = abs(float(input()))
    if num <= 5.032 :
        print("Bangkok")
    elif num <= 35.477 :
        print("Samut Prakarn")
    elif num <= 52.900 :
        print("Chachoengsao")
    elif 52.900 < num <= 58.855 :
        print("Chon Buri")
    else :
        print("InValid")
main()
