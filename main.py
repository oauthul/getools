# GETools made by oauthul
import subprocess
import requests
import browser_cookie3
import time
import random
import string
import os
import sys
import platform

def firefox_install_test():
    is_firefox_installed = subprocess.run('powershell.exe Get-Package *Firefox*', shell=True,text=True,capture_output=True)
    if "Firefox" in is_firefox_installed.stdout:
        return 1
    else:
        return 2
    
def firefox():
    global firefox_cookies
    firefox_cookies = browser_cookie3.firefox(domain_name="gillexplore.ie")
    cookieload = str(firefox_cookies)
    if 'AWSALBCORS' in cookieload:
        print('✓ | Cookies found in Firefox. Loading..')
        try:
            firefox_cookies
        except Exception as e:
            print(f'✗ | Error loading cookies: {e}')
            input('- | Press ENTER to continue. ')
        else:
            print('✓ | Cookies loaded successfully. Returning cookie values')
    else:
        print('✗ | No cookies found in Firefox.')
        exit()
    return firefox_cookies

def activate_ebook(code):
    global firefox_cookies
    firefox_cookies = browser_cookie3.firefox(domain_name="gillexplore.ie")
    if firefox_cookies is None:
        firefox()

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
    # Make the request
    response = session.post("https://www.gillexplore.ie/activate",data=m,headers=headers,cookies=firefox_cookies)
    return response

def cookies():
        for cookie in auth_response.cookies:
            print(f"• Cookie: {cookie.name} = {cookie.value}")

def prerequisites():
    print('GETools 1.x.x -- Prerequisites\n')
    if __name__ == "__main__":
        print('✓ | Running script from main.py')
    elif __name__ != "__main__":
        input("✗ | Importing the script can cause problems, try using the main file. ")
        sys.exit()
    if platform.system() == "Windows":
        print('✓ | Running on Windows')
    elif platform.system() != "Windows":
        input(f"✗ | Incorrect OS/Architecture. This program only works on Windows for now. You are currently on {platform.system()}. ")
        sys.exit()
    if firefox_install_test() == 1:
        print('✓ | Firefox is installed')
        time.sleep(.5)
        os.system('cls||clear')
    elif firefox_install_test() == 2:
        input("✗ | Firefox isn't installed ")
        sys.exit()

def generate_code():
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(7))

def main_exec():
        try:
            if auth_response.status_code == 200:
                print("\n✓ | Successfully accessed the page")
                if "Logout" and "My Profile" and "not exist" in auth_response.text:
                    print("✓ | Appears to be logged in and returned a successful e-book validation test\n")
                    cookies()
                    input('\n- | Press ENTER to begin e-book generation ')
                    os.system('cls||clear')
                    while True:
                        # Generate and return the tested code, with its status code
                            generated_code = f"GRC{generate_code()}"
                            retest = activate_ebook(f"{generated_code}")
                            # "eBook has been activated!"" is the expected return for a successful code. If this isn't returned, it's invalid.
                            if "Logout" in retest.text and 'not exist' in retest.text:
                                    print('✗ | Invalid code\n-----------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code} OK')
                                    time.sleep(0.5)
                                    os.system('cls||clear')
                            # When "eBook has been activated" is found, it will output the HTML data to a file so you can read which ebook was redeemed
                            elif 'Logout' in retest.text and 'eBook has been activated' in retest.text:
                                    print('✓ | Successful code found\n------------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code} OK')
                                    time.sleep(.5)
                                    print('- | Outputting all response data to a file..')
                                    with open("success.txt", "w") as fs:
                                        fs.write(f"Successful code found, {generated_code}\n" + retest.text)
                                    print('✓ | Completed, resuming script...')
                                    time.sleep(5)
                                    os.system('cls||clear')
                else:
                    print("✗ | Doesn't appear to be logged in [are you logged in Firefox?]")
                    print(auth_response.text, auth_response.status_code)
                    failedlog = input("✗ | Cannot run the e-book generation while logged out\n\nRestart script? y/n ")
                    if failedlog == "y":
                         os.system('cls||clear')
                         os.system('python main.py')
            else:
                print(auth_response.text)
                failedaccess = input(f"✗ | Failed to access the page. Status code: {auth_response.status_code if auth_response else 'N/A'}\n\nRestart script? y/n ")
                if failedaccess == "y":
                     os.system('cls||clear')
                     os.system('python main.py')
        except Exception as e:
            print(f'\nException occurred: {e}')

# Main execution
print('GETools version 1.x.x\n')
print('- | Starting prerequisites in 3 seconds.')
time.sleep(1)
print('- | Starting prerequisites in 2 seconds.')
time.sleep(1)
print('! | Starting prerequisites in 1 second!')
time.sleep(1)
os.system('cls||clear')
prerequisites()

# Validation Test
try:
    print('GETools 1.x.x -- Validation Test\n')
    print('- | Attempting a request to "gillexplore.ie" to test validation.')
    print('- | Trying code: GRCxxxxxxx')
    auth_response = activate_ebook("GRCxxxxxxx")
    time.sleep(.5)
    main_exec()
except PermissionError:
    input('! | Script has failed to grab the cookies from Firefox. Is Firefox installed?\n\n\nPress ENTER to continue. ')
    sys.exit()
except requests.exceptions.RequestException as e:
    print(f"\n✗ |  An error occurred:\n{e}")
    input('\n✗ | Check if you can access www.gillexplore.ie in Firefox.\n\n\nPress ENTER to continue. ')
    sys.exit()