import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Create Binance client
client = Client(API_KEY, API_SECRET)

# Use Binance Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"