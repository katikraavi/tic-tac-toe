class Player:
	is_player_winner = False

	def __init__(self, mark, winner, replacing_coord, nr_of_wins):
		self.mark = mark
		self.winner = winner
		self.replacing_coord = replacing_coord
		self.nr_of_wins = nr_of_wins
