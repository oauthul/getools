# GETools made by oauthul
# -*- coding: utf-8 -*-

import subprocess
import requests
import browser_cookie3
import time
import random
import string
import os
import sys
import platform
from tqdm import tqdm

version = "1.2.0"

def load_cookie_test():
    try:
        firefox_cookies = browser_cookie3.firefox(domain_name="gillexplore.ie")
        if firefox_cookies is None:
            print('[ERROR] | No cookies were found. Have you opened Firefox?')
            return 1
        else:
            cookieload = str(firefox_cookies)
            if 'AWSALBCORS' in cookieload:
                print('[OK] | Authentication cookies found in Firefox.')
                time.sleep(.5)
                return 0
            else:
                input('[ERROR] No authentication for Gill Explore was found. Please check if you are logged in.\n\n[INFO] | Press ENTER when you are logged in.. ')
                time.sleep(2)
    except TypeError:
        input('\n[FAIL] | There are no detectable cookies in Firefox. Please open Firefox and log in.\n\n[INFO] | Press ENTER when you are logged in.. ')
        prerequisites()
    except browser_cookie3.BrowserCookieError:
        input('[ERROR] | Profile cannot be found. Script will attempt to reinstall Firefox.\n\n[INFO] | Press ENTER to continue.. ')
        firefox_installer(reinstall=True)

def download_firefox():
    try:
        url = "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US"
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        with open("FirefoxInstaller.exe", 'wb') as file, \
             tqdm(
                total=total_size,
                ncols=100,
                bar_format='{percentage:3.0f}%|{bar:10}|',
                leave=False
             ) as progress_bar:
            
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                progress_bar.update(size)
        return 0
    except Exception as e:
        input(f'[ERROR] | Failed to download Firefox: {str(e)}\n\n[INFO] | Press ENTER to continue.. ')
        return 1

def firefox_install_test(quiet=False):
    is_firefox_installed = subprocess.run('powershell.exe Get-Package *Firefox*', shell=True,text=True,capture_output=True)
    if "Firefox" in is_firefox_installed.stdout:
        if not quiet:
             print('[OK] | Firefox is installed')
        return 1
    else:
        if not quiet:
             print('[FAIL] | Firefox is not installed')
        return 2

def activate_ebook(code):
    firefox_cookies = browser_cookie3.firefox(domain_name="gillexplore.ie")
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

def firefox_installer(reinstall=False):
    is_firefox_installed = None
    if not reinstall:
        is_firefox_installed = firefox_install_test(quiet=True)
    if is_firefox_installed == 1:
        print('[OK] | Firefox is installed')
        time.sleep(1)
    elif reinstall == True or is_firefox_installed == 2:
        ask_for_install = None
        if not reinstall:
            ask_for_install = input("[INFO] | Firefox isn't installed, do you want the script to install it now? (y/n) ")
        if reinstall == True or ask_for_install == 'y':
            print('\n[INFO] | Downloading Firefox..')
            firefox_installer_default = None
            firefox_installer_customise = None
            download_latest_firefox = download_firefox()
            if download_latest_firefox == 0:
                print('[OK] | Latest version of Firefox downloaded.')
                if not reinstall:
                    customise_install = input("[INFO] | Do you want the script to install Firefox automatically? (y/n) ")
                if reinstall == True or customise_install == 'y':
                    print('[INFO] | Installing Firefox to defaults, please press "Yes" to the UAC prompt..')
                    firefox_installer_default = subprocess.call(args='FirefoxInstaller.exe /S')
                elif customise_install != "y":
                    print('[INFO] | Running Firefox installer, please press "Yes" to the UAC prompt..')
                    firefox_installer_customise = subprocess.call(args='FirefoxInstaller.exe')
                try: 
                    if (firefox_installer_customise is not None and firefox_installer_customise == 0) or (firefox_installer_default is not None and firefox_installer_default == 0):
                        print('[OK] | Completed installer. Deleting installer file..')
                        os.remove('FirefoxInstaller.exe')
                        print('[INFO] | Checking if Firefox is installed properly..')
                        return_test = firefox_install_test(quiet=True)
                        if return_test != 1:
                            input(f"[ERROR] | Unsuccessful install. Can't continue script with Firefox not installed\n\n- | Press ENTER to continue.. ")
                            sys.exit()
                        else:
                            print('[OK] | Install was successful..')
                            return 0
                except UnboundLocalError:
                    print(firefox_installer_customise)
                    print(firefox_installer_default)
                    input('[ERROR] | Failed to check if install was successful.\n\n[INFO] | Press ENTER to continue.. ')
        elif ask_for_install != 'y'or ask_for_install == "":
             input('[INFO] | Please install Firefox from the link in the GitHub.\n\n[INFO] | Press ENTER to exit.. ')
             sys.exit('[INFO] | User declined to install Firefox automatically.')
                     

def prerequisites():
    os.system('cls||clear')
    print(f'GETools {version} | Prerequisites\n')
    # Check if the script is run on Windows
    if platform.system() == "Windows":
        print('[OK] | Running on Windows')
    elif platform.system() != "Windows":
        input(f"[ERROR] | Incorrect OS/Architecture. This program only works on Windows for now. You are currently on {platform.system()}. ")
        sys.exit()
    # Check if Firefox is installed, otherwise install automatically
    check_if_firefox_is_installed = firefox_installer(reinstall=False)
    if check_if_firefox_is_installed == 0:
        print('[OK] | Completed installer.')
    # Check for any cookies in Firefox
    cookie_check_value = load_cookie_test()
    if cookie_check_value == 0:
        print('[OK] | Successful Firefox cookie check.')
        time.sleep(.5)
    validate()

def generate_code():
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(7))

def main_exec(clear=True):
        try:
            if clear == True:
                os.system('cls||clear')
            if auth_response.status_code == 200:
                print(f"\n[OK] | Successfully accessed the page, status code: {auth_response.status_code}")
                if "Logout" and "My Profile" and "not exist" in auth_response.text:
                    print("[OK] | Appears to be logged in and returned a successful e-book validation test\n")
                    cookies()
                    input('\n[INFO] | Press ENTER to begin e-book generation.. ')
                    os.system('cls||clear')
                    while True:
                        # Generate and return the tested code, with its status code
                            generated_code = f"GRC{generate_code()}"
                            retest = activate_ebook(f"{generated_code}")
                            # "eBook has been activated!"" is the expected return for a successful code. If this isn't returned, it's invalid.
                            if "Logout" in retest.text and 'not exist' in retest.text:
                                    print('[FAIL] | Invalid code\n-----------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code if 200 else 'KO [Rate-limit?]'} OK')
                                    time.sleep(0.5)
                                    os.system('cls||clear')
                            # When "eBook has been activated" is found, it will output the HTML data to a file so you can read which ebook was redeemed
                            elif 'Logout' in retest.text and 'eBook has been activated' in retest.text:
                                    print('[SUCCESS] | Successful code found\n-----------------------')
                                    print(f'• Tested Code: {generated_code}')
                                    print(f'• Status Code: {retest.status_code if 200 else 'KO [Rate-limit?]'} OK')
                                    time.sleep(.5)
                                    print('[INFO] | Outputting full HTML data to a file..')
                                    with open("success.txt", "a") as successful:
                                        successful.write(f"\nSuccessful code found, {generated_code}\nHTML Data:\n" + retest.text)
                                    print('[OK] | Completed, resuming script...')
                                    time.sleep(5)
                                    os.system('cls||clear')
                else:
                    print("[WARN] | Doesn't appear to be logged in")
                    input("[ERROR] | Cannot run the e-book generation while logged out\n\n[INFO] | Press ENTER to try again.. ")
                    validate()
            else:
                print(auth_response.text)
                input(f"[FAIL] | Failed to access the page. Status code: {auth_response.status_code if auth_response else 'N/A'}\n\n[INFO] | Press ENTER to try again.. ")
                validate()
        except Exception as e:
            print(f'\n[ERROR] | Exception occurred: {e}\n\n[INFO] | Press ENTER to try again.. ')
            validate()
def validate():
    try:
        os.system('cls||clear')
        print(f'GETools {version} | Validation Test\n')
        print('[INFO] | Attempting a redemption request to "gillexplore.ie" to test for issues with validation.')
        print('[INFO] | Trying code: "GRCxxxxxxx"')
        global auth_response
        auth_response = activate_ebook("GRCxxxxxxx")
        time.sleep(.5)
        main_exec(clear=False)
    except PermissionError:
        input('[FAIL] | Script has failed to grab the cookies from Firefox. Is Firefox installed?\n\n[INFO] | Press ENTER to try again.. ')
        validate()
    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] |  An error occurred while trying to redeem with requests library.")
        input('\n[WARN] | Check if you can access www.gillexplore.ie in Firefox.\n\n[INFO] | Press ENTER to try again.. ')
        validate()
    except TypeError:
        input('[ERROR] | Failed to redeem. Are you properly logged into Gill Explore?\n\n[INFO] | Press ENTER to continue.. ')
        validate()

# Main execution
if __name__ == "__main__":
    prerequisites()