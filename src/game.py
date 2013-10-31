import sys
import player
from player import * 
import mob
from mob import * 
import powers
from powers import *
import battle
from battle import *

"""Game Starts here"""	

print "Welcome Player, start by entering your name:"
name = raw_input(">")
print "Hello there %s, \nYou are about to enter a cave of no return." % name
print "Once inside the only way back a mistic portal at the end." 
print "So why take this risk? Because within this cave lies the worlds" 
print "largest collection of tresuse hiden away by a long dead king and" 
print "protected by evil monsters."

class_options(name)

print "You enter the dark cave, Good Luck :D"

battle.start_battle()
win = False
while win == False:	
	win = battle.battle_options()
print "You continue on through the dark cave when....."
battle.start_battle()
win = False
while win == False:	
	win = battle.battle_options()
print "You continue on through the dark cave when....."
battle.start_battle()
win = False
while win == False:	
	win = battle.battle_options()
print "You continue on through the dark cave when....."
battle.start_battle()
win = False
while win == False:	
	win = battle.battle_options()
print "You continue on through the dark cave when....."
battle.start_battle()
win = False
while win == False:	
	win = battle.battle_options()
print "Won the tresure. Yay!"