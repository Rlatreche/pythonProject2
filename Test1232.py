
hidden_word = "Nurse"
guessed_word = ""

while True:
    try:
        guessed_word = input("Please enter a guess: ")

        result = ""
        if hidden_word[0] == guessed_word:
            result = result + "1"
        elif guessed_word in hidden_word:
            result = result + "0"
        else:
            result = result + "X"
        if hidden_word[1] == guessed_word:
            result = result + "1"
        elif guessed_word in hidden_word:
            result = result + "0"
        else:
            result = result + "X"
        if hidden_word[2] == guessed_word:
            result = result + "1"
        elif guessed_word in hidden_word:
            result = result + "0"
        else:
            result = result + "X"
        if hidden_word[3] == guessed_word:
            result = result + "1"
        elif guessed_word in hidden_word:
            result = result + "0"
        else:
            result = result + "X"
        if hidden_word[4] == guessed_word:
            result = result + "1"
        elif guessed_word in hidden_word:
            result = result + "0"
        else:
            result = result + "X"