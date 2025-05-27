
def years_in_second():

    days_in_year = 365
    hours_in_day = 24
    minutes_in_hours = 60
    
    find_the_hours = days_in_year * hours_in_day
    print(find_the_hours,'hours in a yaear')

    find_the_minutes = find_the_hours * minutes_in_hours
    print(find_the_minutes,'minutes in a year')

    find_the_seconds = find_the_minutes * 60
    print(find_the_seconds,'seconds in a year')
   
if __name__ == "__main__":
    years_in_second()
    