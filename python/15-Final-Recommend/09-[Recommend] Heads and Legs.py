"""Heads and Legs"""
def findleg ():
    """ok"""
    animal = int(input())
    leg = int(input())
    bird = 0
    rabbit = 0
    rabbit = ((leg-2)*animal)//2
    bird = animal - rabbit
    if animal == 0 and leg > 0:
        print("Impossible")
    elif rabbit < 0 or bird < 0:
        print("Impossible")
    else:
        print(rabbit,bird)
findleg()
