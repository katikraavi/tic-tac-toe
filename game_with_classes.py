import random
from game_classes import Player
# TODO: The correct formatting of stacking the imports is like this
from game_functions import (
	print_game,
	print_coordinate_hints,
	mark_to_board,
	current_symbol,
	check_the_winner,
	nr_criteria,
)

tic_tac_toe = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]  # 2d list

coordinates = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"],
]

player_1 = Player("X", False, None, 0)
player_2 = Player("O", False, None, 0)

print("====WELCOME TO TIC-TAC-TOE, Vlad ====")
print("")
print_game(tic_tac_toe)
print("")
print("------------------------------------")
print_coordinate_hints(coordinates)
print("")

game = True
winner = "No winner yet!"
continue_game = True
play_agen = "0"
print(f"You will play against computer, computer will be {player_2.mark}")
player_1.mark = input(f"Choose your mark: ")

while game:
	skip_second_player = False
	player_1.is_player_winner = False
	player_2.is_player_winner = False

	if play_agen == "1":
		print(f"your mark was {player_1.mark}")

		# TODO: No need for f'' string if you do not put any variable inside.
		print(f"you can chose the same mark or change it to something else:")

		# TODO: If I choose 0, the player_2 also will be 0 by default,
		#  and then there are no differences in players in the field.
		player_1.mark = input("print you mark: ")
	play_agen = "0"

	# Player X choice
	player_1.replacing_coord = input("Chose a coordinate: ")
	# condition = "correct"

	# check for a valid number between 1 and 9
	while nr_criteria(player_1.replacing_coord) != "nr is in range":
		# TODO: Do you expect all the players to always be an X,
		#  even if you allow them to choose their mark?
		player_1.replacing_coord = input(f"Place X in valid coordinate: ")

	# Print the symbol in chosen coordinate
	symbol_in_board = current_symbol(tic_tac_toe, coordinates, player_1.replacing_coord)
	while symbol_in_board == player_1.mark or symbol_in_board == player_2.mark:
		print(f"This place has been taken by: {symbol_in_board}")
		player_1.replacing_coord = input("Place X in unused coordinate: ")
		while nr_criteria(player_1.replacing_coord) != "nr is in range":
			# TODO: No need for f'' string if you do not put any variable inside.
			replace_coord_X = input(f"Place X in valid coordinate: ")
		symbol_in_board = current_symbol(tic_tac_toe, coordinates, player_1.replacing_coord)

	# Replace chosen coordinate to "X" in board game "tic_tac_toe", print new board:
	mark_to_board(player_1.mark, tic_tac_toe, coordinates, player_1.replacing_coord)
	print_game(tic_tac_toe)

	# Check for a winner and play agen
	winner = check_the_winner(tic_tac_toe, player_1.mark)
	if winner == "No winner yet":
		game = True
	if winner == player_1.mark:
		player_1.is_player_winner = True
		player_1.nr_of_wins = player_1.nr_of_wins + 1
		print(f"You won with a mark: {player_1.mark}")
		print("The score is now:")
		print(f"You ({player_1.mark}) -  {player_1.nr_of_wins}")
		print(f"Computer ({player_2.mark}) -  {player_2.nr_of_wins}")
		play_agen = input(f"Do you want to play agen? y/n: ")
		if play_agen == "y":
			tic_tac_toe = [
				[" ", " ", " "],
				[" ", " ", " "],
				[" ", " ", " "],
			]
			game = True
			skip_second_player = True
		else:
			game = False
			continue_game = False
			print("Bye!")

	# TODO: Better to evaluate not by the string "Everyone won, its a Tie"
	#  but by a separate variable that defines a tie, like tie = Boolean.
	if winner == "Everyone won, its a Tie":
		print(winner)
		player_1.nr_of_wins = player_1.nr_of_wins + 1
		player_2.nr_of_wins = player_2.nr_of_wins + 1

		# TODO: Next lines are duplicated from the if winner == player_1.mark.
		#  Better to make a reusable function and call it in both places.
		print("The score is now:")
		print(f"{player_1.mark} -  {player_1.nr_of_wins}")
		print(f"{player_2.mark} -  {player_2.nr_of_wins}")
		play_agen = input(f"Do you want to play agen? y/n")
		if play_agen == "y":
			tic_tac_toe = [
				[" ", " ", " "],
				[" ", " ", " "],
				[" ", " ", " "],
			]
			skip_second_player = True
			game = True
		else:
			game = False
			continue_game = False
			print("Bye!")

	# Computers choice
	if not skip_second_player:
		player_2.replacing_coord = str(random.randint(1, 9))
		symbol_in_board = current_symbol(tic_tac_toe, coordinates, player_2.replacing_coord)
		while symbol_in_board == player_1.mark or symbol_in_board == player_2.mark:
			player_2.replacing_coord = str(random.randint(1, 9))
			symbol_in_board = current_symbol(tic_tac_toe, coordinates, player_2.replacing_coord)
		mark_to_board(player_2.mark, tic_tac_toe, coordinates, player_2.replacing_coord)
		print(f"Computer chose :{player_2.replacing_coord}")
		print_game(tic_tac_toe)

		#  Check if computer wins
		winner = check_the_winner(tic_tac_toe, player_2.mark)
		if winner == player_2.mark:
			player_2.nr_of_wins = player_2.nr_of_wins + 1

			# TODO: Next lines are duplicated from the if winner == player_1.mark.
			#  Better to make a reusable function and call it in both places.
			print(f"the winner is {player_2.mark}")
			print("The score is now:")
			print(f"{player_1.mark} -  {player_1.nr_of_wins}")
			print(f"{player_2.mark} -  {player_2.nr_of_wins}")
			play_agen = input(f"Do you want to play agen? y/n: ")
			if play_agen == "y":
				tic_tac_toe = [
					[" ", " ", " "],
					[" ", " ", " "],
					[" ", " ", " "],
				]
				game = True
			else:
				game = False
				continue_game = False
				print("Bye!")
		if winner == "Everyone won, its a Tie":
			print(winner)
			player_1.nr_of_wins = player_1.nr_of_wins + 1
			player_2.nr_of_wins = player_2.nr_of_wins + 1

			# TODO: Next lines are duplicated from the if winner == player_1.mark.
			#  Better to make a reusable function and call it in both places.
			print("The score is now:")
			print(f"{player_1.mark} -  {player_1.nr_of_wins}")
			print(f"{player_2.mark} -  {player_2.nr_of_wins}")
			play_agen = input(f"Do you want to play agen? y/n")
			if play_agen == "y":
				tic_tac_toe = [
					[" ", " ", " "],
					[" ", " ", " "],
					[" ", " ", " "],
				]
				skip_second_player = True
				game = True
			else:
				game = False
				print("Bye!")

	#  Make a user to chose if continue playing
	print("+++++++++++++++++++++++++++++++++++")
	# if not continue_game:
	if play_agen == "y":
		# TODO: play_agen. Since it is a binary option (1 or 0) it is better to use boolean True or False.
		play_agen = "1"

		user_choice_continue_game = input("CONTINUE the game? y/n ")
		if user_choice_continue_game == "y":
			game = True
			print_coordinate_hints(coordinates)
		elif user_choice_continue_game == "n":
			game = False
			print("Bye!")

print("The end")
