# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore accounts (https://www.gillexplore.ie/).
## How does this work?
Generates a random sequence of letters tested for validity and if valid, redeems onto your account. This does mean it is basically bruteforcing a code, which makes validity slow, but there is little rate-limiting (from testing). The script grabs your cookie data for Gill Explore automatically and uses it as the authentication to redeem the codes. 
## Requirements
You need Python 3.3 or above.
Install Python in your operating system from their website: https://www.python.org/downloads/ (Install Python to the PATH in the installation menu)
## Instructions
1. Download and install the latest version of Python from the link above
2. Navigate to the GETools directory in your terminal and install the libraries with `pip install -r requirements.txt`
3. Log into your Gill Explore account in your desired browser
4. Run the script
## Features
- Automatically grabs the auth cookie from your browser
- Outputs any valid codes (with its HTML output) into "successful_codes.txt"
- Fast generation and avoids rate-limiting
- Avoids generating any pre-generated codes and writes them to "failed_codes.txt"
- Supports most browsers
- Debug mode
## Issues
~~Requires you to keep your browser closed~~ (Fixed in v1.1.0)

~~Required to use Firefox to use the program~~ (Fixed in v2.0.0)
## Plans
- [x] Remove the issue of keeping browsers closed (Added in v1.1.0)
- [x] Remove the issue of only being able to use Firefox (Added in v2.0.0) 
- [X] Add Linux and MacOS functionality (Added in v2.0.0)
## Debug Mode
To see how the program functions, you can enable debug mode. This is done by changing `getools_logs.setLevel(logging.INFO)` to `getools_logs.setLevel(logging.DEBUG)` at the top of the script.
## Credits
Rookie library - (https://pypi.org/project/rookiepy)

BeautifulSoup library - (https://pypi.org/project/beautifulsoup4)

Requests library - (https://pypi.org/project/requests)

PyUAC library - (https://github.com/Preston-Landers/pyuac)
## Why?
To learn Python.
