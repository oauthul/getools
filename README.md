# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore accounts (https://www.gillexplore.ie/).

## How does this work?
Generates a random sequence of letters tested for validity and if valid, redeems onto your account. This does mean it is basically bruteforcing a code. The script grabs your cookie data for Gill Explore automatically and uses it as the authentication to redeem the codes.

## Requirements
You will need Windows 10 or above, Python 3+, the Firefox browser and the browser-cookie3 library.

Install Firefox from https://www.mozilla.org/en-GB/firefox/download/thanks/  
Install Python from https://www.python.org/downloads/  
Install browser-cookie3 for Python in your terminal with:
```
pip install browser-cookie3
```

## Features
- Automatically grabs the auth cookie from your browser
- Checks for any validation issues before generation
- Outputs any valid codes into "success.txt"
- Fast and no found rate-limiting
## Issues
~~- Requires you to keep your browser closed~~ Fixed in v1.1.0
