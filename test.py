from random import choice


number_of_guesses = 8
def wordle(number_of_guesses):
    list_of_words = ["nurse", "Ramzi", "Guess"]
    hidden_word = choice(list_of_words)
    guessed_word = []
    for i in range(number_of_guesses):
        guessed_word = input("Please enter a guess: ")
        result = ""
        if guessed_word == hidden_word:
            print("Correct!")
            break
        for j in range(len(guessed_word)):
            if hidden_word[j] == guessed_word[j]:
                result = result + "!"
            elif guessed_word[j] in hidden_word:
                result = result + "0"
            else:
                result = result + "X"
    print(result, end="")
    # print("You guessed " + guessed_word)
    # if hidden_word == guessed_word:
    #     print("You are correct!")
    # else:
    #     print("Incorrect!")
    # print(guessed_word)
    # print(result)

wordle(1)