from commands import touch
from commands import use
from commands import grab
from scenes import scene2
import essential
from commands import command
import color
color = color.color

def poster():
  if "flag" in grab.posterflaglist:
    poster_act1 = essential.prompt()
    poster_act1 = poster_act1.lower()
    while poster_act1 not in command.poster:
      print("\n Please Try Again.")
      poster()
      
    if poster_act1 == str("help"):
      print("")
      for r in command.poster:
        print(color.PURPLE + r + color.END)
      poster()
      
    if poster_act1 == str("grab"):
      grab.postersnatch()
      poster()
      
    if poster_act1 == str("touch"):
      touch.poster()
      poster()
      
    if poster_act1 == str("look"):
      print("")
      print(color.GREEN + "You see a poster for Mega Milk Man X-2: Moopocalypse. Its your favorite movie." + color.END)
      poster()
      
    if poster_act1 == str("use"):
      use.nouse()
      poster()
    
    if poster_act1 == str("exit"):
      scene2.exit_room()
  else:
    print("")
    print(color.GREEN + "You look at the empty space where a poster once used to reside." + color.END)
  