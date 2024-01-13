# CosmosBasketOfAssetsIndex
Scripts in Python to create indices to track COSMOS altcoin performance against


Allows for getting the price basis for an index at any point in time using the CoinGecko Price API



Example usage include assessing outperformance of the COSMOS altcoin market 
Includes: KleomedesCustomBasket and a simulation of IBCX 

KleomedesCustomBasket: MarketCap based index of Cosmos altcoins - allows for tracking performance against a basket of assets weighted by market cap 

IBCXIndex: Grants access to historical IBCX prices based on definition of IBCX tokens and weighting. Allows for getting historical data, even if there's future changes to index coins/weights. 


To use: 

Install packages from requirements.txt

Include a public DEMO API KEY from Coingecko in the example.env file and rename to .env 

