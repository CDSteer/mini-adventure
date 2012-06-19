class Player(object):
	
	#set up a players stats
	def __init__(self, name, plrclass, power, maxHP, HP, DP):
		self.name = name
		self.plrclass = plrclass
		self.power = power
		self.maxHP = maxHP
		self.HP = HP
		self.DP = DP
	
	#get the name of the player
	def getplayername(self):
		return self.name
	
	#get the class of the player	
	def getplrclass(self):
		return self.plrclass
		
	#get the power of the player	
	def getplrpower(self):
		return self.power
	
	#gets the players max hp
	def getplayermaxHP(self):
		return self.maxHP
	
	#sets a new max hp for the player
	def setplayermaxHP(self, newmax):
		self.maxHP = newmax
	
	#gets the players hp
	def getplayerHP(self):
		return self.HP
	
	#sets a new hp for the player
	def setplayerHP(self, newhp):
		self.HP = newhp
	
	#gets the damge of the player
	def getplayerDP(self):
		return self.DP
	
	#sets the damge of the player
#	in furture this will be calcalated from stats
	def setplayerDP(self, newDP):
		self.DP = newDP
	
	def isalive(self, mob):
		if self.HP <= 0:
			print "Game Over the %s brutaly murdereds you!" % mob
			return False
		else:
			return True
