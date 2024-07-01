import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

def check_instagram_username_status(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find('meta', property='og:description'):
            return 'active'
        else:
            return 'suspended'
    elif response.status_code == 404:
        return 'suspended'
    else:
        return 'unknown'

def main():
    with open('username.txt', 'r') as file:
        usernames = [line.strip() for line in file]

    active_users = []
    suspended_users = []

    for username in usernames:
        status = check_instagram_username_status(username)
        if status == 'active':
            active_users.append(username)
        elif status == 'suspended':
            suspended_users.append(username)
        else:
            print(f"Could not determine the status of username: {username}")

    print(f"{Fore.GREEN}ACTIVE USERS =")
    for username in active_users:
        print(f"{Fore.GREEN}{username}")

    print(f"\n{Fore.RED}SUSPENDED USERS =")
    for username in suspended_users:
        print(f"{Fore.RED}{username}")


    print("\n©️𝑻𝑯𝑰𝑺 𝑪𝑶𝑫𝑬 𝑴𝑨𝑲𝑬𝑫 𝑩𝒀 @𝑳𝒐𝒕𝒎𝒂𝒙𝑫𝒆𝒗")

    with open('active.txt', 'w') as file:
        for username in active_users:
            file.write(username + '\n')

    with open('suspend.txt', 'w') as file:
        for username in suspended_users:
            file.write(username + '\n')

if __name__ == "__main__":
    main()
