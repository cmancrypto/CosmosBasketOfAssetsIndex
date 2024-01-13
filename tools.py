from config import coingecko_endpoint, history_endpoint, coingecko_api_key
import pandas as pd
import requests
import datetime


def get_coingecko_history_data(date, coin_name, api_key=None):
    # construct the history endpoint from the config endpoint
    constructed_endpoint = f"{coingecko_endpoint}{coin_name}{history_endpoint}"
    # params recieve the formatted date dd-mm-yyyy
    params = {
        "date": date
    }

    # Include API key in headers if provided
    headers = {}
    if api_key:
        headers['x-cg-demo-api-key'] = api_key

    # Make the API request
    response = requests.get(constructed_endpoint, params=params, headers=headers)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        if response_data:
            return response_data
        else:
            print(f"No data available for {coin_name} on {date}")
    else:
        print(f"Error {response.status_code}: {response.text}")


def get_market_cap_usd_from_history_data(response_data):
    ##gets the market cap from the coingecko response.json()
    market_cap = response_data['market_data']['market_cap']['usd']
    return market_cap


def get_price_usd_from_history_data(response_data):
    ##gets the price from the coingecko response.json()
    price = response_data["market_data"]["current_price"]["usd"]
    return price


def format_date_for_API_query(date: datetime.datetime) -> str:
    ##formats the datetime.datetime format to the dd-mm-yyyy that the coingecko API needs
    formatted_date = date.strftime("%d-%m-%Y")
    return formatted_date


def get_coins_market_cap(formatted_date: str, coinlist: list) -> dict:
    """using formatted date and a list of coingecko coin names,
     calls the coingecko API and returns a dict which are name:market cap"""

    ##initialise an empty dict to hold coin_name: market cap pairs)
    market_caps = {}
    #iterate through the list of coins
    for coin in coinlist:

        history_data = get_coingecko_history_data(formatted_date, coin, coingecko_api_key)
        market_caps[coin] = get_market_cap_usd_from_history_data(history_data)
    return market_caps


def get_coins_price(formatted_date: str, coinlist: list) -> dict:
    """using formatted date and a list of coingecko coin names,
     calls the coingecko API and returns a dict of name:price pairs"""
    prices = {}
    for coin in coinlist:
        history_data = get_coingecko_history_data(formatted_date, coin, coingecko_api_key)
        prices[coin]=get_price_usd_from_history_data(history_data)

    return prices


def get_coin_prices_for_date_list(datelist: list[datetime.datetime], coinlist: list) -> list:
    ##iterates through the datelist, calling the get_list_coins_price function for each - returns a list of dict of date:price
    date_prices = []
    for date in datelist:
        formatted_date = format_date_for_API_query(date)
        list_of_prices = get_coins_price(formatted_date, coinlist)
        date_coinlist_dict = {formatted_date:list_of_prices}
        date_prices.append(date_coinlist_dict)
    return date_prices


def get_coin_market_caps_for_date_list(datelist: list[datetime.datetime], coinlist: list) -> list:
    ##iterates through the datelist, calling the get_list_coins_price function for each - returns a list of dict of date:price
    date_market_caps = []
    for date in datelist:
        formatted_date = format_date_for_API_query(date)
        list_of_market_caps = get_coins_market_cap(formatted_date, coinlist)
        date_coinlist_dict = {formatted_date: list_of_market_caps}
        date_market_caps.append(date_coinlist_dict)
    return date_market_caps

def df_from_list_dicts(list_of_dicts:list[dict]):
    all_dataframes=[]
    for date_dict in list_of_dicts:
        df = pd.DataFrame(date_dict)
        all_dataframes.append(df)
    result = pd.concat(all_dataframes, axis=1, join="inner")
    return result





##test data
#coin_names = ["akash-network", "juno-network", "kujira", "fetch-ai", "evmos", "stargaze", "persistence"]
#dates = [datetime.datetime(2024, 1, 1),datetime.datetime(2023, 1, 1)]

#print(get_coin_market_caps_for_date_list(dates, coin_names))
#print(get_coin_prices_for_date_list(dates,coin_names))
