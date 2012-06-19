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
print "1. Warrior: Power = Rage"
print "2. Thief:   Power = Poison"
print "3. Mage:    Power = Fireball"

pclass = raw_input(">")

if pclass == "1":
	#make the player setting the name, hp, dp depending on the class
	player = Player(name, "Warrior", "Rage", 300, 300, 20)
elif pclass == "2":
	player = Player(name, "Thief", "Poison", 200, 200, 10)
elif pclass == "3":
	player = Player(name, "Mage", "Fireball", 100, 100, 10)

print "Welcome %s" % player.plrclass

def userattack():
	hp = mob.mobHP
	dam = player.plrDP
	newhp = hp - dam
	mob.mobHP = newhp
	print "You deal %r points of damage" % player.plrDP
	print "%s: %r/%r" % (mob.mobname, mob.mobHP, mob.mobmaxHP)
	return

def mobattack():
	hp = player.plrHP
	dam = mob.mobDP
	newhp = hp - dam
	player.plrHP = newhp
	print "%s deals %r points of damage" % (mob.mobname, mob.mobDP)
	print "%s: %r/%r" % (player.plrname, player.plrHP, player.plrmaxHP)
	return
	
def battle():

	while mob.mobHP > 0:
		if player.isalive(mob.mobname) == False:
			sys.exit()
		print "How will you attack?"
		print "1. Bassic Attack"
		print "2. %s" % player.plrpower
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

mob = Mob("Large Rat", 60, 60, 30)
print "You enter the dark cave then a large %s goes to attack you" % mob.mobname
win = False
while win == False:	
	win = battle()
print "You beat the rat and won the tresure"
