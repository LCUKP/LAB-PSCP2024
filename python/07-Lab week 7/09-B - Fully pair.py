"""B - Fully pair?"""
def main():
    """B - Fully pair?"""
    text = input()
    ans = ""
    for i in text:
        num = text.count(i)
        if num%2 >= 1:
            if ans.find(i) <0:
                ans += i
    if not ans:
        print("fully paired")
    else:
        print(ans)
main()
