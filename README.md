# luno-api

A python SDK for the Luno bitcoin exchange API

[Luno](https://www.luno.com/) is a South African-based Bitcoin and Etherium exchange.  

## Usage 

    from luno_api import LunoApi
    api = LunoApi()
## API 

### Latest exchange rate 
    api.get_ticker()
## Includes 

Example script which prints the live exchange rate to the console every 10 seconds. 
