"""
Inventory management system for tracking stock items.
"""
import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to inventory with specified quantity."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove specified quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Get the quantity of a specific item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    with open(file, "r", encoding='utf-8') as f:
        global stock_data
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print all inventory items."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Check and return items below threshold quantity."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() call - originally: eval("print('eval used')")


if __name__ == "__main__":
    main()
