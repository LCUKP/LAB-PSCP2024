"""mod doc"""
def main():
    """doc"""
    n = int(float(input())*100)
    k = int(input())
    for _ in range(k):
        n = n+((n*381)//10000)
    print((f"{(n//100):d}.{(n%100):02d}"))
main()
