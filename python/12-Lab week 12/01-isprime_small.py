"""isprime_small"""
def is_prime(x):
    """is_prime"""
    n=0
    for i in range(x+1,2,-1):
        if not x%i and not i == x:
            n=1
            break
    return n,x
def main():
    """isprime_small"""
    n,x=is_prime(int(input()))
    print("Yes" if not n and x!=1 else "No")
main()
