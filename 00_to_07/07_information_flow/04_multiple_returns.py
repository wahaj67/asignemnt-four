
def user_data():
    first_name = str(input('What is your first name: '))
    last_name = str(input('What is your last name:'))
    email = str(input('Whats is your email:'))

    return first_name,last_name,email

def main():
    get_user = user_data()
    print(f'Recived the following user data: {get_user}')

if __name__ == '__main__':
    main()
