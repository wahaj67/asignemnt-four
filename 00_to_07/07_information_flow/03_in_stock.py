
def main():

    user= str(input('Enter fruit name: '))
    stock = in_stock(user)
    if stock == 0:
        return 'This fruit is not in inventory'
    else:
        print(stock)

def in_stock(fruit):
    if fruit == 'apple':
        return 2
    elif fruit == 'mango':
        return 1000
    elif fruit == 'banana':
        return 5

if __name__ == '__main__':
    main()