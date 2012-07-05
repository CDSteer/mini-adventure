class Bag(object):
	def __init__(self):
		self.id_01 = 1
		self.id_02 = 0
		self.slot_one = 0
		self.slot_two = 0
		self.slot_three = 0
		self.slot_four = 0
	
	"""Functions for HP Potions"""
	def add_01(self):
			self.id_01 = self.id_01 + 1
			print "HP potion added!"
			return
		
		
	def use_01(self):
		if self.id_01 > 0:
			self.id_01 = self.id_01 - 1
			print "HP potion Used!"
			return 100
		else:
			print "You dont have any!"
			return False
			
	"""Functions for AP Potions"""	
	def add_02(self):
		self.id_02 = self.id_02 + 1
		print "AP potion added!"
		return
		
	def use_02(self):
		if self.id_02 > 0:
			self.id_02 = self.id_02 - 1
			print "HP potion Used!"
			return 100
		else:
			print "You dont have any!"
			return False
	
		
	
