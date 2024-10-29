# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore (https://www.gillexplore.ie). Requires you to be logged in to Gill Explore.

## How does this work?
Generates a random sequence of letters that redeem onto your account. This does mean it is basically bruteforcing a code. The script grabs your cookie data for Gill Explore and uses it as the authentication to redeem the codes.

## Requirements
A Windows machine, browser-cookie3, and to be logged into your Gill Explore account on any browser. Install browser-cookie3 with:
```
pip install browser-cookie3
```
in your terminal.

## Features
- Automatically grabs the auth cookie from your browser
- Checks for any validation issues before generation
- Outputs any valid codes into "success.txt"
- Fast and no found rate-limiting
