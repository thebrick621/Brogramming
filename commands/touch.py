import color
color = color.color
from scenes import scene2
from scenes import scene1

def choice1():
  print("")
  print(color.GREEN + "You feel a cold, hard wooden surface underneath your arms. Your fingers feel as if they have some sort of powder on them. You're sitting. The chair underneath you is made of mesh yet is somehow less breathable than your asmthmatic lungs which you feel weighing you down." + color.END)
  scene1.choice1()

def desk():
  print("")
  print(color.GREEN + "You can feel the desk." + color.END)
  scene2.choice1()

def poster():
  print("")
  print(color.GREEN + "You touch the wall. It sure is drywall." + color.END)