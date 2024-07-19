"""Donut"""
def main():
    """main"""
    a = int(input()) #ราคา
    b = int(input()) #ถ้าซื้อโดนัทจำนวน b ชิ้น
    c = int(input()) #จะได้แถมอีก c ชิ้นฟรี
    d = int(input()) #ถ้าต้องการโดนัท d ชิ้น จ่ายเงินน้อยสุดกี่บาท และจะได้โดนัทมากสุดกี่ชิ้น
    donut = b + c
    price = a*b
    box = d // donut
    donut *= box
    remain = d  - donut
    if remain >= b:
        remain = b
        donut += (b+c)
    else :
        donut += remain
    price = box*price + remain*a
    print(price,donut)
main()
