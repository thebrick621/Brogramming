import color
color = color.color
import scenes
from scenes import scene1

def choice1():
  print("")
  print(color.GREEN + "You're able to hear the whirr of a computer fan, as well as a car alarm blaring. It must have been what woke you up. You can also hear a non-distinct voice somewhere else in the house, but you can't pin down where." + color.END)
  scene1.choice1()

def s1Creeping():
  print("")
  print(color.GREEN + "You hear someone quietly walking around the house. Your door is closed and footsteps are faint, but you hear them." + color.END)