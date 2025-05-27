def double_num(num:int):
    return num * 2


def main():
    user_input = int(input("Enter a number"))

    num_result = double_num(user_input)
    print(num_result)

if __name__ == '__main__':
    main()