import valuecheck

def humiliate():
	print("How hard is it follow instructions you dyslexic piece of crap?")
	choice = input("\n*Take offence*\n1. Yes.\n2. No\n")
	choice = valuecheck.value_check(choice)
	if choice == 1:
		print("\nGonna cry? Piss your pants, maybe?")
		choice = input("\n1. *Cry, piss your pants and quit.*\n2. Just put an end to this misery.\n")
		choice = valuecheck.value_check(choice)
		if choice == 1 or choice == 2:
			print("\nAs expected, sucker.")
			exit()
		else:
			print("\n╭∩╮ Frick you!")
			exit()
	elif choice == 2:
		print("\nPussy!")
		choice = input("\n1. *Run away to your momma.*\n2. Quit.\n")
		choice = valuecheck.value_check(choice)
		if choice == 1 or choice == 2:
			print("\nRun pussy, run.")
			exit()
		else:
			print("╭∩╮ Frick you!")
			exit()
	else:
		print("\nJust leave while you still have some self-respect, you dumb neanderthal.\n")
		choice = input("\n1. Quit.\n2. Q U I T.\n")
		choice = valuecheck.value_check(choice)
		if choice == 1 or choice == 2:
			exit()
		else:
			print("\n╭∩╮ Frick you!")
			exit()