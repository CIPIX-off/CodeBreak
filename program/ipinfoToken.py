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
    
terminalTitle('Setting/IpInfo Token')


try : 
    print(f'\n{TIME_YELLOW()} {INFO_YELLOW} IpInfo token : {data['ipinfoToken']}')
    print(f"{TIME()} {INPUT} Please provide the token obtained from https://ipinfo.io/ (leave blank if you don't have one). {reset}\n")
    choice = input(Prompt('Setting')).strip()
    
    if choice == '':
        data['ipinfoToken'] = 'null'
    else :
        data['ipinfoToken'] = choice
    Sauvegarde()
    print(f'\n{TIME()} {INFO} IpInfo token set to :{lightLilac} {data['ipinfoToken']}')
except Exception as error :
    print(f'{TIME_RED()} {ERROR} Error : {error}')

Pause()
startMenu('setting.py')
