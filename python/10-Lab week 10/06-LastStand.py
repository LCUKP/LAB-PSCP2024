'''LastStand'''
import json
def main():
    '''LastStand'''
    old_list = json.loads(input())
    new_list = []
    for i in old_list:
        last = str(i)[-1:]
        new_list.append(last)
    for j in new_list:
        print(j)
main()
