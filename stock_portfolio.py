
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        value = stocks[stock] * quantity
        total_investment += value

        print("Stock price:", stocks[stock])
        print("Investment value:", value)

    except ValueError:
        print("Please enter a valid quantity.")

print("\nTotal Investment Value:", total_investment)

save = input("Save result to a text file? (yes/no): ").lower().strip()

if save == "yes":
    with open("portfolio_result.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("Total Investment Value: " + str(total_investment))

    print("Result saved to portfolio_result.txt")