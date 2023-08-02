import psycopg2
from DB_connection import DatabaseManager

# EX XP PART 1:


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self, connection):
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s);"
            data = (self.name, self.price)
            cursor.execute(insert_query, data)
            connection.commit()

        except (Exception, psycopg2.Error) as err:
            print("Error while inserting to PostgreSQL:", err)

    def delete(self, connection):
        try:
            cursor = connection.cursor()
            delete_query = 'DELETE FROM menu_items WHERE item_name = %s;'
            data = (self.name,)
            cursor.execute(delete_query, data)
            connection.commit()

        except (Exception, psycopg2.Error) as err:
            print("Error while deleting to PostgreSQL:", err)

    def update(self, new_name, new_price, connection):
        try:
            cursor = connection.cursor()
            update_query = 'UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s;'
            data = (new_name, new_price, self.name)
            cursor.execute(update_query, data)
            connection.commit()

        except (Exception, psycopg2.Error) as err:
            print("Error while updating to PostgreSQL:", err)


class MenuManager:
    def get_by_name(self, item_name, connection):
        try:
            cursor = connection.cursor()
            get_query = 'SELECT * FROM menu_items WHERE item_name = %s;'
            data = (item_name,)
            cursor.execute(get_query, data)
            item = cursor.fetchone()

            if item:
                return item
            else:
                return None
        except (Exception, psycopg2.Error) as err:
            print("Error while fetching from PostgreSQL:", err)

    def all_items(self, connection):
        try:
            cursor = connection.cursor()
            fetch = 'SELECT * FROM menu_items'
            cursor.execute(fetch)
            all_items = cursor.fetchall()

            if all_items:
                return all_items
            else:
                return None

        except (Exception, psycopg2.Error) as err:
            print("Error while fetching from PostgreSQL:", err)

# TESTS

# with DatabaseManager() as db:
#     itemA = MenuItem('Burger', 35)
#     itemB = MenuItem('Pasta', 20)
#     itemC = MenuItem('Gabagool', 420)
#     itemA.save(db.connection)
#     itemB.save(db.connection)
#     itemC.save(db.connection)
#     itemB.delete(db.connection)
#     itemA.update('Veggie Burger', 37, db.connection)
#     manager = MenuManager()
#     item3 = manager.get_by_name('Gabagool', db.connection)
#     item2 = manager.get_by_name('Beef Stew', db.connection)
#     items = manager.all_items(db.connection)
#     print('ONE ITEM:', item2)
#     print('ONE ITEM:', item3)  # expect - Gabagool
#     print('ALL ITEMS:', items)
