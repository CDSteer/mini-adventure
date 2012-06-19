class Player(object):
	#set up a players stats
##	add level, defence level, endurence
	def __init__(self, name, plrclass, power, maxHP, HP, DP):
		self.plrlvl = 1
		self.plrname = name
		self.plrclass = plrclass
		self.plrpower = power
		self.plrmaxHP = maxHP
		self.plrHP = HP
##	in furture this will be calcalated from stats
		self.plrDP = DP
	
	def isalive(self, mob):
		if self.plrHP <= 0:
			print "Game Over the %s brutaly murdereds you!" % mob
			return False
		else:
			return True
