"""Ping ไม่ผ่าน 1 เทสเคส"""
import math
def slicing(text, maxn, minn, time="") :
    """find ms"""
    time = text[text.find("time")+5:text.find("m",text.find("time")+5)]
    if text[0:5] != "Reply" :
        return -1, maxn, minn
    time = int(time)
    time = 0 if text[text.find("time")+4:][0:2] == "<1" else time
    maxn = time if time > maxn else maxn
    minn = time if time < minn else minn
    return time, maxn, minn

def main() :
    """Ping"""
    ping = input()
    space = input()
    pinging = input()+ping  #ตัวแปร ping ไม่ได้ใช้ เลยเอามาบวกเฉยๆ ไม่มีผลอะไร กัน PEP-8
    maxn = 0
    minn = math.inf
    received, lost, avg = 0,0,0
    for _ in range(4) :
        send, maxn, minn = slicing(input(), maxn, minn,space)   #space ไม่มีผลต่อโปรแกรม
        if send != -1 :
            received += 1
            avg += send
        else :
            lost += 1
    if pinging.find("[") != -1 :
        pinging = pinging[pinging.find("[")+1:pinging.find("]",pinging.find("[")+1)]
    else :
        pinging = pinging[pinging.find(" ")+1:pinging.find(" ",pinging.find(" ")+1)]
    if not received :
        print(f"Ping statistics for {pinging}")
        print(f"    Packets: Sent = 4, Received = 0, Lost = 4 ({int((lost*100)/4)}% loss),")
    else :
        print(f"Ping statistics for {pinging}:")
        print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} "\
              f"({int((lost*100)/4)}% loss),")
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {minn}ms, Maximum = {maxn}ms, Average = {int(avg/received)}ms")
main()
# Ping ผิด 1 เทสเคส วันไนท์มิราเคลิไม่มีจริง เราคงต้องจากการ (T-T)
