
def one_digit(num:int):
  print('One digit is: ', num % 10)

def main():
 num = int(input('Enter a number: '))
 one_digit(num)


if __name__ == '__main__':
    main()