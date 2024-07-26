# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

import colorama, sys, os
colorama.init()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import *
from config.menu import *
from config.info import *
terminalTitle('Info')

def english():
    print(f"""
{TIME_YELLOW()} {INFO_YELLOW} Information : 

    CodeBreak is a tool developed by CIPIX for practicing programming.
    Additionally, it was designed to allow other people to analyze and understand the code to know how it works.

    CodeBreak is a tool for educational and ethical purposes.
    Any other misuse is not accepted and you may be breaking 
    the law depending on the country where you live.
        
    To report a bug, give an opinion, suggestion or other. We invite you to join the discord server

    > Discord : {linkDiscord} 
    > Github : {linkGithub} 
    > Version : {versionCode}
    > Creator : {creator}
""")

def french():
    print(f"""
{TIME_YELLOW()} {INFO_YELLOW} Information : 

    CodeBreak est un outil développé par CIPIX pour s'exercer à la programmation.
    De plus, il a été conçu pour permettre à d'autres personnes d'analyser
    et de comprendre le code afin de savoir comment il fonctionne.

    CodeBreak est un outil à des fins éducatives et éthiques.
    Toute autre utilisation détournée n'est pas acceptée
    et vous pourriez enfreindre la loi selon le pays où vous habitez.

    Pour signaler un bug, donner un avis, suggestion ou autre. On vous invite a rejoindre le serveur discord

    > Discord : {linkDiscord} 
    > Github : {linkGithub}
    > Version : {versionCode}
    > Createur : {creator}
""")

    

while True:
    print(f"\n{(TIME())} {INPUT} {CHOICELANG} {reset} \n")
    command = input(Prompt('Info'))
    if command == '1':
        english()
        Pause()  
        mainMenu()
    elif command == '2':
        french()
        Pause() 
        mainMenu()
    else:
        print(f'\n{TIME_RED()} {ERROR} Invalid option! Please choose an existing option.{reset}')
        Pause()
        CLEAR()
        print(TITLE, LINK)