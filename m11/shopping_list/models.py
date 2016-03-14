from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import re

Base = declarative_base()


class ShoppingItem(Base):
    """
    Here you need to define the columns for the table that will represent entries
    in the database. The columns represent the attributes of the model
    you will be defining. This model contains a record for each item on the shopping list,
    which is simply the name of the item, and how many of them to get along with an item id.
    """
    __tablename__ = 'shopping_item'
    id = Column(Integer, primary_key=True)
    item = Column(String(250))
    num_items = Column(Integer)

    def __init__(self, item, num_items):
        """
        Standard constructor - sets the values of this instance of a ShoppingItem.
        """
        self.item = item
        self.num_items = num_items

    def to_json(self):
        """
        Returns a json format representation of the model.
        """
        return { 'id': self.id, 'item': self.item, 'num_items': self.num_items }

    def add_item(self, session):
        """
        Add the instance of this shopping item to the database
        and commit the change to the database as well.
        """
        session.add(self)
        session.commit()

    def remove_item(self,session):
        """
        Remove this instance of the model from the database
        and commit the change to the database as well.
        """
        session.delete(self)
        session.commit()

    @staticmethod
    def get_all(session):
        """
        Return a list of all the shopping items in the database.
        Note that this is a static method, and is not associated with an
        instance of the model. See driver.py for an example of how to use it.
        """
        items = session.query(ShoppingItem).all()
        return items

# Creates all the tables in the engine.
# This is equivalent to "Create Table" in sql
engine = create_engine('sqlite:///shopping_items.db')
