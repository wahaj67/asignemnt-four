def Calculate():

    degrees_fahrenheit = float(input("Enter Temperature in Fahrenheit: "))

    degree_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0  
    print("Temperature:" , degrees_fahrenheit, "F =", degree_celsius, "C")

if __name__ == "__main__":
    Calculate()
    