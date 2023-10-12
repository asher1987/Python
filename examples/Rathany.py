def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] +   '   |   ' +   board[0][1] +   ' |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] +   '   |   ' +   board[1][1] +   ' |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] +   '   |   ' +   board[2][1] +   ' |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    ok = False	
while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' 
		if not ok:
			print("Bad move - repeat your input!") 
			continue
		move = int(move) - 1 	
		row = move // 3 	
		col = move % 3		
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	
			print("Field already occupied - repeat your input!")
			continue
board[row][col] = 'O' 	

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []	
for row in range(3): 
		for col in range(3): 
			if board[row][col] not in ['O','X']: 
				free.append((row,col)) 
return free



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
        if sign == "X":	
	            who = 'COMPUTER'
        elif sign == "O":
                who = 'PLAYER'
        else:
		        who = None
for rc in range(3):
    if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
        return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
            if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
                return who
                if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
                    return who
                    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    	free = make_list_of_free_fields(board)
        cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
    free = make_list_of_free_fields(board)
    human_turn = True 


while len(free):
	display_board(board)
	if human_turn:
		player_move(board)
		victor = victory_for(board,'O')
	else:	
		computer_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'COMPUTER':
	print("COMPUTER!")
elif victor == 'PLAYER':
	print("PLAYER WON")
else:
	print("TIE!")