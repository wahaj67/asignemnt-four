def add_numbers(numbers)->int:

    total_so_far:int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers:list = [2,6,9,10,10090,26,76]
    sum_of_numbers:int = add_numbers(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()
