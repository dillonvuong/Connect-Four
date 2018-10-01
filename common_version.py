#Molly Taing 82155694 and Dillon Vuong 82352779 Lab 5 
import connectfour

def welcome() -> None:
    'prints out the welcome statement'
    print()
    print("""Welcome to the Connect Four game!
    There are two commands: drop and pop.
    
    EXAMPLE: type d2 to drop in column 2 or type p3 to pop in column 3
    
    Refer to the Connect Four Wikipedia for further rules.""")
    print()

def board(game_state: connectfour.GameState) -> '2D table':
    'returns a 2d list of numbers representing the board'
    counter = 0
    r = []
    
    for row in range(connectfour.BOARD_ROWS): 
        c = [] 
        for col in game_state.board:
            c.append(col[counter])
        r.append(c)
        counter += 1
    return r

def print_board(board: '2D table') -> None:
    'print board in matrix form  with R for 1, Y for 2, and . for 0'
    print()
    numbers = ''
    for x in range(connectfour.BOARD_COLUMNS):
        numbers = numbers + str(x+1) + '  '
    print(numbers)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                space = '.'
            elif board[row][col] == 1:
                space = 'R'
            else:
                space = 'Y'
            print(space, end='')
        print()
    return

def turn(x:int) -> str:
    "returns whether it is red's turn or yellow's turn"
    if x % 2 == 1:
        print("Red's Turn: ")
    else:
        print("Yellow's Turn: ")

def winner(n: int) -> None:
    'prints out the winner'
    if n == 1:
        print()
        print('Red Wins!')
    elif n == 2:
        print()
        print('Yellow Wins!')
    else:
        print()
        print('Tie!')

def not_full(board: '2D table') -> bool:
    """returns False if board is full and True if it is not full
       used to determine the rare case of a tie"""
    a = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            a.append(board[row][col])
    if 0 in a:
        return True
    else:
        return False



