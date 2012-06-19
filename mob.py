class Mob(object):		
	#set up a mobs stats
	def __init__(self, lvl, name, maxHP, HP, DP):
		self.mob_lvl = lvl
		self.mob_name = name
		self.mob_maxHP = maxHP
		self.mob_HP = HP
##	in furture this will be calcalated from stats
		self.mob_DP = DP
