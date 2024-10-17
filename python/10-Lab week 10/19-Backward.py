"""Backward"""
def main() :
    """Backward"""
    my_list = []
    data = input()
    while data != "NULL" :
        my_list.append(data)
        data = input()
    my_list = my_list[::-1]
    for i in my_list :
        print(i)
main()
