class Board:
	spaces = []
	def __init__(self):

		for i in range(0,10):
			self.spaces.append(' ')

	def place_board(self, space, player):
		self.spaces[space] = player

	def print_board(self):

		print(self.spaces[0]+'|'+self.spaces[1]+'|'+ self.spaces[2])
		print('-----')
		print(self.spaces[3]+'|'+self.spaces[4]+'|'+ self.spaces[5])
		print('-----')
		print(self.spaces[6]+'|'+self.spaces[7]+'|'+ self.spaces[8])

	def clear_board(self):

		for i in range(len(self.spaces)):
			self.spaces[0]=' '
			self.spaces[1]=' '
			self.spaces[3]=' '
			self.spaces[4]=' '
			self.spaces[5]=' '
			self.spaces[6]=' '
			self.spaces[7]=' '
			self.spaces[8]=' '

	def check_win(self, player):

		if(self.spaces[0] == self.spaces[1] == self.spaces[2]=='X'):
			return True
		elif(self.spaces[3] == self.spaces[4] == self.spaces[5] == 'X'):
			return True
		elif(self.spaces[6] == self.spaces[7] == self.spaces[8] == 'X'):
			return True
		elif(self.spaces[0] == self.spaces[3] == self.spaces[6] == 'X'):
			return True
		elif(self.spaces[1] == self.spaces[4] == self.spaces[7] == 'X'):
			return True
		elif(self.spaces[2] == self.spaces[5] == self.spaces[8] == 'X'):
			return True
		elif(self.spaces[0] == self.spaces[4] == self.spaces[8] == 'X'):
			return True
		elif(self.spaces[2] == self.spaces[4] == self.spaces[6] == 'X'):
			return True
		elif(self.spaces[0] == self.spaces[1] == self.spaces[2]=='O'):
			return True
		elif(self.spaces[3] == self.spaces[4] == self.spaces[5] == 'O'):
			return True
		elif(self.spaces[6] == self.spaces[7] == self.spaces[8] == 'O'):
			return True
		elif(self.spaces[0] == self.spaces[3] == self.spaces[6] == 'O'):
			return True
		elif(self.spaces[1] == self.spaces[4] == self.spaces[7] == 'O'):
			return True
		elif(self.spaces[2] == self.spaces[5] == self.spaces[8] == 'O'):
			return True
		elif(self.spaces[0] == self.spaces[4] == self.spaces[8] == 'O'):
			return True
		elif(self.spaces[2] == self.spaces[4] == self.spaces[6] == 'O'):
			return True

		else:
			return False

class Player:
	def __init__(self,name):

		self.name = name
		self.moves = []

	def move(self, space):
		self.moves.append(space)


class Game:
	playerX = Player('X')
	playerO = Player('O')
	board = Board()

	def __init__(self):

		self.won = False

		self.turn = 0

	

	def take_turn(self):

		self.turn += 1

		move = input('Player X move: ')

		if self.board.spaces[move] != 'X' and self.board.spaces[move] !='O':
			self.playerX.move(move)
			self.board.place_board(move, self.playerX.name)
			self.board.print_board()
			if self.board.check_win(self.playerX.name)==True:
				self.won = True
				print('The winning player is PlayerX!')

		if self.won != True:

			move = input('Player O move: ')

			if self.board.spaces[move] != 'X' and self.board.spaces[move] !='O':
				self.playerO.move(move)
				self.board.place_board(move, self.playerO.name)
				self.board.print_board()
				if self.board.check_win(self.playerO.name)==True:
					self.won = True
					print('The winning player is PlayerO!')


def run_game():
	new_game = Game()
	new_game.board.print_board()
	while(new_game.won!= True and new_game.board.spaces.count(' ')!=0):
		new_game.take_turn()
	if new_game.board.spaces.count(' ') == 0:
		print("It's a tie!")

	play_again = raw_input('Do you want to play again [Y/N]: ')

	if play_again =='Y' or play_again == 'y':
		new_game.board.clear_board()
		run_game()
	
	else:
		print('Thanks for playing Tic Tac Toe. Bye Now!')







		

