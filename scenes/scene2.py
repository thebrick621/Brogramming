from commands import move
from commands import command
from commands import look
from commands import touch
from commands import eat
from commands import smell
from commands import use
from commands import grab
from commands import listen
from commands import drop
from player import inventory
from scenes import posterzone
import loc
import essential
import color
color = color.color

def exit_room():
  move1 = essential.moveprompt()
  move1 = move1.lower()
  
  while move1 not in loc.room1:
    print("\n Please Try Again.")
    exit_room()
  
  if move1 == str("help"):
    print("")
    for r in loc.room1:
      print(color.PURPLE + r + color.END)
    exit_room()
  
  if move1 == str("poster"):
    posterzone.poster()
    exit_room()
  
  if move1 == str("door"):
    loc.ur_roomdoor()
    
  if move1 == str("closet"):
    loc.ur_closet()
    
  if move1 == str("window"):
    loc.ur_roomwindow()
    
  if move1 == str("exit"):
    choice1()




  #Choice 1
def choice1():
  desc1 = essential.start()
  desc1 = desc1.lower()
  while desc1 not in command.comlist:
    print("\n Please Try Again.")
    choice1()
  if desc1 == str("help"):
    print("")
    for x in command.comlist:
      print(color.PURPLE + x + color.END)
    choice1()

  if desc1 == str("look"):
    look.choice2()
    choice1()
    
  if desc1 == str("touch"):
    touch.desk()
    choice1()
    
  if desc1 == str("use"):
    use.nouse()
    choice1()   
    
  if desc1 == str("eat"):
    eat.hungrys1()
    choice1()
    
  if desc1 == str("smell"):
    smell.choice1()
    choice1()
    
  if desc1 == str("listen"):
    listen.s1Creeping()
    choice1()
    
  if desc1 == str("grab"):
    grab.postersnatch()
    choice1()
    
  if desc1 == str("drop"):
    drop.xxx()

  if desc1 == str("move"):
    exit_room()
    
  if desc1 == str("inventory"):
    inventory.invcheck()
    choice1()