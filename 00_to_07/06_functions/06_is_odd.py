def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')

def is_odd(value:int):

    remiander = value % 2
    return remiander == 1

if __name__ == '__main__':
    main() 
