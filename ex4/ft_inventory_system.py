import sys

if __name__ == "__main__":
	print("=== Inventory System Analysis ===")
	print()

	inventory = {}

	for arg in sys.argv[1:]:
		parts = arg.split(":")

		if len(parts) != 2:
			print(f"Error - invalid parameter '{arg}'")
			continue

		item = parts[0]
		quantity = parts[1]

		if item in inventory:
			print(f"Redundant item '{item}' - discarding")
			continue

		try:
			quantity = int(quantity)
			inventory.update({item: quantity})
		except ValueError as err:
			print(f"Quantity error for '{item}': {err}")
	print()
	print(f"Got inventory: {inventory}")
	print()
	items = list(inventory.keys())
	print(f"Item list: {items}")
	print()
	total = sum(list(inventory.values()))
	print(f"Total quantity of the {len(items)} items: {total}")
	print()
	for item in items:
		percentage = round(inventory[item] / total * 100, 1)
		print(f"Item {item} represents {percentage}%")
	print()
	most_item = items[0]
	least_item = items[0]
	for item in items:
		if inventory[item] > inventory[most_item]:
			most_item = item
		if inventory[item] < inventory[least_item]:
			least_item = item
	print(
		f"Item most abundant: {most_item} "
		f"with quantity {inventory[most_item]}")
	print(
		f"Item least abundant: {least_item} "
		f"with quantity {inventory[least_item]}"
    	)
	print()
	inventory.update({"magic_item": 1})
	print(f"Updated inventory: {inventory}")