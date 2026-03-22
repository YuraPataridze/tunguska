# --uac-admin

import json
import sys

current_ver = 'v1.0.0'
json_data_file_name = 'data.json'
hosts = 'C:\Windows\System32\drivers\etc\hosts'

def isFirstTime(json_file = json_data_file_name):
    with open(json_file) as f:
        data = json.load(f)

    return data.get('howManyTimesOpened')

def changeHosts(siteURL):
    try:
        with open(hosts, 'a', 'utf-8') as h:
            h.write(f'\n127.0.0.1 {siteURL}')
        return f"Congcongratulation! You've just blocked {siteURL}!"
    except Exception as e:
        return 'Some ERROR: ' + e

def main():
    if isFirstTime() == 0:
        print(f"Hello, It's TUNGUSKA {current_ver}")
        action = input('Input an action below:\n1 - Input site URL I want to block\n')
        if action == '1':
            siteURL = input('Input a site URL (e.g., 1xbet.ru)')
            answer = input(f"Are You seriously think it's good idea to block {siteURL}? [Y/n]")
            if answer == 'Y':
                changeHosts(siteURL)
                input('Press any button to leave')
                sys.exit(0)
            elif answer == 'n':
                input(f'Press any button to leave and then start the TUNGUSKA {current_ver} again')
                sys.exit(0)
            else:
                sys.exit(1)
        else:
            sys.exit(1)

    else: 
        print(f"Hello, It's TUNGUSKA {current_ver}")
        action = input('Input an action below:\n1 - Turn off\n')

        if action == '1':
            pass
        else:
            sys.exit(1)

main()