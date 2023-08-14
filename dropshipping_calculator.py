def calculate_profit(selling_price, cost_price, shipping_cost, quantity):
    total_cost = (cost_price + shipping_cost) * quantity
    total_revenue = selling_price * quantity
    profit = total_revenue - total_cost
    return profit

print("Dropshipping Profit Calculator")

while True:
    try:
        selling_price = float(input("Enter the selling price per unit: "))
        cost_price = float(input("Enter the cost price per unit: "))
        shipping_cost = float(input("Enter the shipping cost per unit: "))
        quantity = int(input("Enter the quantity: "))
        
        profit = calculate_profit(selling_price, cost_price, shipping_cost, quantity)
        
        print(f"Potential Profit: ${profit:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

    choice = input("Do you want to calculate another profit? (yes/no): ")
    if choice.lower() != "yes":
        print("Goodbye!")
        break
