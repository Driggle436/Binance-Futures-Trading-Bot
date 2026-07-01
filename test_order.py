from bot.orders import place_order

try:
    response = place_order(
        symbol="BTCUSDT",
        side="BUY",
        order_type="MARKET",
        quantity=0.001,
    )

    print("Order placed successfully!")
    print(response)

except Exception as e:
    print("Error:")
    print(e)