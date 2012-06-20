class Player(object):
	"""set up a players stats"""
	def __init__(self, lvl, name, plr_class, power, HP, plr_att, plr_def, plr_endu):
		self.plr_lvl = lvl
		self.plr_name = name
		self.plr_class = plr_class
		self.plr_power = power
		self.plr_maxHP = HP
		self.plr_HP = HP
		self.plr_att = plr_att
		self.plr_def = plr_def
		self.plr_endu = plr_endu
		max_AP = self.plr_endu * 2
		self.plr_maxAP = max_AP
		self.plr_AP = max_AP
		self.poison = False
		self.rage = False
	
	"""check it the player is still alive retuen true for alive and false for dead"""
	def isalive(self, mob):
		if self.plr_HP <= 0:
			print "Game Over the %s brutaly murdereds you!" % mob
			return False
		else:
			return True
