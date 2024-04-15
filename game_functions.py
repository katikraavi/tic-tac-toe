def print_game(board):
	print("Game table:")
	for row in board:
		print(row)


def print_coordinate_hints(hint_numbers):
	print("Coordinates hint: ")
	for coordinates_hint in hint_numbers:
		print(coordinates_hint)


def get_valid_coordinate(input_coordinate):
	while not input_coordinate.isdigit() or 1 < int(input_coordinate) > 10:
		input_coordinate(input("use a number as a coordinate: "))
		print(f"input coordinate is now {input_coordinate}")
		return input_coordinate


def number_is_digit(test_number):
	if test_number.isdigit():
		# TODO: .isdigit() returns Boolean, so no need to make a separate function.
		return "digit"


def find_coordinate_index(unused_coordinates, replacing_coordinate):
	for row_ in unused_coordinates:
		if replacing_coordinate in row_:
			return unused_coordinates.index(row_), row_.index(replacing_coordinate)


def nr_criteria(input_coordinate):
	# TODO: .isdigit returns True or False, so it is just enough to if input_coordinate.isdigit():
	if number_is_digit(input_coordinate) != "digit":
		return "not digit"
	if 10 < int(input_coordinate) < 1:
		return "NOT IN RANGE number"
	if 0 < int(input_coordinate) < 10 and number_is_digit(input_coordinate) == "digit":
		return "nr is in range"
	if number_is_digit(input_coordinate) == "digit":
		return "nr is digit, but not in range"


def current_symbol(board, unused_coordinates, replacing_coordinate):
	mark_index = find_coordinate_index(unused_coordinates, replacing_coordinate)
	mark_index0 = int(mark_index[0])
	mark_index1 = int(mark_index[1])
	return str(board[mark_index0][mark_index1])


def mark_to_board(mark, board, unused_coordinates, replacing_coordinate):
	mark_index = find_coordinate_index(unused_coordinates, replacing_coordinate)
	mark_index0 = int(mark_index[0])
	mark_index1 = int(mark_index[1])
	board[mark_index0][mark_index1] = mark
	return board


def check_the_winner(board, mark_input):
	if board[0][0] == board[1][1] == board[2][2] == mark_input:
		return mark_input
	if board[2][2] == board[1][1] == board[0][0] == mark_input:
		return mark_input
	for row in board:
		if row[0] == row[1] == row[2] == mark_input:
			return mark_input
	for column in range(3):
		if board[0][column] == board[1][column] == board[2][column] == mark_input:
			return mark_input
	for row in board:
		for number in row:
			if number == " ":
				return "No winner yet"
	for row in board:
		for number in row:
			if number != " ":
				return "Everyone won, its a Tie"
