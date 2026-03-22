# C:\Windows\System32\drivers\etc\hosts 
# --uac-admin

import json
import sys

current_ver = '1.0.0'
json_data_file_name = 'data.json'

def isFirstTime(json_file = json_data_file_name):
    with open(json_file) as f:
        data = json.load(f)

    return data.get('howManyTimesOpened')

def main():
    if isFirstTime() == 0:
        pass
    else: 
        print(f"Hello, It's TUNGUSKA v{current_ver}")
        action = input('Input an action below:\n1 - Turn off\n')

        if action == '1':
            pass
        else:
            sys.exit(1)

main()