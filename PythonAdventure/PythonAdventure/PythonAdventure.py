#Written by Talkashie

# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep

exit=0
location=0
maxhp=25
hp=25
gp=0
userinput=""
inventory=["HP Potion (Small)","HP Potion (Small)","HP Potion (Small)"]

def drawStats():
	print("HP: " + str(hp) + "/" + str(maxhp))
	print("GP: " + str(gp))

def draw():
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
		print("\n\n\nCOMMANDS: Inventory")


def drawInventory():
	system('cls')
	print("INVENTORY:\n")
	#print(*inventory)
	for i in range(len(inventory)):
		print(str(i) + ": " + inventory[i])
	system('pause')

def userInput():
	#Here we process user input depending upon the location
	myInput=input("\nCOMMAND: ")
	myInput=myInput.lower()
	global location

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

while(exit==0):
	draw()
	userInput()
