# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore accounts (https://www.gillexplore.ie/).
## How does this work?
Generates a random sequence of letters tested for validity and if valid, redeems onto your account. This does mean it is basically bruteforcing a code, which makes validity slow, but there is no rate-limiting (from testing). The script grabs your cookie data for Gill Explore automatically and uses it as the authentication to redeem the codes. 
## Requirements
You will need Windows 10 or above, Python 3+, the Firefox browser and the browser-cookie3 library for Python.

Install Firefox from https://www.mozilla.org/en-GB/firefox/download/thanks/  
Install Python from https://www.python.org/downloads/  
Install browser-cookie3 for Python in your terminal with:
```
pip install browser-cookie3
```
You may need C++ Build Tools to install browser-cookie3. To do so, download the executable from https://visualstudio.microsoft.com/visual-cpp-build-tools/ and run the following command in Powershell. Note: The installation is over 2GB+.
```
vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools
```
## Instructions
1. Download and install the latest version of Python from the link above **(Remember to add Python to PATH)**
2. Open your terminal and enter 'pip install browser-cookie3' (if pip isn't found as a command, reinstall Python with PATH or reboot)
3. Download and install Firefox from the link above
4. Log into your Gill Explore account in Firefox
5. Run the script
## Features
- Automatically grabs the auth cookie from Firefox
- Checks for any validation issues before generation
- Outputs any valid codes into "success.txt"
- Fast generation and no noticed rate-limiting
## Issues
~~Requires you to keep your browser closed~~ Fixed in v1.1.0
## Plans
- [x] Remove the issue of keeping browsers closed (Added in v1.1.0)
- [X] Inbuilt Firefox installer (Added in v1.2.0)
- [ ] Add Linux and MacOS functionality
## Why?
To learn Python, and boredom
