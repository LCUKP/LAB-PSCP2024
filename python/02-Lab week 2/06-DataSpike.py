"""DataSpike"""
def mex(num,dfnum):
    """fine mex"""
    if num >= dfnum:
        dfnum = num
    return dfnum

def main(i=8,mexx = 0):
    """main"""
    if i > 0 :
        mexx = mex(int(input()),mexx)
        main(i-1,mexx)
    else :
        print(mexx)
main()
