import os
from dotenv import load_dotenv


load_dotenv()
##need to configure coingecko_api_key in .env with a demo public API key
coingecko_api_key = os.getenv("coingecko_api_key")

coingecko_endpoint =f"https://api.coingecko.com/api/v3/coins/"
##history endpoint syntax is {coin_name}/history
history_endpoint = f"/history"
