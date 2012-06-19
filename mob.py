class Mob(object):		
	#set up a mobs stats
	def __init__(self, name, maxHP, HP, DP):
		self.mobname = name
		self.mobmaxHP = maxHP
		self.mobHP = HP
##	in furture this will be calcalated from stats
		self.mobDP = DP
