from random import randint
Board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    print('-------')
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')
    print('-------')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('-------')
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print('-------')




def gametime():
    turn = 'X'
    count = 0
    print("do you want to play with player or computer?")
    player = input()
    if player == "player" or player == 'p':
        print("player vs player")
        for i in range(10):
            printBoard(Board)
            print("It's your turn:" + turn + " where do you want to move?")
            move = input()
            if Board[move] == ' ':
                Board[move] = turn
                count += 1
            else:
                print("That place is already taken, please make different move")
                continue
            if count >= 5:
                if Board['1'] == Board['2'] == Board['3'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['4'] == Board['5'] == Board['6'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['7'] == Board['8'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['1'] == Board['4'] == Board['7'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['2'] == Board['5'] == Board['8'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['3'] == Board['6'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['1'] == Board['4'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['3'] == Board['4'] == Board['7'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        if count == 9:
            print("draw")
    else:
        print("player vs computer")
        for i in range(10):
            if turn == 'X':
                printBoard(Board)
                move = input("It's your turn:" + turn + " where do you want to move?")
            else:
                move = str(randint(1, 9))
            if Board[move] == ' ':
                Board[move] = turn
                count += 1
            else:
                print("That place is already taken, please make different move")
                continue
            if count >= 5:
                if Board['1'] == Board['2'] == Board['3'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['4'] == Board['5'] == Board['6'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['7'] == Board['8'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['1'] == Board['4'] == Board['7'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['2'] == Board['5'] == Board['8'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['3'] == Board['6'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['1'] == Board['4'] == Board['9'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
                elif Board['3'] == Board['4'] == Board['7'] != ' ':
                    printBoard(Board)
                    print(turn + " you won")
                    break
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        if count == 9:
            print("draw")


if __name__ == '__main__':
    gametime()
