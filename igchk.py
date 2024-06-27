import requests
from bs4 import BeautifulSoup

def check_instagram_account(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find('meta', property="og:description"):
            return "active"
        else:
            return "suspended"
    elif response.status_code == 404:
        return "suspended"
    else:
        return "error"

def check_accounts_from_file(filename):
    with open(filename, 'r') as file:
        usernames = [line.strip() for line in file]

    active_users = []
    suspended_users = []

    for username in usernames:
        status = check_instagram_account(username)
        if status == "active":
            active_users.append(username)
        elif status == "suspended":
            suspended_users.append(username)
        else:
            print(f"Error checking account: {username}")

    return active_users, suspended_users

if __name__ == "__main__":
    filename = input("Enter the filename containing Instagram usernames: ")
    active_users, suspended_users = check_accounts_from_file(filename)

    print("\nActive Users:")
    for user in active_users:
        print(user)

    print("\nSuspended Users:")
    for user in suspended_users:
        print(user)

    # Optionally, save results to files
    with open('active_users.txt', 'w') as file:
        for user in active_users:
            file.write(f"{user}\n")

    with open('suspended_users.txt', 'w') as file:
        for user in suspended_users:
            file.write(f"{user}\n")
