"""mod doc"""
def main():
    """doc"""
    x = int(input())
    service = x*0.1
    if service < 50:
        service =50
    elif service >1000:
        service =1000
    x += service
    x += x*0.07
    print(f"{x:.2f}")
main()
