import random
import valuecheck
import playagain

def game():
	grid = [[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "],]
	valid_moves = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
	print("\nGrid Numbers (for reference):\n  1  |  2  |  3\n-----------------\n  4  |  5  |  6\n-----------------\n  7  |  8  |  9\n")

	while True:
		while True:
			player_input = input("\nYour turn. Enter the grid number where you want to place X: ")
			player_input = valuecheck.value_check(player_input)
			if player_input in valid_moves:
				print("\nYou have marked grid number {}.".format(player_input))
				valid_moves.remove(player_input)
				if 0 < player_input < 4:
					grid[0][player_input-1] = "X"
					break
				elif 3 < player_input < 7:
					grid[1][player_input-4] = "X"
					break
				else:
					grid[2][player_input-7] = "X"
					break
			else:
				print("\nEnter valid grid number, you idiot.")
				

		print("\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}".format(grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2],))

		if grid[0] == ["X", "X", "X"] or grid[1] == ["X", "X", "X"] or grid[2] == ["X", "X", "X"] or (grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X") or (grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X") or (grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X"):
			print("\nYou win the game.")
			playagain.oneplayer()
		elif len(valid_moves) == 0:
			print("\nThe game is a draw.\n")
			playagain.oneplayer()
	
		
		while True:
			cpu_input = random.choice(valid_moves)
			valid_moves.remove(cpu_input)
			print("\nCPU has marked grid number {}.".format(cpu_input))
			if 0 < cpu_input < 4:
				grid[0][cpu_input-1] = "O"
				break
			elif 3 < cpu_input < 7:
				grid[1][cpu_input-4] = "O"
				break
			elif 6 < cpu_input < 10:
				grid[2][cpu_input-7] = "O"
				break
			else:
				print("\nPlease enter valid grid number.\n")

		print("\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}\n-----------------\n  {}  |  {}  |  {}".format(grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2],))


		if grid[0] == ["O", "O", "O"] or grid[1] == ["O", "O", "O"] or grid[2] == ["O", "O", "O"] or (grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O") or (grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O") or (grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
			print("\nCPU wins the game.")
			playagain.oneplayer()
		elif len(valid_moves) == 0:
			print("\nThe game is a draw.\n")
			playagain.oneplayer()