while True:
    first_word = str(input("What is your first word"))
    second_word = str(input("What is your second word"))
    if len(first_word) == len(second_word):
        print("the words are the same length")
    if len(first_word) < len(second_word):
        print("the second word is bigger")
    if len(first_word) > len(second_word):
        print("the first word is bigger")
