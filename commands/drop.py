import color
from player import inventory
color = color.color
from scenes import scene1

def choice1():
  if bool(inventory.current_inv) is False:
    print("")
    print(color.GREEN + "You have nothing in your inventory." + color.END)
    scene1.choice1()
  else:
    inventory.invcheck()
    scene1.choice1()
    