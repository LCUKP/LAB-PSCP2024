"""Gift II"""
num = []
def loop_append(i=8):
    """loop_append"""
    if i > 0:
        num.append(int(input()))
        loop_append(i-1)
def find_even_gift(i=0):
    """find_even_gift"""
    if i < 8 :
        if not num[i] % 2:
            print(num[i])
        find_even_gift(i+1)
loop_append()
find_even_gift()
