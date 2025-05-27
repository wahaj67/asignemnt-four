
def average(num1:float,num2:float):

    return (num1 + num2) / 2


def main():
    avg_1 = average(10,20)
    avg_2 = average(100,200)
    final = average(avg_1,avg_2)

    print(f"The average of 10 and 20 is {avg_1}")
    print(f"The average of 100 and 200 is {avg_2}")
    print(f"The average of {avg_1} and {avg_2} is {final}")
if __name__ == '__main__':
    main()

