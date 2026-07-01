# Binance Futures Testnet Trading Bot

A Python-based trading bot that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**. The application features a clean CLI, input validation, structured logging, exception handling, and a modular codebase.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL**
- Input validation
- Exception handling
- Logging of API requests and responses
- Clean modular architecture
- Rich CLI interface (Bonus)
- View recent orders (Bonus)

---

## Project Structure

```
TradingBot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Requirements

- Python 3.10 or above
- Binance Futures Testnet (Demo Trading) account
- API Key and Secret

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/TradingBot.git
cd TradingBot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

### View Recent Orders

Run:

```bash
python cli.py
```

Select:

```
2
```

Then enter the trading symbol.

Example:

```
BTCUSDT
```

---

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

---

## Validation

The application validates:

- Symbol
- Side (BUY / SELL)
- Order Type (MARKET / LIMIT)
- Quantity
- Price (required for LIMIT orders)

---

## Error Handling

The application handles:

- Invalid user input
- Binance API errors
- Network errors
- Missing required parameters

---

## Bonus Features

- Rich CLI Interface using `rich`
- Recent Order History
- Structured logging
- Modular project structure

---

## Assumptions

- The user has an active Binance Futures Demo/Testnet account.
- API credentials are stored securely in a `.env` file.
- Orders are placed on the USDT-M Futures Testnet.

---

## Sample Output

### Market Order

```
ORDER REQUEST
Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.001

ORDER RESPONSE
Status        : FILLED
Executed Qty  : 0.0010
Average Price : 60137.20
```

### Limit Order

```
Status : NEW
```

This indicates the order has been accepted and is waiting to be filled.

---

## Author

**Piyush Kumar**