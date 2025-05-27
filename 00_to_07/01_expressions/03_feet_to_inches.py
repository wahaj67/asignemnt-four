INCHES_IN_FOOT = 12
def feet_to_inches():
    feet = float(input("Enter feet:"))
    inches:float = feet * INCHES_IN_FOOT

    print(f"That is {inches} inches")

if __name__ == "__main__":
    feet_to_inches()
