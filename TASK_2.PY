# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# Dictionary to store the user's portfolio
portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Type 'done' when finished.\n")

# Input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠️ Invalid quantity. Please enter a number.")
        continue

    # Add to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
print("\n🧾 Portfolio Summary:")
total = 0
lines = []

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total += value
    line = f"{stock}: {quantity} x ${price} = ${value}"
    print(line)
    lines.append(line)

print(f"\n💰 Total Investment Value: ${total}")

# Ask to save results
save = input("Do you want to save the result to a file? (y/n): ").lower()
if save == 'y':
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for line in lines:
            file.write(line + "\n")
        file.write(f"\nTotal Investment Value: ${total}\n")
    print("📁 Saved to 'portfolio.txt'.")
