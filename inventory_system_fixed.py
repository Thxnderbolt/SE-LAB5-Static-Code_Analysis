"""
Inventory management system for tracking stock items.
"""
import json


stock_data = {}


def add_item(item, quantity, logs=None):
    """Add an item to inventory with specified quantity."""
    if logs is None:
        logs = []
    stock_data[item] = quantity
    logs.append(f"Added {item}: {quantity}")


def remove_item(item):
    """Remove an item from inventory."""
    try:
        if item in stock_data:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Get the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(filename='inventory.json'):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}


def save_data(filename='inventory.json'):
    """Save inventory data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(stock_data, f)


def print_data():
    """Print all inventory items."""
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def check_low_items(threshold=10):
    """Check and print items below threshold quantity."""
    low_items = []
    for item, qty in stock_data.items():
        if qty < threshold:
            low_items.append(item)
    return low_items


def main():
    """Main function to demonstrate inventory operations."""
    add_item("Apple", 50)
    add_item("Banana", 5)
    add_item("Orange", 30)
    save_data()
    print_data()
    # Removed dangerous eval() call


if __name__ == "__main__":
    main()