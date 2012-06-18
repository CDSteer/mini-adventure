import sys

print "Welcome Player, start by entering your name:"
plrname = raw_input(">")
print "Hello there %s, \nYou are about to enter a cave of no return." % plrname
print "Once inside the only way back a mistic portal at the end." 
print "So why take this risk? Because within this cave lies the worlds" 
print "largest collection of tresuse hiden away by a long dead king and" 
print "prtected by evil monsters, so good luck :D"

print "Choise you class:"
print "1. Warrier: Power = Furry"
print "2. Thief: Power = Poison"
print "3. Mage: Power = Fireball"

pclass = raw_input(">")

if pclass == "1":
	pclass = "warrier"
	classpower = "Furry"
elif pclass == "2":
	pclass = "thief"
	classpower = "poison"
elif pclass == "3":
	pclass = "mage"
	classpower = "fireball"

print "Welcome %s" % pclass

def lifecheck (playerhp):
	if (playerhp < 1):
		return "Game Over"
		sys.exit()
	else:
		return True

def userattack(mob, attack, hp):
	hpnew = hp - attack
	print "You deal %r points of damage" % attack
	print "%s: %r/%r" % (mob, hpnew, hp)
	return hpnew

def mobattack(mob, attack, plrname, playerhp):
	hpnew = playerhp - attack
	print "%s deals %r points of damage" % (mob, attack)
	print "%s: %r/%r" % (plrname, hpnew, playerhp)
	return hpnew
	
def battle(mob, hp, plrname, playerhp):
	
	while hp > 0:
		lifecheck(playerhp)
		print "How will you attack?"
		print "1. Bassic Attack"
		print "2. %s" % classpower
		print "3. Item"
		print "4. Quit"

		aplayer = raw_input(">")
		
		if aplayer == "1":
			hp = userattack(mob, 30, hp)
			playerhp = mobattack(mob, 40, plrname, playerhp)
		elif aplayer == "2":
			hp = ratbattle(60, hp, playerhp)
			playerhp = mobattack(mob, 40, plrname, playerhp)
		elif aplayer == "3":
			aplayer == "item"
		elif aplayer == "4":
			print "You coward!!!"
			sys.exit()
	return True
	
playerhp = 200
print "Enter the dark cave then a large rat goes to attack you"
win = False
while win == False:
	
	win = battle("Rat", 60, plrname, playerhp)
	
print "Your beat the rat a won the tresure"

