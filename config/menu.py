# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

from config.config import *

try :
    from config.info import *
except Exception as e :
    errorModule(e)

TITLE = f"""{purple}                                                                                                                                        
                        ▄████▄   ▒█████  ▓█████▄ ▓█████  ▄▄▄▄    ██▀███  ▓█████ ▄▄▄       ██ ▄█▀
                        ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓█████▄ ▓██ ▒ ██▒▓█   ▀▒████▄     ██▄█▒ 
                        ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒██▒ ▄██▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓███▄░ 
                        ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██░█▀  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄ 
                        ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░▓█  ▀█▓░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ █▄
                        ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░▒▓███▀▒░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒
                        ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░▒░▒   ░   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░  
                        ░        ░ ░ ░ ▒   ░ ░  ░    ░    ░    ░   ░░   ░    ░    ░   ▒   ░ ░░ ░ 
                        ░ ░          ░ ░     ░       ░  ░ ░         ░        ░  ░     ░  ░░  ░    
                        ░                  ░                   ░                                 
{reset}"""
NukeBotTitle = f"""{purple}
                             ███▄    █  █    ██  ██ ▄█▀▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
                             ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
                            ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
                            ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
                            ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
                            ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
                            ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░    
                               ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░       ░    ░ ░ ░ ░ ▒    ░      
                                     ░    ░     ░  ░      ░  ░    ░          ░ ░           
                                                                       ░                   
{reset}"""
LINK = f"""
                                         {blue}{linkGithub}
                                             {linkDiscord}{reset}
"""
def MENU(options):
    colonnes = 3
    largeur_numero = 2
    largeur_colonne = 30
    nombre_options = len(options)
    marge_gauche = 15
    for i in range(0, nombre_options, colonnes):
        ligne = ""
        for j in range(colonnes):
            index = i + j
            if index < nombre_options:
                option = options[index]
                formatedNum = f"{option['num']:0{largeur_numero}}"
                ligne += f"{red}[{purple}{formatedNum}{red}] {option['titre']:<{largeur_colonne}}"
            else:
                ligne += " " * (largeur_numero + 3) + " " * (largeur_colonne - 3)  # Ajuster l'espace pour les cases vides
        print((' ' * marge_gauche) + ligne + reset)
    print('')

def Prompt(place) :
    return f'{red}┌───({promptColor}{username}@CodeBreak{red})─[{promptColor}~/{place}{red}]\n└──$ {white}'

