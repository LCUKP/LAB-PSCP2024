"""CompositeFunction"""
num = int(input())
def f(x):
    """Function"""
    return x*2

def g(x):
    """Function"""
    return (x/2)+1
print(f"{f(g(num)):.2f}")
print(f"{g(f(num)):.2f}")
