# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try:
   from config.config import *
   from config.menu import *
   from menu.discordAnim import discordAnim
   import os
except Exception as e :
    errorModule(e)

terminalTitle('MainMenu')
checkUpdate()

while True:
   try:
      CLEAR()
      print(TITLE, LINK)
      MENU(MainOption)
      select = input(Prompt('Main Menu')).strip().lstrip('0')
      if select == '1':
         startProgram("info.py")
      elif select == '2':
         startMenu("setting.py")
      elif select == '3':
         discordAnim('nukeBot.py')
      elif select == '4':
         startProgram('infoServerDisc.py')
      elif select == '5':
         startProgram('ipInfo.py')
      elif select == '6':
         Soon()
      elif select == '7':
         Soon()
      elif select == '8':
         Soon()
      elif select == '9':
         Soon()
      elif select == '10':
         Soon()
      elif select == '11':
         Soon()
      elif select == '12':
         Soon()
      elif select == '13':
         Soon()
      elif select == '14':
         Soon()
      elif select == '15':
         Soon()
      else:
         print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')
         Pause()
   except Exception as error:
      print(f'{ERROR} An error has occurred.\n{yellow}{error}{reset}')
      os.system("pause")


