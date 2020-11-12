import valuecheck
import playagain


def game(player1, player2):
	grid = [[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "],]
	valid_moves = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
	print("\nGrid (for reference):\n  1  |  2  |  3\n-----------------\n  4  |  5  |  6\n-----------------\n  7  |  8  |  9\n")

	while True:
		
		while True:
			x_input = input("\n{}'s turn. Enter the grid number where you want to place X: ".format(player1))
			x_input = valuecheck.value_check(x_input)
			if x_input in valid_moves:
				print("\n{} has marked grid number {}.".format(player1, x_input))
				valid_moves.remove(x_input)
				if 0 < x_input < 4:
					grid[0][x_input-1] = "X"
					break
				elif 3 < x_input < 7:
					grid[1][x_input-4] = "X"
					break
				else:
					grid[2][x_input-7] = "X"
					break
			else:
				print("\nEnter valid grid number, you idiot.")

		print("\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}".format(grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2],))

		if grid[0] == ["X", "X", "X"] or grid[1] == ["X", "X", "X"] or grid[2] == ["X", "X", "X"] or (grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X") or (grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X") or (grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X"):
			print("\n{} wins the game.".format(player1))
			playagain.twoplayer(player1, player2)
		elif len(valid_moves) == 0:
			print("\nThe games is a draw.\n")
			playagain.twoplayer(player1, player2)
	
		

		while True:
			y_input = input("\n{}'s turn. Enter the grid number where you want to place O: ".format(player2))
			y_input = valuecheck.value_check(y_input)
			if y_input in valid_moves:
				print("\n{} has marked grid number {}.".format(player2, y_input))
				valid_moves.remove(y_input)
				if 0 < y_input < 4:
					grid[0][y_input-1] = "O"
					break
				elif 3 < y_input < 7:
					grid[1][y_input-4] = "O"
					break
				else:
					grid[2][y_input-7] = "O"
					break
			else:
				print("\nEnter valid grid number, you idiot.")

		print("\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}".format(grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2],))


		if grid[0] == ["O", "O", "O"] or grid[1] == ["O", "O", "O"] or grid[2] == ["O", "O", "O"] or (grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O") or (grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O") or (grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
			print("\n{} wins the game.".format(player2))
			playagain.twoplayer(player1, player2)
		elif len(valid_moves) == 0:
			print("\nThe game is a draw.\n")
			playagain.twoplayer(player1, player2)