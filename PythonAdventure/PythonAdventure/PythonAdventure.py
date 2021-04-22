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
inventory=["test","test","test2"]

def drawStats():
	print("HP: " + str(hp) + "/" + str(maxhp))
	print("GP: " + str(gp))

def draw(loc):
	system('cls')
	#Main Menu
	if(loc==0):
		print("Python Adventure!")
		print("Written by Talkashie")
		print("\n\n\nPLAY\nEXIT")

	#Cabin
	if(loc==1):
		print("Location: Your cabin\n\n\n\n\n")
		drawStats()
		print(*inventory)
		print("\n\n\nPLAY")

def userInput():
	#Here we process user input depending upon the location
	myInput=input("")
	myInput=myInput.lower()
	#Main Menu
	if(location==0):
		exit=1

while(exit==0):
	draw(location)
	userInput()
	if(userinput=="exit"):
		exit=1