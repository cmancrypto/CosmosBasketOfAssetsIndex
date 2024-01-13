from tools import get_coins_price, format_date_for_API_query
import datetime

class IBCXAsset:
    ##class with coingecko_name and weights
    def __init__(self,coingecko_name,weight):
        self.coingecko_name=coingecko_name
        #weight is token count in the IBCX pool
        self.weight=weight


def get_weighted_prices(asset_list, date : datetime.datetime):
    coin_names = []

    for asset in asset_list:
        coin_names.append(asset.coingecko_name)
    formatted_date = format_date_for_API_query(date)
    prices = get_coins_price(formatted_date, coin_names)

    weighted_prices = []
    weighted_prices_sum = 0
    for asset in asset_list:
        weighted_price = prices[asset.coingecko_name] * asset.weight
        weighted_prices.append(weighted_price)
        weighted_prices_sum = weighted_prices_sum + weighted_price

    return weighted_prices_sum

if __name__ == '__main__':
    print(f"IBCX historical price estimate")

##this is the current set up of the IBCX index
asset_list = [IBCXAsset("osmosis",29.8912),IBCXAsset("cosmos",2.2524),IBCXAsset("akash-network",4.9391),IBCXAsset("stargaze",160.2985),IBCXAsset("juno-network",11.1186), IBCXAsset("secret",7.6466),IBCXAsset("stride",0.4433), IBCXAsset("evmos",12.7267), IBCXAsset("axelar",1.1723), IBCXAsset("regen", 7.9257), IBCXAsset("ion",0.001), IBCXAsset("umee",101.868)]


#date in datetime.datetime  YYYY, MM, DD
date=datetime.datetime(2024, 1, 13)

print(f"IBCX index price for {date} is: {get_weighted_prices(asset_list,date)}")

