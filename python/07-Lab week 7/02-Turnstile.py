"""Turnstile"""
def main():
    """Turnstile"""
    text = input()
    cp = text
    count = 0
    while text != "END" :
        text = input()
        cp += text
    i = 0
    while i < len(cp) :
        ch = cp[i:i+2]
        if ch == "CP" :
            count += 1
        i += 1
    print(count)
main()
