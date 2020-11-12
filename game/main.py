import valuecheck
import humiliation
import vs2player
import vscpu
import namechange



print("Welcome to Terminal-Tac-Toe.")
choice = input("\nEnter a number depending on your choice: \n1. Play\n2. Instruction \n3. Quit\n")
choice = valuecheck.value_check(choice)
if choice == 1:
	choice = input("\nWho do you want to be your opponent?\n1. Play vs CPU.\n2. Play vs Human.\n")
	choice = valuecheck.value_check(choice)
	if choice == 1:
		print("\nHave fun!\n")
		vscpu.game()
	elif choice == 2:
		ret = namechange.name_change()
		print("\nHave fun!\n")
		vs2player.game(ret[0], ret[1])
	else:
		humiliation.humiliate()

elif choice == 2:
	print("\nYou never played Tic-Tac-Toe? What a noob. Get outta here.\n\nUnless you want to know how this version plays.n\nIt's simple. Just enter the grid number (1-9) where you want to put your mark.")
	print("\nGrid Numbers:\n  1  |  2  |  3\n-----------------\n  4  |  5  |  6\n-----------------\n  7  |  8  |  9")
	choice = input("\nReady to play now?\n1. Yes\n2. Nah, maybe some other time.\n")
	choice = valuecheck.value_check(choice)
	if choice == 1:
		choice = input("\nWho do you want to be your opponent?\n1. Play vs CPU.\n2. Play vs Human.\n")
		choice = valuecheck.value_check(choice)
		if choice == 1:
			print("\nHave fun!\n")
			vscpu.game()
		elif choice == 2:
			ret = namechange.name_change()
			print("\nHave fun!\n")
			vs2player.game(ret[0], ret[1])
		else:
			humiliation.humiliate()
	elif choice == 2:
		print("\nWell, come anytime if you want to play.")
		exit()
	else:
		humiliation.humiliate()

elif choice == 3:
	print("\nIt's alright. Come back another time.")
	exit()

else:
	humiliation.humiliate()
	


