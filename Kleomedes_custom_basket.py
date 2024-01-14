from tools import get_coin_market_caps_for_date_list, df_from_list_dicts
import datetime

def get_Kleomedes_custom_basket_results(dates,coin_names,make_csv=False):
    # get the market caps for the dates and the coin list and print the results
    market_caps = get_coin_market_caps_for_date_list(dates, coin_names)
    #create the dataframe
    dataframes = df_from_list_dicts(market_caps)
    print(dataframes)
    dates = list(dataframes.columns)
    for date in dates:
        market_cap = dataframes[f"{date}"].sum()
        print(f"Kleo custom basket market cap at {date} is {market_cap}")
    if make_csv==True:
        dataframes.to_csv("custom_basket_results.csv")
    return dataframes


if __name__ == '__main__':
    print("Kleomedes Custom Basket")

    # these are the chains in the current Kleomedes custom basket
    ##coin_names = ["akash-network", "juno-network", "kujira", "fetch-ai", "evmos", "stargaze", "persistence","sentinel","cudos"]
    coin_names = ["akash-network","juno-network", "kujira", "fetch-ai", "evmos", "stargaze", "persistence", "sentinel",
                  "cudos"]


    # dates in datetime.datetime(YYYY, MM, DD) format
    dates = [datetime.datetime(2023, 12, 29), datetime.datetime(2023, 2, 3)]

    #call the function to run the script
    get_Kleomedes_custom_basket_results(dates,coin_names,make_csv=True)


