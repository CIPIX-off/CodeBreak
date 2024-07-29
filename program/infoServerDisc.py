# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try:
    import os, sys, textwrap
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config.config import *
    from config.menu import Prompt
    from datetime import datetime
    import requests
except Exception as e:
   errorModule(e)

terminalTitle("Invite Info (Discord)")

PUBLIC_FLAGS = {
    0: 'None',
    1 << 0: 'Discord Employee',
    1 << 1: 'Partnered Server Owner',
    1 << 2: 'HypeSquad Events',
    1 << 3: 'Bug Hunter Level 1',
    1 << 6: 'House Bravery',
    1 << 7: 'House Brilliance',
    1 << 8: 'House Balance',
    1 << 9: 'Early Supporter',
    1 << 10: 'Team User',
    1 << 12: 'System',
    1 << 14: 'Bug Hunter Level 2',
    1 << 16: 'Verified Bot',
    1 << 17: 'Early Verified Bot Developer',
}
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def Sbadges():
    user_flags = invite_info['inviter']['public_flags']
    badges = []
    for flag, description in PUBLIC_FLAGS.items():
        if user_flags & flag:
            badges.append(description)
    if not badges:
        badges = 'None'
    return badges

def format_list(lst):
    width=50
    wrapped_lines = []
    for item in lst:
        wrapped_lines.extend(textwrap.wrap(item, width))
    return f'\n{dim}{purple}        └──────────────── {normal}: {lightLilac}'.join(wrapped_lines)

def saveFile(content):
    output_dir = 'Output/Invitation-Info'
    os.makedirs(output_dir, exist_ok=True)
    filename = datetime.now().strftime('Invitation-Info-%Y%m%d%H%M%S.txt')
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\n{TIME()} {ADD} Information saved in the file : {file_path}")


try:
    print(f"\n{TIME()} {INPUT} Please enter a discord server invitation.\n")
    invite = input(Prompt('Invite Info'))
    print(f"\n{TIME()} {INPUT} Do you want to save this information to a file ? (yes/no) (default : no).\n")
    save = input(Prompt('Invite Info')).strip().lower()
    response = requests.get(f"https://discord.com/api/v9/invites/{invite.split("/")[-1]}")

    if response.status_code == 200:
        data = response.json()
        schemaApi = {
            "type": "None",
            "code": "None",
            "expires_at": "None",
            "flags": "None",
            "guild_id": "None",
            "guild": {
                "name": "None",
                "icon": "None",
                "features": "None",
                "verification_level": "None",
                "nsfw_level": "None",
                "nsfw": "None",
                "premium_subscription_count": "None"
            },
            "channel": {
                "id": "None",
                "type": "None",
                "name": "None"
            },
            "inviter": {
                "id": "None",
                "username": "None",
                "avatar": "None",
                "discriminator": "None",
                "public_flags": "None",
                "flags": "None",
                "banner": "None",
                "accent_color": "None",
                "global_name": "None",
                "banner_color": "None"
            }
        }
     
        invite_info = deep_update(schemaApi, data)

        print(f"""{blue} {bold}
Invitation Information {normal}
    {ADD} Invitation        : {lightLilac}https://discord.gg/{invite.split("/")[-1]}
    {ADD} Type              : {lightLilac}{invite_info['type']}
    {ADD} Code              : {lightLilac}{invite_info['code']}
    {ADD} Expired           : {lightLilac}{invite_info['expires_at']}
    {blue} {bold}
Server Information {normal}     
    {ADD} ID                : {lightLilac}{invite_info['guild_id']}
    {ADD} Name              : {lightLilac}{invite_info['guild']['name']}
    {ADD} Icon              : {lightLilac}{invite_info['guild']['icon']}
    {ADD} Features          : {lightLilac}{format_list(invite_info['guild']['features'])}
    {ADD} NSFW Level        : {lightLilac}{invite_info['guild']['nsfw_level']}
    {ADD} Server NSFW       : {lightLilac}{invite_info['guild']['nsfw']}
    {ADD} Flags             : {lightLilac}{invite_info['flags']}
    {ADD} Verif Level       : {lightLilac}{invite_info['guild']['verification_level']}
    {ADD} Boosts            : {lightLilac}{invite_info['guild']['premium_subscription_count']}        
    {blue} {bold}
Channel Information {normal}
    {ADD} Name              : {lightLilac}{invite_info['channel']['name']}        
    {ADD} ID                : {lightLilac}{invite_info['channel']['id']}
    {ADD} Type              : {lightLilac}{invite_info['channel']['type']}
    {blue} {bold}
Inviter Information {normal}
    {ADD} ID                : {lightLilac}{invite_info['inviter']['id']}
    {ADD} Username          : {lightLilac}{invite_info['inviter']['username']}
    {ADD} Global Name       : {lightLilac}{invite_info['inviter']['global_name']}
    {ADD} Avatar            : {lightLilac}{invite_info['inviter']['avatar']}
    {ADD} Link avatar       : {lightLilac}https://cdn.discordapp.com/avatars/{invite_info['inviter']['id']}/{invite_info['inviter']['avatar']}.png
    {ADD} Discriminator     : {lightLilac}{invite_info['inviter']['discriminator']}
    {ADD} Public Flags      : {lightLilac}{invite_info['inviter']['public_flags']}
    {ADD} Flags             : {lightLilac}{invite_info['inviter']['flags']}
    {ADD} Badges            : {lightLilac}{Sbadges()}
    {ADD} Banner            : {lightLilac}{invite_info['inviter']['banner']}
    {ADD} Link banner       : {lightLilac}https://cdn.discordapp.com/banners/{invite_info['inviter']['id']}/{invite_info['inviter']['banner']}.png
    {ADD} Accent Color      : {lightLilac}{invite_info['inviter']['accent_color']}
    {ADD} Banner Color      : {lightLilac}{invite_info['inviter']['banner_color']}
    """)
        
        if save in ['yes', 'y']:
            output = f"""Invitation Information
    Invitation        : https://discord.gg/{invite.split("/")[-1]}
    Type              : {invite_info['type']}
    Code              : {invite_info['code']}
    Expired           : {invite_info['expires_at']}
    
Server Information   
    ID                : {invite_info['guild_id']}
    Name              : {invite_info['guild']['name']}
    Icon              : {invite_info['guild']['icon']}
    Features          : {invite_info['guild']['features']}
    NSFW Level        : {invite_info['guild']['nsfw_level']}
    Server NSFW       : {invite_info['guild']['nsfw']}
    Flags             : {invite_info['flags']}
    Verif Level       : {invite_info['guild']['verification_level']}
    Boosts            : {invite_info['guild']['premium_subscription_count']}        

Channel Information
    Name              : {invite_info['channel']['name']}        
    ID                : {invite_info['channel']['id']}
    Type              : {invite_info['channel']['type']}

Inviter Information
    ID                : {invite_info['inviter']['id']}
    Username          : {invite_info['inviter']['username']}
    Global Name       : {invite_info['inviter']['global_name']}
    Avatar            : {invite_info['inviter']['avatar']}
    Link avatar       : https://cdn.discordapp.com/avatars/{invite_info['inviter']['id']}/{invite_info['inviter']['avatar']}.png
    Discriminator     : {invite_info['inviter']['discriminator']}
    Public Flags      : {invite_info['inviter']['public_flags']}
    Flags             : {invite_info['inviter']['flags']}
    Badges            : {Sbadges()}
    Banner            : {invite_info['inviter']['banner']}
    Link Banner       : https://cdn.discordapp.com/banners/{invite_info['inviter']['id']}/{invite_info['inviter']['banner']}.png
    Accent Color      : {invite_info['inviter']['accent_color']}
    Banner Color      : {invite_info['inviter']['banner_color']}
    """
        if save in ['yes', 'y']:
            saveFile(output)
    else:
        errorUrl()
    Pause()
    mainMenu()
except Exception as e:
    errorModule(e)