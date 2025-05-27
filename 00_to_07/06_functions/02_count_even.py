def count_even(lst):
    """Returns number of even number in lists
     
       """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count  += 1
    print(count)

def get_lists_of_ints():
    """
    Reads in integers until the user presses enter and returns the resultings lists 
    """

    lst = []
    user_input = input('Enter an integer or press enter to stop :')
    while user_input  != '':
        lst.append(int(user_input))
        user_input = input('Enter an integer or press enter to stop')
    return lst

def main():
    lst = get_lists_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()