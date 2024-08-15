"""PhoneNumber"""
def main():
    """PhoneNumber"""
    num = input()
    typep = input()
    if typep == "Domestic":
        if len(num) == 9 :
            print(f"{num[0]} {num[1:5]} {num[5:9]}")
        elif len(num) == 10:
            print(f"{num[0:2]} {num[2:6]} {num[6:11]}")
    elif typep == "International":
        if len(num) == 9 :
            print(f"+66 {num[1:5]} {num[5:9]}")
        elif len(num) == 10:
            print(f"+66{num[1]} {num[2:6]} {num[6:11]}")
main()
