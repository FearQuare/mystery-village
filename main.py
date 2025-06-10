from citizen import *
from colorama import Fore, Back, Style, init

town = {
    "name": 'Mystery Town',
    "citizens": [],
    "mystery_events": [],
}

def enter_citizen():
    # Setting the citizen's id
    current_population = len(town['citizens'])
    if current_population > 0:
        id = town['citizens'][current_population-1]['id'] + 1
    else:
        id = 1
    
    # Setting the identity information of the citizen
    name = input(Style.BRIGHT + Fore.BLUE + "Enter the name of the new citizen: " + Style.RESET_ALL)
    age = input(Style.BRIGHT + Fore.BLUE + "Enter the age of the new citizen: " + Style.RESET_ALL)

    identity = (name, int(age))

    # Setting the job info of the citizen
    job = input(Style.BRIGHT + Fore.BLUE + "Enter the occupation of the new citizen. If there is none leave here empty: " + Style.RESET_ALL)

    # Setting the status of the citizen
    statusFlag = True

    while statusFlag:

        status_option = (
            f"{Style.BRIGHT + Fore.BLUE}What's the status of the citizen: {Style.RESET_ALL}\n"
            f"  {Back.GREEN}1. Normal{Style.RESET_ALL}\n"
            f"  {Back.YELLOW}2. Missing{Style.RESET_ALL}\n"
            f"  {Back.RED}3. Suspicious{Style.RESET_ALL}\n"
            f"{Style.BRIGHT + Fore.BLUE}Enter your selection: {Style.RESET_ALL}"
        )

        status = int(input(status_option))
        
        if status == 1:
            status = "Normal"
            statusFlag = False
        elif status == 2:
            status == "Missing"
            statusFlag = False
        elif status == 3:
            status == "Suspicious"
            statusFlag = False
        else:
            print("Please enter a valid status.")
    
    if job != '':
        citizen = create_citizen(id, identity, status, job)
    else:
        citizen = create_citizen(id, identity, status)
    
    town['citizens'].append(citizen)

def print_town_info():
    town_info = (
    f"{Style.BRIGHT}Town Information:{Style.RESET_ALL}\n"
    f"    * {Style.BRIGHT + Fore.RED}Name{Style.RESET_ALL}: {town['name']}\n"
    f"    * {Style.BRIGHT + Fore.RED}Citizens{Style.RESET_ALL}: {len(town['citizens'])}\n"
    f"    * {Style.BRIGHT + Fore.RED}Amount of Mystery Events{Style.RESET_ALL}: {len(town['mystery_events'])}\n"
    )
    print(town_info)

flag = True
welcome_ascii = r"""
__        __   _                            _                         
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                 
 __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/                  
|  \/  |_   _ ___| |_ ___ _ __ _   _  \ \   / (_) | | __ _  __ _  ___ 
| |\/| | | | / __| __/ _ \ '__| | | |  \ \ / /| | | |/ _` |/ _` |/ _ \
| |  | | |_| \__ \ ||  __/ |  | |_| |   \ V / | | | | (_| | (_| |  __/
|_|  |_|\__, |___/\__\___|_|   \__, |    \_/  |_|_|_|\__,_|\__, |\___|
        |___/                  |___/                       |___/      
"""
print(Fore.CYAN + welcome_ascii + Style.RESET_ALL)
while flag:

    print_town_info()

    menu_info = (
        f"{Style.BRIGHT}Menu:{Style.RESET_ALL}\n"
        f"  1. {Style.BRIGHT + Fore.RED}Create a citizen{Style.RESET_ALL}\n"
    )

    choice = input(menu_info)

    if int(choice) == 1:
        enter_citizen()

    print_town_info()

    flag = False