import argparse

from bot.orders import place_order, get_recent_orders
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# =========================
# Main Menu
# =========================

console.print(
    Panel.fit(
        "[bold magenta]Binance Futures Trading Bot[/bold magenta]",
        border_style="cyan",
    )
)

console.print("[1] Place Order")
console.print("[2] View Recent Orders")

choice = input("\nEnter your choice: ")

# =========================
# Recent Orders
# =========================

if choice == "2":

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()

    try:

        orders = get_recent_orders(symbol)

        table = Table(title="Recent Orders")

        table.add_column("Order ID", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Side", style="yellow")
        table.add_column("Type", style="blue")
        table.add_column("Qty", style="magenta")
        table.add_column("Avg Price", style="red")

        for order in orders[-5:]:

            table.add_row(
                str(order["orderId"]),
                order["status"],
                order["side"],
                order["type"],
                order["origQty"],
                order.get("avgPrice", "-"),
            )

        console.print(table)

    except Exception as e:

        console.print(f"[bold red]Error:[/bold red] {e}")

    exit()

# =========================
# Place Order
# =========================

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    price = None

    if order_type == "LIMIT":

        if args.price is None:
            raise ValueError("LIMIT order requires --price")

        price = validate_price(args.price)

    # =========================
    # Order Request
    # =========================

    console.print(
        Panel.fit(
            "[bold cyan]ORDER REQUEST[/bold cyan]",
            border_style="green",
        )
    )

    request_table = Table(title="Order Details")

    request_table.add_column("Field", style="cyan")
    request_table.add_column("Value", style="green")

    request_table.add_row("Symbol", symbol)
    request_table.add_row("Side", side)
    request_table.add_row("Type", order_type)
    request_table.add_row("Quantity", str(quantity))

    if price:
        request_table.add_row("Price", str(price))

    console.print(request_table)

    # =========================
    # Place Order
    # =========================

    response = place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )

    # =========================
    # Order Response
    # =========================

    console.print(
        Panel.fit(
            "[bold cyan]ORDER RESPONSE[/bold cyan]",
            border_style="blue",
        )
    )

    response_table = Table(title="Order Response")

    response_table.add_column("Field", style="cyan")
    response_table.add_column("Value", style="yellow")

    response_table.add_row("Order ID", str(response["orderId"]))
    response_table.add_row("Status", response["status"])
    response_table.add_row("Executed Qty", response["executedQty"])
    response_table.add_row(
        "Average Price",
        str(response.get("avgPrice", "N/A")),
    )

    console.print(response_table)

    console.print(
        "\n[bold green]✓ ORDER PLACED SUCCESSFULLY[/bold green]"
    )

except Exception as e:

    console.print(f"\n[bold red]✗ FAILED[/bold red]\n{e}")