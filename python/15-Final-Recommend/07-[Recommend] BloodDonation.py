"""[Recommend] BloodDonation"""
def main() :
    """[Recommend] BloodDonation"""
    age = int(input())
    weight = int(input())
    donatetime = int(input())
    cer = True
    if 17 == age or 60 <= age <= 70 :
        if input() == "False" :
            cer = False
    cond_age = 17 <= age <= 70
    cond_weight = weight >= 45
    cond_time = donatetime >= 1 or age <= 55
    if cond_age and cond_weight and cond_time and cer :
        print("Yes")
    else :
        print("No")
main()
