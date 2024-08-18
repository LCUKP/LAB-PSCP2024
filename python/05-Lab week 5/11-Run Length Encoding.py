"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    encodetxt = ""
    count = 1
    i = 0
    while i < len(text):
        for j in range(i+1,len(text)):
            if text[i] == text[j] :
                count += 1
            else :
                break
        encodetxt += str(count)+text[i]
        i += count
        count = 1
    print(encodetxt)
main()
