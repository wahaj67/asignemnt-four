
def greet(name:str):
    return f"greeting {name}"

def main():

    user_input = str(input("Enter your name: "))
    print(greet(user_input))

if __name__ == '__main__':
    main()

