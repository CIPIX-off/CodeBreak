# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try :
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config.config import *
    from config.menu import *
except Exception as e :
    errorModule(e)
    
terminalTitle('Setting')

SettingOption = [
    {"num": 1, "titre": "Prompt color"},
    {"num": 5, "titre": "bot token censorship"},
    {"num": 8, "titre": "Soon"},
    {"num": 2, "titre": "Soon"},
    {"num": 6, "titre": "IpInfo Token"},
    {"num": 9, "titre": "Soon"},    
    {"num": 3, "titre": "Soon"},
    {"num": 7, "titre": "Soon"},
    {"num": 10, "titre": "Soon"},
    {"num": 4, "titre": "Exit"},
]

while True:
    try:
        CLEAR()
        print(TITLE, LINK)
        MENU(SettingOption)
        select = input(Prompt('Setting')).strip().lstrip('0')
        if select == '1':
            startProgram('promptColor.py')
        elif select == '2':
            Soon()
        elif select == '3':
            Soon()
        elif select == '4':
            mainMenu()
        elif select == '5':
            startProgram('censorToken.py')
        elif select == '6':
            startProgram('ipinfoToken.py')
        elif select == '7':
            Soon()
        elif select == '8':
            Soon()
        elif select == '9':
            Soon()
        elif select == '10':
            Soon()
        else:
            print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')
            Pause()
    except Exception as error:
        print(f'{ERROR} An error has occurred.\n{yellow}{error}{reset}')
        os.system("pause")