class Item():
    def __init__(self, name, cost):
        self.name = name    # Name of item (string)
        self.cost = cost    # Cost of item in dollars (integer)

    def __str__(self):
        return self.name + " ($" + str(self.cost) + ")"

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost


class ItemCount():
    def __init__(self, item, count):
        self.item = item    # An Item
        self.count = count  # Number of items (integer)

    def get_item(self):
        return self.item

    def get_count(self):
        return self.count


class Store():
    def __init__(self, name):
        self.name = name
        self.inventory = []     # List of ItemCount

    def __str__(self):
        result = "Store '" + self.name + "'\n"
        result += "Inventory total value: $" + str(self.get_inventory_value()) + "\n"
        for item_count in self.inventory:
            result += "  " + str(item_count.get_count()) + " " + str(item_count.get_item()) + "\n"
        return result

    def add_item_count(self, item_count):
        self.inventory.append(item_count)

    def get_inventory_value(self):
        value = 0
        for item_count in self.inventory:
            item = item_count.get_item()
            count = item_count.get_count()
            cost = item.get_cost()
            value += cost * count
        return value

item1 = Item("iPhone4s", 100)
item2 = Item("iPhone5c", 200)
item3 = Item("iPhone5s", 300)
item4 = Item("Galaxy S4", 250)

store1 = Store("TerpTech")
store1.add_item_count(ItemCount(item1, 5))
store1.add_item_count(ItemCount(item3, 7))
store1.add_item_count(ItemCount(item4, 3))
print store1

store2 = Store("CompetitorU")
store2.add_item_count(ItemCount(item1, 2))
store2.add_item_count(ItemCount(item2, 5))
store2.add_item_count(ItemCount(item4, 2))
print store2