import color
import essential
import loc
import options
color = color.color
from scenes import scene1
from scenes import scene2

def choice1():
  print("")
  print(color.GREEN + "You stand. You then decide to do a little jig before sitting back down. Why were you dancing? Who knows. Either way, you have no reason to move yet. If only I could see my surroundings..." + color.END)
  scene1.choice1()