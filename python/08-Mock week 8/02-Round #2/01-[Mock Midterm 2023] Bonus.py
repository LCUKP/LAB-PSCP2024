"""Bonus"""
def main():
    """Bonus"""
    salary = int(input())
    years = int(input())
    month = int(input())
    if month >= 10 :
        years +=1
    if years > 20 :
        years = 20
    salary *= years
    if salary < 5000 :
        salary = 5000
    elif salary > 1000000 :
        salary = 1000000
    print(salary)
main()
