def add_item(current_cart, items_to_add):
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1

    return current_cart


def read_notes(notes):
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}

    for key in cart.keys():
        fulfillment_cart[key] = [cart[key]] + aisle_mapping[key]

    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    for key, values in fulfillment_cart.items():
        store_inventory[key][0] = store_inventory[key][0] - values[0]
        if store_inventory[key][0] == 0:
            store_inventory[key][0] = "Out of Stock"

    return store_inventory
