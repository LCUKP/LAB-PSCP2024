"""Jumping"""
def jumping(num=1) :
    """jumping"""
    if num <= 4 :
        print_output(num)
        jumping(num+1)

def print_output(num,i=3) :
    """print_output"""
    if i :
        print(f"Output{num}")
        print_output(num,i-1)
jumping()
