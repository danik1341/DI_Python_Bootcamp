import psycopg2
from DB_connection import DatabaseManager
from menu_item import MenuManager
from menu_item import MenuItem

# PART 2:


class MenuEditor:
    @staticmethod
    def show_user_menu():
        print("Program Menu:")
        print('View an Item (V)')
        print('Add an Item (A)')
        print('Delete an Item (D)')
        print('Update an Item (U)')
        print('Show the Menu (S)')

        user_input = input(" --> ").strip().lower()

        if user_input == 'v':
            MenuEditor.view_item()
        elif user_input == 'a':
            MenuEditor.add_item()
        elif user_input == 'd':
            MenuEditor.delete_item()
        elif user_input == 'u':
            MenuEditor.update_item()
        elif user_input == 's':
            MenuEditor.show_menu()
        else:
            print("Invalid choice!")

    @staticmethod
    def view_item():
        item_name = input('Enter the item name: ').strip()
        with DatabaseManager() as db:
            manager = MenuManager()
            item = manager.get_by_name(item_name, db.connection)
            if item:
                print(f"Item: {item[1]}, Price: {item[2]}")
            else:
                print("Item not found.")

    @staticmethod
    def add_item():
        item_name = input('Enter the item name: ').strip()
        item_price = float(input('Enter item price: '))
        item = MenuItem(item_name, item_price)
        with DatabaseManager() as db:
            item.save(db.connection)
            print(
                f"Item: {item_name} with price: {item_price} was saved successfully")

    @staticmethod
    def delete_item():
        item_name = input('Enter the item name you wish to delete: ').strip()
        with DatabaseManager() as db:
            manager = MenuManager()
            item = manager.get_by_name(item_name, db.connection)
            if item:
                del_item = MenuItem(item[1], item[2])
                del_item.delete(db.connection)
                print("Item deleted successfully.")
            else:
                print("Item not found.")

    @staticmethod
    def update_item():
        item_name = input("Enter the item name to update: ")
        new_name = input("Enter the new item name: ")
        new_price = float(input("Enter the new item price: "))
        with DatabaseManager() as db:
            manager = MenuManager()
            item = manager.get_by_name(item_name, db.connection)
            if item:
                up_item = MenuItem(item[1], item[2])
                up_item.update(new_name, new_price, db.connection)
                print("Item updated successfully.")
            else:
                print("Item not found.")

    @staticmethod
    def show_menu():
        with DatabaseManager() as db:
            manager = MenuManager()
            items = manager.all_items(db.connection)
            if items:
                for item in items:
                    print(f"Item: {item[1]}, Price: {item[2]}")
            else:
                print("No items in the menu.")


if __name__ == "__main__":
    MenuEditor.show_user_menu()
