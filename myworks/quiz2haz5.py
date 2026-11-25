def calculate_warehouse(stock_dict):
    total = 0
    expensive = None
    expensive_item = None
    for item, info in stock_dict.items():
        price, qty = info
        total = total + (price * qty)
        if expensive is None or stock_dict[item][0] > expensive:
            expensive = stock_dict[item][0]
            expensive_item = item
    return total, expensive_item

warehouse = {
    "Keyboard": (800, 4),
    "Mouse": (400, 10),
    "Monitor": (5000, 2)
}

total_val, most_expensive = calculate_warehouse(warehouse)
print(f"Total Value: {total_val}, Most Expensive: {most_expensive}")