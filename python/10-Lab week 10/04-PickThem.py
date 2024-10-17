'''PickThem'''
def main():
    '''PickThem'''
    old_list = input()
    old_list = old_list.strip('[]').split(',')
    new_list = []
    for i in old_list:
        if not int(i)%2:
            new_list.append(i)
    if not new_list:
        print('Nope')
    else:
        for j in new_list:
            print(j.strip(' '))
main()
