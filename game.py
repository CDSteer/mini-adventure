import sys
import player
from player import * 
import mob
from mob import * 

print "Welcome Player, start by entering your name:"
name = raw_input(">")
print "Hello there %s, \nYou are about to enter a cave of no return." % name
print "Once inside the only way back a mistic portal at the end." 
print "So why take this risk? Because within this cave lies the worlds" 
print "largest collection of tresuse hiden away by a long dead king and" 
print "protected by evil monsters, so good luck :D"

print "Choose you class:"
print "1. Warrior: Power = Furry"
print "2. Thief: Power = Poison"
print "3. Mage: Power = Fireball"

pclass = raw_input(">")

if pclass == "1":
	#make the player setting the name, hp, dp depending on the class
	player = Player(name, "Warrior", "Furry", 300, 300, 10)
elif pclass == "2":
	pclass = "thief"
	classpower = "poison"
	playerhp = Player(200)
elif pclass == "3":
	pclass = "mage"
	classpower = "fireball"
	playerhp = Player(150)

print "Welcome %s" % pclass

def userattack():
	hp = mob.getmobHP()
	dam = player.getplayerDP()
	newhp = hp - dam
	mob.setmobHP(newhp)
	print "You deal %r points of damage" % player.getplayerDP()
	print "%s: %r/%r" % (mob.getmobname(), mob.getmobHP(), mob.getmobmaxHP())
	return

def mobattack():
	hp = player.getplayerHP()
	dam = mob.getmobDP()
	newhp = hp - dam
	player.setplayerHP(newhp)
	print "%s deals %r points of damage" % (mob.getmobname(), mob.getmobDP())
	print "%s: %r/%r" % (player.getplayername(), player.getplayerHP(), player.getplayermaxHP())
	return
	
def battle():

	while mob.getmobHP() > 0:
		if player.isalive(mob.getmobname()) == False:
			sys.exit()
		print "How will you attack?"
		print "1. Bassic Attack"
		print "2. %s" % player.getplrpower()
		print "3. Item"
		print "4. Quit"

		aplayer = raw_input(">")
		
		if aplayer == "1":
			mobattack()
			userattack()
		elif aplayer == "2":
			print "Coming Soon"
		elif aplayer == "3":
			print "Coming Soon"
		elif aplayer == "4":
			print "You coward!!!"
			sys.exit()
	return True

mob = Mob("Large Rat", 60, 60, 40)
print "You enter the dark cave then a large %s goes to attack you" % mob.getmobname()
win = False
while win == False:	
	win = battle()
print "You beat the rat and won the tresure"
