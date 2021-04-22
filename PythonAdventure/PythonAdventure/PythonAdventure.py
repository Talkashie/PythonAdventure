
#Written by Talkashie

# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

exit=0
location=0
maxhp=25
hp=25
userinput=""

def draw(loc):
    system('cls')
    #Main Menu
    if(loc==0):
        
        print("Python Adventure!")
        print("Written by Talkashie")
        print("\n\n\nPLAY")

    #Cabin
    if(loc==1):
        print("Location: Your cabin\n\n\n\n\n")
        print("Written by Talkashie")
        print("\n\n\nPLAY")

while(exit==0):
    draw(location)
    userinput=input("")
    userinput=userinput.lower()
    if(userinput=="exit"):
        exit=1


