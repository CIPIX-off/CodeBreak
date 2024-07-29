# © 2024 CIPIX
# All rights reserved.
# Tous droits réservés.

import os, sys, requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import *
from config.menu import Prompt

terminalTitle('IpInfo')

def pprint(text, info):
    print(f'{ADD} {text} : {lightLilac}{info}{reset}')

def scanIp(ip):
    global token
    token = data['ipinfoToken']
    if ip in ['myip', 'my', 'me'] :
        if token == 'null':
            url = f"https://ipinfo.io/json"
        else:
            url = f"https://ipinfo.io/json?token={token}"
    else :
        if token == 'null':
            url = f"https://ipinfo.io/{ip}"
        else:
            url = f"https://ipinfo.io/{ip}?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    print(f'\n{TIME()} {INPUT} please enter an ip address (enter "me" for your IP information){reset}\n')
    ip = input(Prompt('IpInfo')).lower().replace(' ','')
    info = scanIp(ip)
    print('')
    if info:
        if info.get("bogon"):
            print(f"{TIME_RED()} {ADD_RED} The IP {ip} is a bogon address ! {reset}")

        else :
            pprint("IP", info.get('ip'))
            pprint("Hostname", info.get('hostname'))
            pprint("City", info.get('city'))
            pprint("Region", info.get('region'))
            pprint("Country", info.get('country'))
            pprint("Location", info.get('loc'))
            pprint("Organization", info.get('org'))
            pprint("Postal", info.get('postal'))
            pprint("Timezone", info.get('timezone'))
            
            if token == 'null':
                print(f"\n{TIME_YELLOW()} {INFO_YELLOW} With a token, you could obtain much more information.\n               For more details, please visit https://ipinfo.io/.")  
                
            else:
                asn = info.get('asn', {})
                pprint("ASN", asn.get('asn'))
                pprint("ASN Name", asn.get('name'))
                pprint("ASN Domain", asn.get('domain'))
                pprint("ASN Route", asn.get('route'))
                pprint("ASN Type", asn.get('type'))

                company = info.get('company', {})
                pprint("Company Name", company.get('name'))
                pprint("Company Domain", company.get('domain'))
                pprint("Company Type", company.get('type'))

                carrier = info.get('carrier', {})
                pprint("Carrier Name", carrier.get('name'))
                pprint("Carrier MCC", carrier.get('mcc'))
                pprint("Carrier MNC", carrier.get('mnc'))

                privacy = info.get('privacy', {})
                pprint("VPN", privacy.get('vpn'))
                pprint("Proxy", privacy.get('proxy'))
                pprint("Tor", privacy.get('tor'))
                pprint("Relay", privacy.get('relay'))
                pprint("Hosting", privacy.get('hosting'))
                pprint("Service", privacy.get('service'))

                abuse = info.get('abuse', {})
                pprint("Abuse Address", abuse.get('address'))
                pprint("Abuse Country", abuse.get('country'))
                pprint("Abuse Email", abuse.get('email'))
                pprint("Abuse Name", abuse.get('name'))
                pprint("Abuse Network", abuse.get('network'))
                pprint("Abuse Phone", abuse.get('phone'))
    else:
        print(f"{TIME_RED()} {ERROR} Unable to retrieve information for this IP.")

if __name__ == "__main__":
    main()
    print('')
    Pause()
    mainMenu()
