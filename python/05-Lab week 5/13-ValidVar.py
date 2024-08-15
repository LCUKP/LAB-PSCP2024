"""ValidVar"""
def main():
    """ValidVar"""
    num = int(input())
    for _ in range(num):
        variable = input()
        if variable in ("if", "else", "elif", "while", "for", "True", "False",\
        "continue","break","return", "is", "in", "and", "or", "from", "as",\
        "pass", "not", "def", "None") :
            print("Invalid")
        elif variable.isidentifier() :
            print("Valid")
        else :
            print("Invalid")
main()
