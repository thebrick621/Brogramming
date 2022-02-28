import essential
from commands import move
from commands import command
from commands import look
from commands import touch
from commands import eat
from commands import smell
from commands import grab
from commands import listen
from commands import use
from commands import drop
from player import inventory
from scenes import scene2
import color
color = color.color
  
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
    #ANSWER AND SKIP TO CHOICE 2
    look.choice1()
    scene2.choice1()
 
  if desc1 == str("touch"):
    touch.choice1()
    
  if desc1 == str("use"):
    use.choice1()
    
  if desc1 == str("eat"):
    eat.choice1()
    
  if desc1 == str("smell"):
    smell.choice1()
    scene1.choice1()
    
  if desc1 == str("listen"):
    listen.choice1()
    
  if desc1 == str("grab"):
    grab.choice1()
    
  if desc1 == str("drop"):
    drop.choice1()
    
  if desc1 == str("move"):
    move.choice1()
    
  if desc1 == str("inventory"):
    inventory.invcheck()
    choice1()