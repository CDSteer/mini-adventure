class Mob(object):		
	"""set up a mobs stats"""
	def __init__(self, lvl, name, HP, mob_att, mob_def, mob_endu):
		self.mob_lvl = lvl
		self.mob_name = name
		self.mob_maxHP = HP
		self.mob_HP = HP
		self.mob_att = mob_att
		self.mob_def = mob_def
		self.mob_endu = mob_endu
		self.poison = False
		self.rage = False
	
	"""checks if the mob is still alive, retuens true for alive and false for dead"""
	def is_alive(self):
		if self.mob_HP <= 0:
			return False
		else:
			return True
