def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    division = num1 / num2
    remainder = num1 % num2

    print(f'The division of {num1} and {num2} is {division}')
    print(f'The remainder of {num1} and {num2} is {remainder}')

if __name__ == "__main__":
    main()