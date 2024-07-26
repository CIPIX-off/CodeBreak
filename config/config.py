# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try:
    import colorama, json, subprocess, os, sys, datetime, requests, webbrowser
    from config.info import *
except Exception as error:
    import os
    print(f'Error in Module : {error}')
    os.system("pause")

colorama.init()
color = colorama.Fore
reset = color.RESET
purple = '\033[38;2;131;0;255m'
white = color.WHITE
yellow = color.YELLOW
blue = color.BLUE
red = color.RED
green = color.GREEN

parametreFichier = 'config/parametre.json'

def githubVersion():
    response = requests.get(linkUpdate)
    if response.status_code == 200:
        github_vars = {}
        exec(response.text, github_vars)
        return github_vars.get('versionCode')
    else:
        print(f"{TIME_RED()} {ERROR} Unable to retrieve the info.py file from the GitHub repository.")
        Pause()
    
def checkUpdate():
    github_version = githubVersion()

    if versionCode != github_version:
        print(f"""
{TIME_RED()} {ERROR} Update available ! 

    Current version :{yellow} {versionCode} {red}
    New version :{green} {github_version} {red}
    Please update CodeBreak to get the latest improvements and fixes.
    Opening the update link in your browser... {reset}
""")
        webbrowser.open(linkGithub)
#        if sys.platform.startswith("win"):
#            file = f'python update.py'
#            subprocess.run(file, shell=True)
#        elif sys.platform.startswith("linux"):       Soon !
#            file = f'python3 update.py'
#            subprocess.run(file, shell=True)
#    else:
#        pass

def Sauvegarde() :
    try:
        with open(parametreFichier, 'w') as fichier:
            json.dump(data, fichier, indent=4)
    except FileNotFoundError:
        print(f'{red}[{white}x{red}] The file {parametreFichier} is not found. {reset}')
        os.system('pause')
    except Exception as error:
        print(f'{red}[{white}x{red}] An error occurred while saving the settings: {yellow}{error}{reset}')
        os.system('pause')

try: 
    with open(parametreFichier, 'r') as fichier:
        data = json.load(fichier)
except FileNotFoundError:
    print(f'{red}[{white}x{red}] The file {parametreFichier} is not found. {reset}')
    os.system('pause')
except json.JSONDecodeError:
    print(f'{red}[{white}x{red}] JSON decoding error in the file {parametreFichier}. {reset}')
    os.system('pause')
except Exception as error:
    print(f'{red}[{white}x{red}] An error occurred while loading the settings: {yellow}{error}{reset}')
    os.system('pause')

def setPromptColor(setting):
    global promptColor
    if setting['promptColor'] == 'white':
        promptColor = white
    elif setting['promptColor'] == 'yellow':
        promptColor = yellow
    elif setting['promptColor'] == 'blue':
        promptColor = blue
    elif setting['promptColor'] == 'red':
        promptColor = red
    elif setting['promptColor'] == 'green':
        promptColor = green
    elif setting['promptColor'] == 'purple':
        promptColor = purple
    else:
        promptColor = white
        print(f'{ERROR} Unknown prompt color: {data['promptColor']}. Using default white.')
        os.system('pause')

setPromptColor(data)
        
try:
    username = os.getlogin()
except:
    username = 'user'

def TIME_H():
    return datetime.datetime.now().strftime('%H:%M:%S')

def CLEAR():
    if sys.platform.startswith("win"):
        os.system("cls")
    else :
        os.system("clear")

def terminalTitle(title):
    if sys.platform.startswith("win"):
        os.system(f'title CodeBreak - {title}')
    else:
        sys.stdout.write(f"\033]0;CodeBreak - {title}\007")
        sys.stdout.flush()
    
def mainMenu():
        print(f'{TIME_YELLOW()} {WAIT_YELLOW} Loading main menu...')
        if sys.platform.startswith("win"):
            file = 'python ./CodeBreak.py'
            subprocess.run(file, shell=True)
        elif sys.platform.startswith("linux"):
            file = 'python3 ./CodeBreak.py'
            subprocess.run(file, shell=True)

def startProgram(program):
    if sys.platform.startswith("win"):
        file = f'python Program/{program}'
        subprocess.run(file, shell=True)
    elif sys.platform.startswith("linux"):
        file = f'python3 Program/{program}'
        subprocess.run(file, shell=True)

def startMenu(program):
    if sys.platform.startswith("win"):
        file = f'python menu/{program}'
        subprocess.run(file, shell=True)
    elif sys.platform.startswith("linux"):
        file = f'python3 menu/{program}'
        subprocess.run(file, shell=True)
        
def Pause():
    input(f"{TIME()} {WAIT} Press to continue >>> {reset}")
def Soon():
    print(f'{TIME_YELLOW()} {INFO_YELLOW} The chosen option will arrive soon. {reset}')
    Pause()

ERROR = f'{red}[{white}x{red}]'

ADD = f'{purple}[{white}+{purple}]'
INFO = f'{purple}[{white}!{purple}]'
INPUT = f'{purple}[{white}>{purple}]'
WAIT = f'{purple}[{white}~{purple}]'
def TIME(): 
    return f'{purple}[{white}{TIME_H()}{purple}]'


ADD_RED = f'{red}[{white}+{red}]'
INFO_RED = f'{red}[{white}!{red}]'
INPUT_RED = f'{red}[{white}>{red}]'
WAIT_RED = f'{red}[{white}~{red}]'
def TIME_RED(): 
    return f'{red}[{white}{TIME_H()}{red}]'

ADD_GREEN = f'{green}[{white}+{green}]'
INFO_GREEN = f'{green}[{white}!{green}]'
INPUT_GREEN = f'{green}[{white}>{green}]'
WAIT_GREEN = f'{green}[{white}~{green}]'
def TIME_GREEN(): 
    return f'{green}[{white}{TIME_H()}{green}]'

ADD_YELLOW = f'{yellow}[{white}+{yellow}]'
INFO_YELLOW = f'{yellow}[{white}!{yellow}]'
INPUT_YELLOW = f'{yellow}[{white}>{yellow}]'
WAIT_YELLOW = f'{yellow}[{white}~{yellow}]'
def TIME_YELLOW(): 
    return f'{yellow}[{white}{TIME_H()}{yellow}]'

CHOICELANG = f'{purple}[{white}1{purple}] English | [{white}2{purple}] French'

MainOption = [
    {"num": 1, "titre": "Info"},
    {"num": 6, "titre": "Soon"},
    {"num": 11, "titre": "Soon"},
    {"num": 2, "titre": "Setting"},
    {"num": 7, "titre": "Soon"},
    {"num": 12, "titre": "Soon"},
    {"num": 3, "titre": "NukeBot Discord"},
    {"num": 8, "titre": "Soon"},
    {"num": 13, "titre": "Soon"},
    {"num": 4, "titre": "Soon"},
    {"num": 9, "titre": "Soon"},
    {"num": 14, "titre": "Soon"},
    {"num": 5, "titre": "Soon"},
    {"num": 10, "titre": "Soon"},
    {"num": 15, "titre": "Soon"},
]