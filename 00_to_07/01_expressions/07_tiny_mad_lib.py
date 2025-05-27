
SENTENCE_TEMPLATE = "The {adjective} {noun} decided to {verb} in the middle of the street!"

adjective = input('Enter an adjective e.g (funny , big , small): ')
noun = input('Enter a noun e.g (dog , cat , car): ')
verb = input('Enter a verb e.g (run , jump , fly): ')

fun_sentence = SENTENCE_TEMPLATE.format(adjective=adjective, noun=noun,verb=verb)

print("\nHere's your fun sentence:" )
print(fun_sentence)
