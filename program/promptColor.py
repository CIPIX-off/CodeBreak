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

terminalTitle('Setting/PromptColor')

while True :
    try : 
        print(f'''
{TIME()} {INPUT} Please select a color from the following choices :
    {white}    [1] : White
    {purple}    [2] : Purple
    {blue}    [3] : Blue
    {red}    [4] : Red
    {green}    [5] : Green
    {yellow}    [6] : Yellow {reset}
''')
        choicePromptColor = input(Prompt('Setting')).strip().lstrip('0')
        
        if choicePromptColor == '1':
            data['promptColor'] = 'white'
        elif choicePromptColor == '2':
            data['promptColor'] = 'purple'
        elif choicePromptColor == '3':
            data['promptColor'] = 'blue'
        elif choicePromptColor == '4':
            data['promptColor'] = 'red'
        elif choicePromptColor == '5':
            data['promptColor'] = 'green'
        elif choicePromptColor == '6':
            data['promptColor'] = 'yellow'
        else :
            print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')
            Pause()
        Sauvegarde()
        setPromptColor(data)
        startMenu('setting.py')
    except Exception as error :
        print(f'{TIME_RED()} {ERROR} Error : {error}')