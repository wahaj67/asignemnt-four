def devisor(num:int):
    print('Here are the divisors of:',num)
    for i in range(num):
        curr_divisior = i + 1
        if num % curr_divisior:
            print(curr_divisior)
        
def main():
    num = int(input('Enter a number to check the divisior: '))
    devisor(num)

if __name__ == '__main__':
    main()