def tri_perimeter():
    side1 = float(input("Enter side 1: "))
    side2  = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))

    perimetr = side1 + side2 + side3

    print("The perimeter of the triangle is", perimetr)

if __name__ == "__main__":
    tri_perimeter()