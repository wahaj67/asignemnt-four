import math 

def main():
    side_ab:float = float(input("Enter the length of AB: "))
    side_ac:float = float(input("Enter the length of AC: "))

    sum_of_squares:float = (side_ab ** 2) + (side_ac ** 2)

    hypothenius_bc:float = math.sqrt(sum_of_squares)

    print(f"The length of  BC (the hypothenius) is: {hypothenius_bc}")

if __name__ == "__main__":
    main()