# --uac-admin

import json
import sys

current_ver = 'v1.0.0'
hosts = 'C:\Windows\System32\drivers\etc\hosts'

def changeHosts(siteURL):
    try:
        with open(hosts, 'a', 'utf-8') as h:
            h.write(f'\n127.0.0.1 {siteURL}')
        return f"Congcongratulation! You've just blocked {siteURL}!"
    except Exception as e:
        return f'Oops! ERROR(changeHosts): {e}'

def main():
    print(f"Hello, It's TUNGUSKA {current_ver}")
    action = input('Input an action below:\n1 - Input site URL I want to block\n')
    if action == '1':
        siteURL = input('Input a site URL (e.g., 1xbet.ru)')
        answer = input(f"Are You seriously think it's good idea to block {siteURL}? Really, read each letter to check if it's exactly site URL You wanted to block!!!\n [Y/n]")
        if answer == 'Y':
            print(changeHosts(siteURL))
            input('Press ENTER button to leave')
            sys.exit(0)
        elif answer == 'n':
            input(f'Press ENTER button to leave and then start the TUNGUSKA {current_ver} again')
            sys.exit(0)
        else:
            sys.exit(1)
    else:
      sys.exit(1)

main()