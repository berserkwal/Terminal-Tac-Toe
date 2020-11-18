import namechange, vscpu, vs2player

def oneplayer():
	while True:
		choice = int(input("\nWanna play again?\n1. Yes.\n2. Yes, but vs Human opponent.\n3. No.\n"))

		if choice == 1:
			vscpu.game()
		elif choice == 2:
			ret = namechange.name_change()
			vs2player.game(ret[0], ret[1])
		elif choice == 3:
			print("\nHope you had fun. Come again another time.")
			exit()

def twoplayer(player1, player2):
	while True:
		choice = int(input("\nWanna play again?\n1. Yes.\n2. Yes, but with different names.\n3. Yes, but vs CPU. \n4. No\n"))

		if choice == 1:
			vs2player.game(player1, player2)
		elif choice == 2:
			ret = namechange.name_change()
			vs2player.game(ret[0], ret[1])
		elif choice == 3:
			vscpu.game()
		elif choice == 4:
			print("\nHope you had fun. Come again another time.")
			exit()