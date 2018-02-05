"""
Programmer: Daniel Mullen
DLM: April 4th 2017
This code simulates the Monty Hall Problem and calculates 
the probability of winning if you switch or keep your original pick.
It simulates a game for three curtains and for n curtains
"""

import random

# function for the game with three curtains
def three_curtains(switch):
	curtains = [0, 1, 2] # creates the curtains
	prize = random.randrange(3) # picks which one will have the prize
	curtains[prize] = "prize"  # replaces the integer with word prize
	goats = list(range(3))  # creates a list of goats
	del goats[prize]  # deletes the integer where prize is
	for i in goats:
		curtains[i] = "goat"  # puts a goat behind the curtain of the integers left
	pick = random.randrange(3) # persons choice
	if switch == True: 
		if curtains[pick] == 'goat': # if they picked goat switch to prize
			return "prize"
		else:
			return "goat"
	elif switch == False:
		if curtains[pick] == 'goat': # if they picked goat they keep on goat
			return "goat"
		else:
			return "prize"

# function for the game with n curtains
def n_curtains(n, switch):
	curtains = list(range(n)) # creates n curtains
	prize = random.randrange(n) # picks which curtains out of n curtains will have the prize
	curtains[prize] = "prize"  # replaces the integer with word prize
	goats = list(range(n))  # creates a list of goats in range n
	del goats[prize]  # deletes the integer where prize is
	for i in goats:
		curtains[i] = "goat"  # puts a goat behind the curtain of the integers left 
	pick = random.randrange(n) # persons choice in range of n 
	if switch == True: 
		if curtains[pick] == 'goat': 
			return "prize"
		else:
			return "goat"
	elif switch == False:
		if curtains[pick] == 'goat':
			return "goat"
		else:
			return "prize"



#-Game Simulator for a Game With 3 Curtains-#

trials = 1000    # amount of times to run through 
n_goats = 0  # accumulator 
n_prizes = 0 # accumulator
border = " " * 4 + "-" * 36 # creates a dash border

print("The Outcomes For a Game With 3 Curtains and", trials, "Trials:")

# Simulating a Switch:
print(border)
for i in range(trials):
	if (three_curtains(True)) == 'goat':
		n_goats += 1
	else:
		n_prizes += 1
print("\tIf You Switch:" + " " * 22 + "|") 
print("\tGoats:", n_goats, " " * 25 + "|")
print("\tPrizes:", n_prizes, " " * 24 + "|")
print("\tWin Probability:", ((3 - 1) / 3), "|")
print(border)
 
n_goats = 0  # resetting the accumulator 
n_prizes = 0 # resetting the accumulator

# Simulating a Stubborn Non-Switcher
for i in range(trials): 
	if (three_curtains(False)) == 'goat':
		n_goats += 1
	else:
		n_prizes += 1
print("\tIf You Don't Switch:" + " " * 16 + "|")
print("\tGoats:", n_goats, " " * 25 + "|")
print("\tPrizes:", n_prizes, " " * 24 + "|")
print("\tWin Probability:", 1 / 3, "|")
print(border)


#-Game Simulator for a Game With N Curtains-#

trials = 100000 
n = 4 # number of courtains
n_goats = 0 
n_prizes = 0  

print("\nThe Outcomes For a Game With", n, "Curtains and", trials, "Trials:")

# Simulating a Switch
print(border)
for i in range(trials):
	if (n_curtains(n, True)) == 'goat':
		n_goats += 1
	else:
		n_prizes += 1
print("\tIf You Switch:") 
print("\tGoats:", n_goats)
print("\tPrizes:", n_prizes)
print("\tWin Probability:", (n - 1) / (n * (n - 2)))
print(border)

n_goats = 0  # resetting the accumulator
n_prizes = 0 # resetting the accumulator

# Simulating a Stubborn Non-Switcher
for i in range(trials): 
	if (n_curtains(n, False)) == 'goat':
		n_goats += 1
	else:
		n_prizes += 1
print("\tIf You Don't Switch:")
print("\tGoats:", n_goats)
print("\tPrizes:", n_prizes)
print("\tWin Probability:", 1 / n)
print(border)

# (n − 1) / (n * (n−2))) is the probability of winning when switching 
# 1 / n is the probability of winning without switching