# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore accounts (https://www.gillexplore.ie/).

## How does this work?
Generates a random sequence of letters tested for validity and if valid, redeems onto your account. This does mean it is basically bruteforcing a code, which makes validity slow. The script grabs your cookie data for Gill Explore automatically and uses it as the authentication to redeem the codes.

## Requirements
You will need Windows 10 or above, Python 3+, the Firefox browser and the browser-cookie3 library.

Install Firefox from https://www.mozilla.org/en-GB/firefox/download/thanks/  
Install Python from https://www.python.org/downloads/  
Install browser-cookie3 for Python in your terminal with:
```
pip install browser-cookie3
```
## Instructions
1. Download and install the latest version of Python from the link above **(Remember to add Python to PATH)**
2. Open your terminal and enter 'pip install browser-cookie3' (if pip isn't found as a command, reinstall Python as PATH or reboot)
3. Download and install Firefox from the link above
4. Log into your Gill Explore account in Firefox and click 'My Profile'
5. Run the script

## Features
- Automatically grabs the auth cookie from your browser
- Checks for any validation issues before generation
- Outputs any valid codes into "success.txt"
- Fast generation and no found rate-limiting
## Issues
~~Requires you to keep your browser closed~~ Fixed in v1.1.0
