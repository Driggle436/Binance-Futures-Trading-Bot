import time
from binance.enums import TIME_IN_FORCE_GTC

from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"REQUEST -> Symbol={symbol}, Side={side}, Type={order_type}, Qty={quantity}, Price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = TIME_IN_FORCE_GTC

        response = client.futures_create_order(**params)

        # Wait briefly for Binance to update the order
        time.sleep(1)

        order = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"]
        )

        logger.info(f"RESPONSE -> {order}")

        return order

    except Exception as e:
        logger.exception(e)
        raise

def get_recent_orders(symbol, limit=5):
    """
    Fetch recent orders for a symbol.
    """

    try:
        orders = client.futures_get_all_orders(
            symbol=symbol,
            limit=limit
        )

        logger.info(f"Fetched {len(orders)} recent orders")

        return orders

    except Exception as e:
        logger.exception(e)
        raise