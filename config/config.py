# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try:
    import colorama, json, subprocess, os, sys, datetime, requests, webbrowser, platform
    from config.info import *
    from colorama import Fore, Style
except Exception as error:
    import os
    print(f'Error in Module : {error}')
    os.system("pause")

data = {}
colorama.init()
color = colorama.Fore
reset = Style.RESET_ALL
purple = '\033[38;2;131;0;255m'
lightPurple = '\033[38;2;178;102;255m'
pink = '\033[38;2;255;105;180m'
lightBlue = '\033[38;2;173;216;230m'
lightLilac = '\033[38;2;200;162;200m'
white = color.WHITE
yellow = color.YELLOW
blue = color.BLUE
red = color.RED
green = color.GREEN
bold = Style.BRIGHT
dim = Style.DIM
normal = Style.NORMAL

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

def setPromptColor():
    global promptColor
    if data['promptColor'] == 'white':
        promptColor = white
    elif data['promptColor'] == 'yellow':
        promptColor = yellow
    elif data['promptColor'] == 'blue':
        promptColor = blue
    elif data['promptColor'] == 'red':
        promptColor = red
    elif data['promptColor'] == 'green':
        promptColor = green
    elif data['promptColor'] == 'purple':
        promptColor = purple
    else:
        promptColor = white
        print(f'{ERROR} Unknown prompt color: {data['promptColor']}. Using default white.')
        Pause()

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

def errorModule(error):
    print(f'{TIME_RED()} {ERROR} Error Module (Restart install.bat) or contact support on the discord server : {yellow}{error}{reset}')
    webbrowser.open(linkDiscord)
    Pause()
    mainMenu()

def error(error):
    print(f"\n{TIME_RED()} {ERROR} Error : {yellow}{error}{reset}")
    Pause()
    mainMenu()

def errorUrl():
    print(f"\n{TIME_RED()} {ERROR} Invalid URL ! {reset}")
    Pause()
    mainMenu()
        
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
    {"num": 4, "titre": "Discord Invitation Info"},
    {"num": 9, "titre": "Soon"},
    {"num": 14, "titre": "Soon"},
    {"num": 5, "titre": "IpScan"},
    {"num": 10, "titre": "Soon"},
    {"num": 15, "titre": "Soon"},
]
def Sauvegarde() :
    try:
        save_dir = setDirectory()
        filePath = os.path.join(save_dir, 'Save.json')
        with open(filePath, 'w') as fichier:
            json.dump(data, fichier, indent=4)
    except FileNotFoundError:
        print(f'{TIME_RED()} {ERROR} The file {filePath} is not found. {reset}')
        Pause()
    except Exception as error:
        print(f'{TIME_RED()} {ERROR} An error occurred while saving the settings: {yellow}{error}{reset}')
        Pause()

def setDirectory():
    if platform.system() == 'Windows':
        documents_folder = os.path.join(os.path.expanduser('~'), 'Documents')
        return os.path.join(documents_folder, 'CodeBreak')
    elif platform.system() == 'Linux':
        return os.path.join(os.path.expanduser('~'), '.local', 'share', 'CodeBreak')
    elif platform.system() == 'Darwin':
        library_folder = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support')
        return os.path.join(library_folder, 'CodeBreak')
    else:
        raise OSError(f"{TIME_RED()} {ERROR} Système d'exploitation non supporté{reset}")
    
def saveDirectory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f'{TIME_RED()} {ERROR}  Erreur lors de la création du dossier {path}: {e} {reset}')
        Pause()

def loadData(saveFile):
    if os.path.exists(saveFile):
        try :
            with open(saveFile, 'r') as fichier:
                data = json.load(fichier)
                if not isinstance(data, dict):
                    return {}
                return data
        except FileNotFoundError:
            print(f'{TIME_RED()} {ERROR}  The file {saveFile} is not found. {reset}')
        except json.JSONDecodeError:
            print(f'{TIME_RED()} {ERROR}  JSON decoding error in the file {saveFile}. {reset}')
        except Exception as error:
            print(f'{TIME_RED()} {ERROR}  An error occurred while loading the settings: {yellow}{error}{reset}')
        return defaultData
    else:
        return defaultData

def FirstSauvegarde(file_path, data):
    try:
        with open(file_path, 'w') as fichier:
            json.dump(data, fichier, indent=4)
    except Exception as error:
        print(f'{TIME_RED()} {ERROR}  Une erreur est survenue lors de la sauvegarde des paramètres : {yellow}{error}{reset}')
        Pause()

def upData(existing_data, newData):
    if isinstance(existing_data, dict) and isinstance(newData, dict):
        for key, value in newData.items():
            if key not in existing_data:
                existing_data[key] = value
    else:
        print(f'{TIME_RED()} {ERROR} Les données existantes ou nouvelles ne sont pas des dictionnaires.{reset}')
    return existing_data


try:
    username = os.getlogin()
except:
    username = 'user'

defaultData = {
    "promptColor": "purple",
    "token": "null",
    "excludeIds": [
        "726772485252710503"
    ],
    "censureToken": "False",
    "ipinfoToken": "null"
}

def main():
    global data

    try :
        save_dir = setDirectory()
        save_file_path = os.path.join(save_dir, 'Save.json')
        saveDirectory(save_dir)
        existing_data = loadData(save_file_path)
        data = upData(existing_data, defaultData)
        FirstSauvegarde(save_file_path, data)
    except Exception as error:
        print(f'{TIME_RED()} {ERROR} error loading/writing backup : {error} {reset}')
        Pause()

    try: 
        setPromptColor()
    except Exception as error:
        print(f'{TIME_RED()} {ERROR} error setPromptColor : {error} {reset}')
        Pause()
main()