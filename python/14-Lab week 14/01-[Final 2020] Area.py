"""[Final 2020] Area"""
def main() :
    """[Final 2020] Area"""
    num = int(input())
    count = 0
    text = ""
    for _ in range(num) :
        text += input()
    for i in text :
        if i != " " :
            count += 1
    print(count)
main()
