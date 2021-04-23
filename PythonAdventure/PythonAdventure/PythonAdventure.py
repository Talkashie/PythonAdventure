#Written by Talkashie

# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep

exit=0
location=0
userinput=""

#Stats
maxhp=25
hp=25
gp=0
power=5
defense=0
level=1
xp=0
maxxp=10

inventory=["HP Potion (Small)"]
shop1=["HP Potion (Small)", "Wood Shield", "Tin Shield"]

#------------------------------------------------
#DRAW FUNCTIONS
#------------------------------------------------
def drawStats():
	#This function shows basic stats
	print("HP: " + str(hp) + "/" + str(maxhp))
	print("GP: " + str(gp))

def draw():
	#This function shows information about the player's
	#location and the commands available to them
	global location
	system('cls')
	#Main Menu
	if(location==0):
		print("Python Adventure!")
		print("Written by Talkashie")
		print("\n\n\nCOMMANDS: PLAY, EXIT")

	#Cabin
	if(location==1):
		print("Location: Your cabin")
		drawStats()
		print("\n\n\nCOMMANDS: INVENTORY, STATS, TOWN")

	#Town
	if(location==2):
		print("Location: Town")
		drawStats()
		print("\n\n\nCOMMANDS: INVENTORY, STATS, CABIN, SHOP")

	#TownShop
	if(location==3):
		print("Location: Town Shop")
		drawStats()
		drawShop()
		print("\n\n\nCOMMANDS: BUY, LEAVE")

def drawInventory():
	#This function displays the player's inventory
	system('cls')
	print("INVENTORY:\n\n")
	for i in range(len(inventory)):
		print(str(i) + ": " + inventory[i])
	print("")
	system('pause')

def drawShop():
	#This function displays the current shop
	global location
	print("\nSHOP WARES:\n\n")
	if(location==3):
		for i in range(len(shop1)):
			print(str(i) + ": " + shop1[i])


def drawFullStats():
	#This function displays the player's full stats
	system('cls')
	print("PLAYER STATS:\n\n")
	print("LEVEL: " + str(level))
	print("XP: " + str(xp) + "/" + str(maxxp))
	print("POWER: " + str(power))
	print("DEFENSE: " + str(defense))
	print("")
	system('pause')

#------------------------------------------------
#END DRAW FUNCTIONS
#------------------------------------------------


#------------------------------------------------
#GAME FUNCTIONS
#------------------------------------------------
def userInput():
	#Here we process user input depending upon the location
	myInput=input("\nCOMMAND: ")
	myInput=myInput.lower()
	global location
	global exit

	#Main Menu
	if(location==0):
		if(myInput=="exit"):
			exit=1
		elif(myInput=="play"):
			location=1

	#Cabin
	if(location==1):
		if(myInput=="inventory"):
			drawInventory()
		elif(myInput=="stats"):
			drawFullStats()
		elif(myInput=="town"):
			location=2

	#Town
	if(location==2):
		if(myInput=="inventory"):
			drawInventory()
		elif(myInput=="stats"):
			drawFullStats()
		elif(myInput=="cabin"):
			location=1
		elif(myInput=="shop"):
			location=3

	#TownShop
	if(location==3):
		if(myInput=="buy"):
			print("Not yet implemented!")
			system('pause')
		elif(myInput=="leave"):
			location=2

#------------------------------------------------
#END GAME FUNCTIONS
#------------------------------------------------


#------------------------------------------------
#MAIN GAME LOOP
#------------------------------------------------
while(exit==0):
	draw()
	userInput()
#------------------------------------------------
#END MAIN GAME LOOP
#------------------------------------------------
