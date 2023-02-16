import random

def getNewBoard(size):

    ''' This Python function, getNewBoard(size), takes an integer argument size and returns a 2D list representing a game board with size rows and size columns.

    Here's an explanation of how it works:

    1. The outermost square brackets define the list that will be returned by the function.
    2. The innermost square brackets define a list that will represent a single row of the game board.
    3. The expression ['-' for _ in range(size)] creates a list of size hyphens ('-') using a list comprehension. This is a shorthand way of writing a for loop that appends hyphens to the list size times. The use of the _ variable name indicates that we don't actually care about the loop variable - we just want to execute the loop size times.
    4. The outermost list comprehension [['-' for _ in range(size)] for _ in range(size)] creates a list of size rows, where each row is itself a list of size hyphens. This is done using a nested list comprehension, where the inner list comprehension creates a row of hyphens size times, and the outer list comprehension creates size rows using the inner list comprehension.

    Overall, the function returns a 2D list representing a game board with size rows and size columns, where each position is initially marked with a hyphen ('-').'''

    return [['-' for _ in range(size)] for _ in range(size)]

def printBoard(board):

    ''' This function takes a 2D list (a board) as input and prints it out in a nicely formatted way.

    The first line printed is the column numbers, with each number separated by a space.

    Then, for each row of the board, the function prints the row number, followed by the values in that row, separated by a space.

    The result is a grid-like representation of the board.'''

    print("  " + " ".join(str(i) for i in range(len(board))))
    for i in range(len(board)):
        row = "".join(str(board[i][j]) + " " for j in range(len(board)))
        print(str(i) + " " + row)

def getNextTile(playerName, symbol, size):

    ''' This is a Python function named "getNextTile" that takes three arguments: playerName (a string), symbol (a string), and size (an integer). It prompts the player with the given name to enter the coordinates for the next tile in the format "row1 col1 row2 col2", where row1 and col1 represent the coordinates of the first square and row2 and col2 represent the coordinates of the second square. It then checks the validity of the input by ensuring that it contains four integers, each within the range of the game board, and that the two squares are either vertically or horizontally adjacent. If the input is valid, the function returns the coordinates of the two squares as strings. If the input is not valid, the function prints an error message and prompts the player to enter new coordinates. The function runs in a loop until valid input is provided.'''

    while True:
        tile = input(f"{playerName}, enter the coordinates for the next tile (row1 col1 row2 col2): ")
        tile = tile.strip().split()
        if len(tile) != 4:
            print("Invalid input, please enter 4 coordinates")
            continue
        try:
            row1, col1, row2, col2 = [int(x) for x in tile]
        except ValueError:
            print("Invalid input, please enter integers only")
            continue
        if row1 < 0 or row1 >= size or col1 < 0 or col1 >= size or row2 < 0 or row2 >= size or col2 < 0 or col2 >= size:
            print("Invalid coordinates, please enter coordinates within the game board")
            continue
        if not validateTile(f"{row1}{col1}", f"{row2}{col2}", size):
            print("Squares are diagonal or squares are not connected vertically-horizontly")
            continue
        return f"{row1}{col1}", f"{row2}{col2}"

def validateTile(square1, square2, size):

    ''' This function is designed to validate if two squares on a square grid are adjacent or not. The function takes three arguments - the coordinates of the first square (square1), the coordinates of the second square (square2), and the size of the square grid (size).

    The first step in the function is to check if the two squares are the same or not. If they are the same, the function returns False, indicating that the squares are not adjacent.

    The next step is to convert the coordinates of both squares into their row and column values. This is done by splitting the input strings into two separate integers using a list comprehension.

    Then, the function checks if the two squares are adjacent or not. Two squares are considered adjacent if they are either in the same row and have a column difference of one or in the same column and have a row difference of one. The function uses the abs() function to calculate the absolute difference between the row and column values and returns True if this difference is equal to 1.

    If the squares are not adjacent, the function returns False.'''

    if square1 == square2:
        return False
    row1, col1 = [int(x) for x in square1]
    row2, col2 = [int(x) for x in square2]
    if (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1):
        return True
    return False

def placeTile(board, symbol, square1, square2):

    ''' This function is used to place a symbol (e.g. 'X' or 'O') on a game board, which is represented as a 2-dimensional array. The function takes four arguments: the board itself, the symbol to be placed, and the coordinates of two squares on the board where the symbol should be placed.

    The function first converts the coordinates from strings to integers using a list comprehension. It then checks if both of the squares are empty (i.e. contain the '-' character). If they are, the function updates the board by placing the symbol in both squares and returns True to indicate that the placement was successful. If either square is already occupied, the function returns False to indicate that the placement was invalid.'''

    row1, col1 = [int(x) for x in square1]
    row2, col2 = [int(x) for x in square2]
    if board[row1][col1] == '-' and board[row2][col2] == '-':
        board[row1][col1] = symbol
        board[row2][col2] = symbol
        return True
    return False

def isGameAlive(board):

    ''' This function, isGameAlive(), takes a 2D board as input and checks if the game is still alive. The game is considered alive if there are any empty spaces on the board that can be filled by a tile.

    The function loops through the board using two nested loops and checks if any position on the board is empty. If the position is empty, it checks the neighboring positions to see if they are also empty and can be filled by a tile. If a neighboring position is empty and can be filled by a tile (using the validateTile() function), the function returns True, indicating that the game is still alive.

    If the function has looped through the entire board and has not found any empty positions that can be filled by a tile, it returns False, indicating that the game is over.'''

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                if j+1 < len(board) and board[i][j+1] == '-' and validateTile(f"{i}{j}", f"{i}{j+1}", len(board)):
                    return True
                if i+1 < len(board) and board[i+1][j] == '-' and validateTile(f"{i}{j}", f"{i+1}{j}", len(board)):
                    return True
    return False

def playGame():

    ''' This function is a Python program for playing a tic-tac-toe game. It prompts the user to enter the names of two players, the size of the game board, and randomly selects the starting player. The program then proceeds to allow the players to take turns placing their respective symbols ("X" or "O") on the board until a winner is determined or the game is a tie. It prints the winner and the final score of the game.'''

    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    players = { "X": player1, "O": player2 }

    size = 0
    while size % 2 != 1 or size < 3:
        size = int(input("Enter the size of the game board (must be odd number and at least 3): "))
    board = getNewBoard(size)

    starting_player = "X" if random.randint(0, 1) == 0 else "O"
    print(f"{players[starting_player]} will start the game!")

    while isGameAlive(board):
        printBoard(board)
        symbol = starting_player
        starting_player = "X" if starting_player == "O" else "O"
        print(f"{players[symbol]}'s turn ({symbol})")
        valid = False
        while not valid:
            square1, square2 = getNextTile(players[symbol], symbol, size)
            valid = validateTile(square1, square2, size) and placeTile(board, symbol, square1, square2)
            if not valid:
                print("Invalid move! Please try again.")
        printBoard(board)
    winner, score = determineWinner(board, player1, player2)
    print(f"{winner} wins with a score of {score[winner]}!")
    print(f"{player1}: {score[player1]}")
    print(f"{player2}: {score[player2]}")


def determineWinner(board, player1, player2):

    ''' This function takes in a tic-tac-toe board, player1, and player2 as arguments. It counts the number of X's and O's on the board and determines the winner based on the player with more marks. If there is a tie, it prints a message and starts a new game by calling the playGame() function.

    If there is a winner, it returns the winner's name and a dictionary of scores for both players. The scores are stored in the score dictionary using player names as keys. Finally, the function prints the winner's name and their score, as well as the score for the other player.'''

    x_count = 0
    o_count = 0
    for row in board:
        for square in row:
            if square == "X":
                x_count += 1
            elif square == "O":
                o_count += 1
    if x_count > o_count:
        winner = player1
        score = {player1: x_count, player2: o_count}
    elif x_count < o_count:
        winner = player2
        score = {player1: x_count, player2: o_count}
    else:
        print("Tie game! Starting new game...")
        playGame()
        return

    print(f"{winner} wins with a score of {score[winner]}!")
    print(f"{player1}: {score[player1]}")
    print(f"{player2}: {score[player2]}")
    return winner, score



if __name__ == "__main__":
    
    playGame()