
def make_sentence(word:str,parts_of_speech:int):
    if parts_of_speech ==0:
        print("I'm excited to add this " + word + "to my vast collection of them !" )
    elif parts_of_speech == 1:
        print(f"It's so nice outside today it make we want to {word} !")
    elif parts_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word} !")
    else:
        print('Part of speech must be 0,1, or 2! can"t make a sentence:)')

def main():
    wordsssss = str(input('Enter a words !'))
    part = int(input('Enter a number!'))

    make_sentence(wordsssss,part)

if __name__ == "__main__":
    main()
    