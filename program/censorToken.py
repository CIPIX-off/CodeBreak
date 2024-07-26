# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

import colorama, sys, os
colorama.init()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import *
from config.menu import *
terminalTitle('Setting/Censor token')

while True :
    try : 
        print(f'''
{TIME()} {INPUT} Do you want to censor your bot token ? {green}[1] Yes {purple}| {red}[2] No {reset}
''')
        choice = input(Prompt('Setting')).strip().lstrip('0')
        
        if choice == '1':
            data['censureToken'] = 'True'
        elif choice == '2':
            data['censureToken'] = 'False'
        else :
            print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')
            Pause()
        Sauvegarde()
        startMenu('setting.py')
    except Exception as error :
        print(f'{TIME_RED()} {ERROR} Error : {error}')