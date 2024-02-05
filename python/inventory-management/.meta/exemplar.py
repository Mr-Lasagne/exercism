def create_inventory(items):
    inventory = {}
    add_items(inventory, items)
    return inventory


def add_items(inventory, items):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    output = []
    for item in sorted(inventory.items()):
        if item[1] > 0:
            output.append(item)
    return output
