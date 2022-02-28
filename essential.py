import color
from commands import command
color = color.color


def start():
  print("")
  command.help()
  print("")
  f = input(color.CYAN + "What would you like to do? \n" + color.END)
  return f


def prompt():
  print("")
  f = input(color.CYAN + "What would you like to do? \n" + color.END)
  return f

def moveprompt():
  print("")
  f = input(color.CYAN + "Where would you like to move? \n" + color.END)
  return f