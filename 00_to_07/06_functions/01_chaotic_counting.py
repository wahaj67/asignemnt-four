import random
DONE_LIKE_HOOD = 0.2

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)

def done():
    """Returns True  with a Probablity of DONE_LIKE_HOOD"""
    if random.random() < DONE_LIKE_HOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until i feel like stopping which ever comes first ")
    chaotic_counting()
    print("I'm done !")

if __name__ == '__main__':
    main()