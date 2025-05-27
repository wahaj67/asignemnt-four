
ADULT_AGE = 18

def is_adult(age:int):
    if age >= ADULT_AGE:
        return True
    return False

def main():

    user_age = int(input("Enter Your age ! "))

    is_adult(user_age)

if __name__ == '__main__':
    main()