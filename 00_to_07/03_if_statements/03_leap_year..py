
def get_leap_year(year):
    if(year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False

years = int(input("Enter a year: "))

print(get_leap_year(years))