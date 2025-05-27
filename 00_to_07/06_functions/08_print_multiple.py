

def print_mess(mess:str,repeat:int):
    for i in range(repeat):
        print(mess,i)

def main():
    user_mess = str(input('Enter a message: '))
    repaetd_time = int(input('Enter a number to repaet the message: '))

    print_mess(user_mess,repaetd_time)

if __name__ == "__main__":
    main()