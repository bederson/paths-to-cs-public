from db_connection import *

# create instances of the Contact class to be added to local db
item1 = ShoppingItem("Milk", "1 quart")
item2 = ShoppingItem("Eggs", "1 dozen")
item3 = ShoppingItem("Ice cream", "5 pints")
engine = create_engine('sqlite:///shopping_items.db')

# initialize connection to db
session = DB_Setup.start()

# add items to the db and commit
item1.add_item(session)
item2.add_item(session)
item3.add_item(session)

# print each item in the db in json format using the static method
print "After adding the items to the database, it looks like this:"
items = ShoppingItem.get_all(session)
for item in items:
    print item.to_json()

# remove two items from db and verify that they have been removed
item1.remove_item(session)
item2.remove_item(session)
print "\nThere should only be one entry now:"
items = ShoppingItem.get_all(session)
for item in items:
    print item.to_json()

# remove any remaining entities to clean-up db
items = ShoppingItem.get_all(session)
for item in items:
    item.remove_item(session)

print "\nAfter removing all the items, the database should now be empty:"
item = session.query(ShoppingItem).first()
print item