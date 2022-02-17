def guideBoard():
    print(" 1 | 2 | 3 ")
    print("---+--+---")
    print(" 4 | 5 | 6 ")
    print("---+--+---")
    print(" 7 | 8 | 9 ")


moves = ["", "", "", "", "", "", "", "", "", "", ""]


def board():
    print(" " + moves[1] + " | " + moves[2] + " | " + moves[3] + " ")
    print("---+--+---")
    print(" " + moves[4] + " | " + moves[5] + " | " + moves[6] + " ")
    print("---+--+---")
    print(" " + moves[7] + " | " + moves[8] + " | " + moves[9] + " ")
    # HORIZONTAL WINNER
    # moves[1], moves[2], moves[3]
    # moves[4], moves[5], moves[6]
    # moves[7], moves[8], moves[9]
    # VERTICAL WINNER
    # moves[1], moves[5], moves[8]
    # moves[3], moves[5], moves[7]
    #


def game():
    count = 0
    turn = "x" or 'O'

    print("This is the board you will play on.")
    guideBoard()
    for i in range(9):
        move = int(input("Where would you like to move " + turn + "?"))
        if moves[move] == "":
            moves[move] = turn
            board()
        else:
            print("You can't move there! Try again?")
            continue
        if turn == "x":
            turn = "O"
        else:
            turn = "x"
        if moves[1] == moves[2] == moves[3] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[4] == moves[5] == moves[6] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[7] == moves[8] == moves[9] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[1] == moves[5] == moves[9] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[3] == moves[5] == moves[7] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[1] == moves[4] == moves[7] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[2] == moves[5] == moves[8] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
        elif moves[3] == moves[6] == moves[9] != '':
            board()
            print("Congragulations! " + turn + " won!")
            break
    if turn == 10:
        print("There has been a tie! Game over!")


game()
