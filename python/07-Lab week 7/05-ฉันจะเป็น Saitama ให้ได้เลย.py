"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def source(num1,num2):
    """อร่อย"""
    if num1 > num2 :
        return num1
    return num2
def main():
    """ฉันจะเป็น Saitama ให้ได้เลย"""
    wid = int(input())
    situp = int(input())
    upsit = int(input())
    run = int(input())
    wid_me = int(input())
    situp_me = int(input())
    run_me = int(input())
    upsit_me = int(input())
    day_wid = math.ceil(wid / wid_me)
    day_situp = math.ceil(situp / situp_me)
    day_upsit = math.ceil(upsit / upsit_me)
    day_run = math.ceil(run / run_me)
    print(source(source(day_wid,day_situp),source(day_upsit,day_run)))
main()
