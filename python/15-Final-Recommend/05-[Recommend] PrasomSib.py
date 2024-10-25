"""[Recommend] PrasomSib"""
def main(nums, count = 0) :
    """[Recommend] PrasomSib"""
    for i,v in enumerate(nums) :
        tmp = int(v)
        while tmp < 10 :
            if i == len(nums) - 1 :
                break
            tmp += int(nums[i+1])
            i += 1
            if tmp == 10 :
                count += 1
    print(count)
main(list(input()))
