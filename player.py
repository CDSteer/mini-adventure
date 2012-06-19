class Player(object):
	#set up a players stats
##	add level, defence level, endurence
	def __init__(self, lvl, name, plr_class, power, max_HP, HP, DP):
		self.plr_lvl = lvl
		self.plr_name = name
		self.plr_class = plr_class
		self.plr_power = power
		self.plr_maxHP = max_HP
		self.plr_HP = HP
##	in furture this will be calcalated from stats
		self.plr_DP = DP
	
	def isalive(self, mob):
		if self.plr_HP <= 0:
			print "Game Over the %s brutaly murdereds you!" % mob
			return False
		else:
			return True
