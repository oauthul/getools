# Please be elevated, and install rookiepy, bs4 and requests.
from rookiepy import arc, firefox, opera, opera_gx, chrome, chromium, edge, vivaldi, brave, to_cookiejar
from bs4 import BeautifulSoup
import requests
import time
import random
import string
import os
import sys
import platform
import logging

getools_logs = logging.getLogger('getools')
# Set the logging level to logging.DEBUG to view debug info
getools_logs.setLevel(logging.INFO)

handler = logging.StreamHandler()
getools_logs.addHandler(handler)

version = "2.0.0"
browsers = {
    'Arc': arc,
    'Firefox': firefox,
    'Opera': opera,
    'Opera GX': opera_gx,
    'Chrome': chrome,
    'Chromium': chromium,
    'Edge': edge,
    'Brave': brave,
    'Vivaldi': vivaldi,
}

browsers_with_cookies = {}

def activate_ebook(code, browser_cookies):
    data = {
        'formID': 'ActivateEBook',
        'ActivateEBook': code
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.gillexplore.ie',
        'Referer': 'https://www.gillexplore.ie/dashboard',
    }

    session = requests.Session()
    response = session.post("https://www.gillexplore.ie/activate",data=data,headers=headers,cookies=browser_cookies)
    return response

def load_cookie_test():
    for browser_name, browser_func in browsers.items():
        try:
            check_cookie = browser_func(['gillexplore.ie'])
            if check_cookie:
                getools_logs.debug(f'[DEBUG]: Found browser with cookies: {browser_name}')
                cookie_jar = to_cookiejar(check_cookie)
                global test_activation
                test_activation = activate_ebook('GRCxxxxxx', cookie_jar)
                getools_logs.debug(f'[DEBUG]: Trying browser: {browser_name}')
                if test_activation.status_code != 200:
                    getools_logs.debug(f'[DEBUG]: Unable to access the website, skipping browser. Status code: {test_activation.status_code}')
                    continue
                else:
                    getools_logs.debug(f'[DEBUG]: Successfully accessed website. Status code: {test_activation.status_code}')
                soup = BeautifulSoup(test_activation.text, 'html.parser')
                login = soup.find('meta',attrs={'content': 'Login'})
                if not login:
                    browsers_with_cookies.update({browser_name:cookie_jar})
                    getools_logs.debug(f'[DEBUG]: Login cookie for {browser_name} found, adding to dictionary')
                else:
                    continue
                getools_logs.debug(f'[DEBUG]: Current available browsers: {list(browsers_with_cookies.keys())}')
        except RuntimeError:
            continue
    if len(browsers_with_cookies.keys()) > 1:
        print(f'[INFO]: Found more than one browser with GE login cookies, {list(browsers_with_cookies.keys())}')
        return random.choice(list(browsers_with_cookies.keys()))
    if len(browsers_with_cookies.keys()) == 0:
        getools_logs.debug(f'[DEBUG]: Available browser dictionary: {list(browsers_with_cookies.keys())}')
        print('[ERROR]: No browsers with GE login cookies found, or you are rate-limited.')
        return None
    else:
        return list(browsers_with_cookies.keys())[0]

def cookies():
    for cookie in test_activation.cookies:
        print(f"- Cookies: {cookie.name} = {cookie.value}")

def generate_code():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(7))
                     
def main_exec():
    try:
        getools_logs.debug(F'[DEBUG]: Comparing the received and expected status code')
        if test_activation.status_code == 200:
            print(f"[OK]: Successfully accessed the page, status code: {test_activation.status_code}\n")
            cookies()
            input('\n[INFO]: Press ENTER to begin code generation.. ')
            fail = open('failed_codes.txt', 'a+')
            if fail:
                getools_logs.debug(f'[DEBUG]: Opened "failed_codes.txt"')
            fail.seek(0)
            existing_codes = set(fail.read().splitlines())
            time.sleep(1)
            os.system('cls||clear')
            while True:
                print(f'-------- GETools {version}: Generation --------\n')
                generated_code = f"GRC{generate_code()}"
                if generated_code in existing_codes:
                    continue
                activate = activate_ebook(f"{generated_code}", browsers_with_cookies.get(browser_cookies))
                if 'not exist' or "Remaning activations" in activate.text:
                    print('[FAIL]: Invalid code redeemed\n-----------------------')
                    print(f'- Tested Code: {generated_code}')
                    print(f'- Status Code: {activate.status_code}')
                    print(f'- Current Browser: {browser_cookies}')
                    fail.write(generated_code + '\n')
                    print('- Wrote invalid code to failed_codes.txt')
                    time.sleep(0.5)
                    os.system('cls||clear')
                elif 'eBook has been activated' in activate.text:
                    print('[SUCCESS]: Successful code redeemed\n-----------------------')
                    print(f'- Tested Code: {generated_code}')
                    print(f'- Status Code: {activate.status_code}')
                    print(f'- Current Browser: {browser_cookies}')
                    time.sleep(.5)
                    print('[INFO]: Outputting full HTML data to a file..')
                    success_code = BeautifulSoup(activate.text, 'html.parser')
                    output = str(success_code.find_all(id='ActivateEBook'))
                    with open("successful_codes.txt", "a+") as successful:
                        successful.write(f"Successful code found, {generated_code}\nHTML Data:\n" + output + '\n\n\n')
                    print('[OK]: Completed, resuming script...')
                    time.sleep(5)
                    os.system('cls||clear')
        else:
            getools_logs.debug(F'[DEBUG]: Status code {test_activation.status_code} did not meet expectation of 200')
            input(f"[ERROR]: Failed to access the page. Status code: {test_activation.status_code}")
    except Exception as e:
        input(f'[ERROR]: Exception occurred: {e} (Status Code: {test_activation.status_code})')

def prerequisites():
    try:
        os.system('cls||clear')
        print(f'-------- GETools {version}: Prerequisites --------\n')
        check_os = platform.system()
        print(f'[OK]: Running on {check_os}')
        if check_os == 'Windows':
            getools_logs.debug(f'[DEBUG]: Checking for elevation (windows-only req). Will ask for manual elevation if not found.')
            import pyuac
            if pyuac.isUserAdmin() == False:
                input('[ERROR]: User is not elevated, please run the script with elevation')
                sys.exit()
            else:
                print('[OK]: User is elevated')
        global browser_cookies
        browser_cookies = load_cookie_test()
        if browsers_with_cookies:
            print(f'[OK]: Successful cookie check, selected "{browser_cookies}" as the browser')
            time.sleep(.5)
            main_exec()
        else:
            input('[ERROR]: Failed cookie check, please login before restarting.')
    except KeyboardInterrupt:
        sys.exit('\n[INFO]: Stopping script')
        
if __name__ == "__main__":
    prerequisites()
