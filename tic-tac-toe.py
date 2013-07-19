class Board(object):
	def __init__(self):
		self.row_1 = [
		"1", "2", "3"]
		self.row_2 = [
		"4", "5", "6"]
		self.row_3 = [
		"7", "8", "9"]

	def check_row():
		pass

	def check_col():
		pass

	def check_diag():
		pass

	def check_win():
		if check_row == True:
			self.winner = True
			print "You win!"
			return
		elif check_col == True:
			self.winner = True
			print "You win!"
			return
		elif check_diag == True:
			self.winner = True
			print "You win!"
			return
		else:
			play()

class Player(object):
	def __init__(self):
		self.value = None
		self.winner = False

def set_value(player):
	player_1.value = player
	if player == "X":
		player_2.value = "O"
	elif player == "O":
		player_2.value = "X"
	else:
		print("That doesn't seem to be a valid option. Try again.")
	first_turn()

my_board = Board()

def rows():
	row1 = my_board.row_1
	row2 = my_board.row_2
	row3 = my_board.row_3
	print row1
	print row2
	print row3


def play():
	pass

def set_piece(board, space, player):
	if space in board.row_1:
		board.row_1[int(space)-1] = player
	elif space in board.row_2:
		board.row_2[int(space)-4] = player
	elif space in board.row_3:
		board.row_3[int(space)-7] = player
	else:
		print("That doesn't seem to be a valid space on the board. Try again.")
		start_game()
	print("Okay, your piece is on space %s" +"\n") %(space)
	computer_turn(board)


player_1 = Player()
player_2 = Player()

prompt = ">> "

def start_game():
	print("Let's play Tic Tac Toe!" + "\n" +  "Pick one: 'X' or 'O'?")
	play_val = raw_input(prompt)
	set_value(play_val)

def first_turn():
	print("Okay, here's the board:")
	rows()
	turn = 0
	print("Pick a number to place your first piece.")
	first_space = raw_input(prompt)
	set_piece(my_board, first_space, player_1.value)

def computer_turn(board):
	print("Ok, here's the board again.\n")
	rows()
	print("\n Now it's my turn.")

start_game()

# if __name__ == "__main__":
# 	main()


