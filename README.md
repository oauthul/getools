# GETools - Simple e-book generator and validator
Generates and Validates e-book codes for Gill Explore (https://gillexplore.ie/). Requires you to be logged in to Gill Explore as a requirement.

## How does this work?
Generates a random sequence of letters that redeem onto your account. This does mean it is basically bruteforcing a code. The script grabs your cookie data for Gill Explore and uses it as the authentication to redeem the codes.

## Requirements
A windows machine, browser-cookie3 and to be logged into Gill Explore on any browser before launch. Install browser-cookie3 with:
```
pip install browser-cookie3
```
in your terminal.
