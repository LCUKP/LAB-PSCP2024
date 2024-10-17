"""PickThemAgain"""
def main() :
    """PickThemAgain"""
    old_list = input().split()
    new_list = []
    for i in old_list:
        if not int(i)%3 or not int(i)%5:
            new_list.append(i)
    if not new_list :
        print('Nope')
    else:
        for j in range(len(new_list),0,-1):
            print(new_list[j-1])
main()
