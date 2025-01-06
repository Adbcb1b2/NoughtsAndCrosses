""" A Noughts and Crosses Game

This script allows the user to play a game of noughts and crosses, against the computer,
within the Python console. The user can also save their current score to a leaderboard
and load and display the leadboard.

This script accepts a text file (leaderboard.txt). For the script to be fully functional,
data within the text file must contain JSON data only. They key-value pairs should be
Name:Score.

This file can be imported as a module and contains the following functions:
    * draw_board - prints a 3x3 grid using ASCII symbols
    * welcome - displays message welcoming user and the grid
    * initialise_board - sets all grid spaces to blank
    * get_player_move - gets a user's choice of square in the grid
    * choose_computer_move - AI used to determine a computer move
    * check_for_win - checks if a certain player has won the game
    * check_for_draw - checks if the board shows a draw for a certain player
    * play_game - plays the game
    * menu - displays menu, gets user's menu choice
    * load_scores - loads scores from a text file
    * save_score - saves user's current score to the text file
    * display_leaderboard - displays a list of previous users scores
"""

import random
import json
import time


# Coursework Assessment 2
# Name: Kim Richards
# Student No: 2111532

def draw_board(board):
    """
    Prints a 3x3 grid, with each square containing an element from a list.

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        None
    """
    # Draws a 3x3 grid from a list of 3 lists, each with 3 elements.
    for row in range(0,3):
        print('-' * 13)
        output = '| '
        for col in range(0,3):
            output = output + board[row][col] + ' | '
        print(output)
    print('-'*13)

def welcome(board):
    """
    Displays a welcome message to the user, calls the draw_board function to display board

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        None
    """
    print('Welcome to the Noughts and Crosses game')
    print('The layout is shown below:')
    # Board displays to user.
    draw_board(board)


def initialise_board(board):
    """
     Returns an empty board

     Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        board(list): 2D list of 3 lists, each with 3 elements all with the value ' '
    """
    print('*** Initialising board ***')
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    return board

def get_player_move(board):
    """
    Returns row and column user has selected to place their 'X'

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        row(int): row user has selected (0-2)
        col(int): column user has selected (0-2)
    """
    while True:
        print("{:>27}".format('1 2 3'))
        print("{:>27}".format('4 5 6'))
        cell = input("{:>29}".format('Please choose a cell  7 8 9 : \n',))
        # Get digit 1-9 from user, if not 1-9 keep asking.
        if cell.isdigit():
            cell = int(cell)
            if cell  >=  1 and cell <=  9:
                # Convert cell number to row/column.
                row = (cell - 1) // 3
                col = (cell - 1) % 3
                # Check if cell is empty, if not ask for another cell.
                if board[row][col] == ' ':
                    break
                else:
                    print('Error: Space occupied.')
            else:
                print('Error: Digit entered is out of range')
        else:
            print('Error: Integers 1-9 accepted only')

    return row, col

def choose_computer_move(board):
    """
    Returns row and column for computer to place 'O'

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        row(int): row computer has selected (0-2)
        col(int): column computer has selected (0-2)
    """
    empty_coordinates = []
    print('The computer is having its turn.....')
    time.sleep(0.7)
    # Adds coordinates of empty squares to a list.
    row = 0
    for board_row in board:
        col = 0
        for element in board_row:
            if element == ' ':
                coordinates = (row, col)
                empty_coordinates.append(coordinates)
            else:
                pass
            col += 1
        row += 1
    # Iterate through list of empty coordinates to see if any are a winning move
    for coordinate in empty_coordinates:
        # Assigns row/column coordinates to variables.
        row = coordinate[0]
        col = coordinate[1]
        # Put nought in empty space, check if a winning move for noughts
        board[row][col] = 'O'
        win_o = check_for_win(board, 'O')
        # If not a winning move, set cell back to empty space
        if win_o is False:
            board[row][col] = ' '
        # If a winning move, leave nought in current empty space and break
        elif win_o is True:
            break
    # If no winning move for noughts, check to see if empty space would block crosses winning.
    if win_o is False:
        for coordinate in empty_coordinates:
            # Assigns row/column coordinates to variables.
            row = coordinate[0]
            col = coordinate[1]
            # Put cross in empty space, check if a winning move for crosses
            board[row][col] = 'X'
            win_x = check_for_win(board, 'X')
            # If a winning move for crosses, return row and col to block win.
            # Nought will replace cross when row, col is returned.
            print('x', win_x)
            if win_x is True:
                break
            # If empty square does not result in a block, reset to ' '.
            elif win_x is False:
                board[row][col] = ' '
    # If a win or block cannot be made, choose random space.
    elif win_o is False and win_x is False:
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if board[row][col] == ' ':
                break
    return row, col


def check_for_win(board, mark):
    """
    Returns True/False depending on if board shows a win for 'X' or 'O'

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '
        mark(str): 'X' or 'O' depending on if you are checking for a X or O win

    Returns:
        win(Boolean): True(win)/False(no win) depending on whether board shows a win.
    """
    win = False
    # Checking for diagonal wins.
    if board[0][0] == board[1][1] == board[2][2] == mark:
        win = True
    elif board [0][2] == board[1][1] == board[2][0] == mark:
        win = True
    # Checking for horizontal/vertical wins
    for i in range(len(board)):
        # Horizontal wins.
        if board[i][0] == board[i][1] == board[i][2] == mark:
            win = True
        # Vertical wins.
        elif board[0][i] == board[1][i] == board[2][i] == mark:
            win = True

    return win


def check_for_draw(board):
    """
    Returns True if there are no empty spaces in the board

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        draw(Boolean): True/False depending on whether board shows a draw.
    """
    draw = True
    # Check each square in the board
    for row in range(0,3):
        for col in range (0,3):
            # If an empty space remains, draw is false
            if board[row][col] == ' ':
                draw = False
    return draw

def play_game(board):
    """
    Returns the user's score having played a complete game of noughts and crossses

    Arguments:
        board(list): 2D list of 3 lists, each with 3 string elements - 'X', 'O' or ' '

    Returns:
        score(int): user's score after a completed game - win(1), draw(0), lose(-1)
    """
    # Welcome user and set board spaces to blank, display board.
    welcome(board)
    board = initialise_board(board)
    draw_board(board)

    # Code runs until a win or draw happens.
    while True:
        # Get player move, assign a cross to square of user's choice and display board.
        row, column = get_player_move(board)
        board[row][column] = 'X'
        draw_board(board)
        # Check if the current board state includes a win for crosses.
        win = check_for_win(board,'X')
        if win is True:
            print("You win!!")
            score = 1
            break
        # Check if the current board state shows a draw.
        draw = check_for_draw(board)
        if draw is True:
            print("It's a draw!")
            score = 0
            break
        # Computer to play it's move and display board.
        row, column = choose_computer_move(board)
        board[row][column] = 'O'
        draw_board(board)
        # Check if the current board state includes a win for noughts.
        win = check_for_win(board, 'O')
        if win is True:
            print("You lose! The computer wins")
            score = -1
            break
        # Check for draw
        draw = check_for_draw(board)
        if draw is True:
            score = 0
            break
    return score

def menu():
    """
    Displays a menu and returns user's choice

    Arguments:
        None

    Returns:
        choice(str): User's menu choice (1, 2, 3 or q)
    """
    choice = ''

    print('Please choose from the following options:')
    print(' 1 - Play the game')
    print(' 2 - Save score in a file "leaderboard.txt"')
    print(' 3 - Load and display the scores from the "leaderboard.txt"')
    print(' q - End the program')
    # Loop until user chooses a valid menu option.
    while choice not in ('1','2','3', 'q'):
        choice = input('Enter option: ')
        if choice not in ('1','2','3', 'q'):
            print('Invalid. Please try again.')
    return choice

def load_scores():
    """
    Returns scores read from JSON data in leaders.txt as a dictionary

    Arguments:
        None

    Returns:
        leaders(dict): Names and associated scores
    """
    # Exception handling - prevent program crashing if data in txt file is not JSON.
    try:
        # Opens file for reading.
        leaderboard_file = open("leaderboard.txt", 'r', encoding ='utf-8')
        leaders = leaderboard_file.read()

        # Converts contents of file into a dictionary.
        leaders = json.loads(leaders)
        # Sort leaderboard into decending order.
        sorted_leaders = sorted(leaders.items(), key = lambda x:x[1], reverse = True)
        leaders = dict(sorted_leaders)

    except json.decoder.JSONDecodeError:
        print('\nError: Data in the leaderboard text file is in the wrong format.\n')
    return leaders

def save_score(score):
    """
    Saves user's current score to the text file leaders.txt

    Arguments:
        score(int): user's total score

    Returns:
        None
    """
    # Exception handling to prevent program crashing if data in text file is not JSON.
    try:
        name = (input("Please enter your name: ")).capitalize()
        # Gets leaderboard dictionary.
        leaders = load_scores()
        # Updates/replaces leaderboard dictionary with name and score.
        leaders.update({name: score})

        # Converts dictionary into JSON format, avoiding double/single quote errors.
        data = json.dumps(leaders)

        # Opens file and overwrites new leaderboard
        leaderboard_file = open("leaderboard.txt", 'w',  encoding ='utf-8')
        leaderboard_file.write(data)
        print('\nYour score has been saved!\n')
    except AttributeError:
        print('\nError - Score not saved: leaderboard text file is in the wrong format.\n')


def display_leaderboard(leaders):
    """
    Displays scores from a dictionary in a table format

    Arguments:
        leaders(dict): names with associated scores

    Returns:
        None
    """
    # Exception handling - prevent program crashing if data in txt file is not JSON.
    try:
        # Prints table headers.
        print("{:<20} {:<20}".format('NAME', 'SCORE'))

        # Prints each key-value pair from dictionary, left aligned width 20.
        for value in leaders.items():
            name, score = value
            print("{:<20} {:<20}".format(name, score))
    except AttributeError:
        print('\nError: Unable to display data. \n')
