
from player import inventory
import color
color = color.color
import scenes
from scenes import scene1

posterflaglist = ["flag"]

def choice1():
  print("")
  print(color.GREEN + "You grab at your chest and your legs. Yes, they indeed are still there. There's nothing else to grab." + color.END)
  scene1.choice1()

def postersnatch():
  print("")
  print(color.GREEN + "You snatch the poster off the wall, fold it neatly and put it in your pocket." + color.END)
  inventory.current_inv.append("Poster")
  inventory.inv_sizecheck()
  posterflaglist.pop()