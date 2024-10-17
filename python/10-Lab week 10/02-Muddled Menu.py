"""Muddled Menu"""
def main():
    """Muddled Menu"""
    menu = []
    while True:
        food = input().strip()
        if food == "DONE":
            break
        if food == "SOMETHING'S WRONG":
            menu = []
        elif food == "CLOSED":
            menu.clear()
            break
        elif "Can't do:" in food:
            item = food.split(": ")[1]
            menu.remove(item)
        else:
            item, indx = food.split(" #")
            if indx == "N":
                menu.append(item)
            else:
                menu.insert(int(indx) - 1, item)
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
main()
