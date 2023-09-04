import datetime

import Product
import User


def access_denied_method():
    access_denied = "\033[1;31mACCESS DENIED\033[0m"
    print("___________________________")
    print(access_denied)
    print("____________________________")
    return


def read_products_from_file():
    file_name = "products.txt"
    products = []
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(';')
            product = Product.Product(int(data[0]), data[1], data[2],
                                      int(data[3]), int(data[4]), data[5],
                                      int(data[6]), int(data[7]), data[8])
            products.append(product)
    # print(products[0])
    return products


def read_users_from_file():
    users = []
    file_name = "users.txt"
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(';')
            if len(data) == 7:
                user_id, user_name, dob, role, active, basket_data, order = data
                basket = {}
                if basket_data.strip() != '{}':
                    basket_items = basket_data.strip('{}').split(',')
                    for item in basket_items:
                        product_id, quantity = item.split(':')
                        basket[int(product_id)] = int(quantity)
                user = User.User(int(user_id), user_name, dob, role, int(active), basket, int(order))
                users.append(user)
            else:
                print(f"Skipping invalid data: {data}")
    return users


products = read_products_from_file()  # read products file
users = read_users_from_file()  # read users file

# ASK USER TO ENTER HIS ID
user_id_input = int(input("Enter your ID: "))
user_founded = None

# SEARCH FOR USER
for user in users:
    if user.user_id == user_id_input:
        user_founded = user
        break

if user_founded:
    print(user_founded)
    while True:
        print("=" * 32)
        print("          MAIN MENU")
        print("=" * 32)
        print("1.  ADD PRODUCT")
        print("2.  PLACE AN ITEM ON SALE")
        print("3.  UPDATE PRODUCT")
        print("4.  ADD NEW USER")
        print("5.  UPDATE USER")
        print("6.  DISPLAY ALL USERS")
        print("7.  LIST ALL PRODUCTS")
        print("8.  LIST SHOPPERS")
        print("9.  ADD PRODUCT TO THE BASKET")
        print("10. DISPLAY BASKET")
        print("11. UPDATE BASKET")
        print("12. PLACE ORDER")
        print("13. EXECUTE ORDER")
        print("14. SAVE PRODUCTS TO FILE")
        print("15. SAVE USERS TO TEXT FILE")
        print("17. LOGIN WITH NEW USER")
        print("16. EXIT")
        print("=" * 32)
        choice = None
        try:
            choice = int(input("CHOOSE ONE OF THE OPTIONS: "))

            if choice == 18:
                break
            elif 1 <= choice <= 17:
                pass
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number for your choice.")

        if choice == 1:
            if user_founded.role.lower() == "admin":
                product_exists = False
                product_id = int(input("ENTER PRODUCT ID: "))

                # check if ID IS ALREADY TAKEN
                for product in products:
                    if product_id == product.product_id:
                        print("=" * 32)
                        print("PRODUCT ALREADY EXIST")
                        print("=" * 32)
                        product_exists = True
                        break

                if not product_exists:
                    product_name = input("ENTER PRODUCT NAME: ")
                    product_category = input("ENTER CATEGORY:")
                    price = int(input("ENTER PRODUCT price: "))
                    inventory = int(input("ENTER NUMBER OF ITEMS AVAILABLE: "))
                    supplier = input("ENTER COMPANY PROVIDING PRODUCT NAME: ")
                    has_an_offer = int(input("IF ON SALE --> 1\nOTHER WISE --> 0: "))
                    new_product = Product.Product(product_id, product_name, product_category, price, inventory,
                                                  supplier,
                                                  has_an_offer)
                    products.append(new_product)
                    print("____________________________")
                    print("PRODUCT ADDED SUCCESSFULLY.")
                    print("____________________________")

            else:
                access_denied_method()

        elif choice == 2:  # add item on sale
            product_found = False
            if user_founded.role.lower() == "admin":
                product_id = int(input("ENTER PRODUCT ID TO BE LISTED: "))
                for product in products:
                    if product_id == product.product_id:
                        product_found = True
                        product.set_has_an_offer(1)
                        offer = int(input("ENTER PRICE AFTER SALE: "))
                        product.set_offer_price(offer)
                        valid_until = input("ENTER DATE until sale is valid  (yyy-mm-dd): ")
                        product.set_valid_until(valid_until)
                        print("______________________")
                        print("PRODUCT IS ON SALE")
                        print("______________________")
                        break

                if not product_found:
                    print("______________________")
                    print("PRODUCT DOESN'T EXIST")
                    print("_______________________")

            else:
                access_denied_method()

        elif choice == 3:
            product_exists = False
            if user_founded.role.lower() == "admin":
                product_id = int(input("ENTER PRODUCT ID:"))
                for product in products:
                    if product_id == product.product_id:
                        product_exists = True
                        while True:
                            print("=" * 32)
                            print("          UPDATE PRODUCT")
                            print("=" * 32)
                            print("1- change product name")
                            print("2- change product category")
                            print("3- change price")
                            print("4- change inventory")
                            print("5- change supplier")
                            print("6- change has an offer")
                            print("7- change offer price")
                            print("8- change date of expire")
                            print("9- exit")
                            print("=" * 32)
                            select = int(input("PLEASE CHOOSE ONE OF THE FOLLOWING: "))
                            if select == 1:
                                new_name = input("Enter product new name: ")
                                product.set_product_name(new_name)
                                print("NAME HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 2:
                                new_name = input("Enter product new category: ")
                                product.set_product_category(new_name)
                                print("category HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 3:
                                new_price = int(input("Enter product new price: "))
                                product.set_product_price(new_price)
                                print("PRICE HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 4:
                                new_inventory = int(input("Enter product new INVENTORY: "))
                                product.set_inventory(new_inventory)
                                print("inventory HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 5:
                                new_supplier = input("Enter product new supplier: ")
                                product.set_supplier(new_supplier)
                                print("supplier HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 6:
                                has_offer = int(input("Enter 1--> OFFER\n0-->NO OFFER: "))
                                product.set_has_an_offer(has_offer)
                                print("HAS OFFER HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 7:
                                new_offer = int(input("Enter product new offer: "))
                                product.set_offer_price(new_offer)
                                print("OFFER PRICE HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 8:
                                dox = input("Enter product new date of expire for sale as yyy-mm-dd: ")
                                product.set_valid_until(dox)
                                print("DATE HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 9:
                                break
                if not product_exists:
                    print("______________________")
                    print("PRODUCT DOESN'T EXIST")
                    print("_____________________")

            else:
                access_denied_method()

        elif choice == 4:
            id_exists = False
            if user_founded.role.lower() == "admin":
                new_user_id = int(input("ENTER NEW USER ID:"))
                for user in users:  # check if ID exists
                    if user.get_user_id() == new_user_id:
                        print("ID ALREADY TAKEN")
                        print("_________________")
                        id_exists = True
                        break
                if not id_exists:
                    new_user_name = input("Enter new user name: ")
                    new_user_dob = input("Enter new user date of birth (yyyy-mm-dd): ")
                    new_user_role = (input("Enter new user role (admin, shopper): "))
                    active = int(input("Enter user activity 1-->active, 0---> not active: "))
                    basket = {}
                    order = 0
                    user = User.User(new_user_id, new_user_name, new_user_dob, new_user_role, active, basket, order)
                    users.append(user)
                    print(f"{new_user_role} HAS BEEN ADDED")
                    print("=" * 32)
            else:
                access_denied_method()

        elif choice == 5:
            if user_founded.role.lower() == "admin":
                user_exist = False
                user_id = int(input("Enter user id to be updated: "))
                for user in users:
                    if user.get_user_id() == user_id:
                        user_exist = True
                        while True:
                            print("=" * 32)
                            print("          UPDATE USER")
                            print("=" * 32)
                            print("1- change user name")
                            print("2- change user date of birth")
                            print("3- change role")
                            print("4- change activity")
                            print("5- update basket")
                            print("6- change order")
                            print("7-exit")
                            print("=" * 32)

                            select = int(input("PLEASE CHOOSE ONE OF THE FOLLOWING: "))
                            if select == 1:
                                new_name = input("Enter user new name: ")
                                user.set_user_name(new_name)
                                print("NAME HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 2:
                                new_dob = input("Enter user new birth of date(yyyy-mm-dd): ")
                                user.set_user_dob(new_dob)
                                print("Birth of date HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 3:
                                new_role = input("Enter user new role (shopper, admin): ")
                                user.set_user_role(new_role)
                                print("ROLE HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 4:
                                new_activity = int(input("Enter user new activity: "))
                                user.set_user_active(new_activity)
                                print("activity HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 5:
                                while True:
                                    print("=" * 32)
                                    print("          USER BASKET")
                                    print("=" * 32)
                                    print("Choose one of the following: ")
                                    print("1- ADD to BASKET")
                                    print("2- DELETE FROM BASKET")
                                    print("4- EDIT THE BASKET")
                                    print("3- Exit")
                                    print("=" * 32)
                                    c = int(input("Your choice: "))

                                    if c == 3:
                                        break

                                    p_id = int(input("Enter product ID: "))
                                    p_exists = False

                                    the_product = None
                                    for p in products:  # check if product exists
                                        if p.get_product_id() == p_id:
                                            p_exists = True
                                            the_product = p

                                    if p_exists:
                                        if c == 1:
                                            num_items = int(input("Enter number of items: "))
                                            # check if inventory have the amount of num_items
                                            if the_product.get_inventory() >= num_items:
                                                user.basket[p_id] = num_items
                                                # remove the amount from the inventory
                                                # the_product.set_inventory(the_product.get_inventory() - num_items)
                                                print("PRODUCT HAS BEEN ADDED SUCCESSFULLY TO BASKET")
                                            else:
                                                print("NO ENOUGH ITEMS IN THE INVENTORY")

                                        elif c == 4:
                                            # check if the item exists in the basket
                                            founded = False
                                            for pid in user.get_user_basket():
                                                if p_id == pid:
                                                    founded = True
                                                    new_num_items = int(input("ENTER NEW NUMBER OF ITEMS YOU WANT: "))
                                                    # check if inventory have the amount of num_items
                                                    if the_product.get_inventory() >= new_num_items:
                                                        # the_product.set_inventory(user.get_user_basket()[p_id] +
                                                        #                           the_product.get_inventory())
                                                        # the_product.set_inventory(the_product.get_inventory() -
                                                        #                           new_num_items)
                                                        user.get_user_basket()[p_id] = new_num_items
                                                        print("PRODUCT HAS BEEN UPDATED SUCCESSFULLY TO BASKET")
                                                    else:
                                                        print("NO ENOUGH ITEMS IN THE INVENTORY")
                                            if not founded:
                                                print("PRODUCT DOESN'T EXIST IN THE USER BASKET")

                                        elif c == 2:
                                            product_deleted = False
                                            # make copy from the basket
                                            b_copy = user.get_user_basket().copy()
                                            # check if product exists in user basket
                                            for pID in b_copy:
                                                if pID == p_id:
                                                    # restore the items to the inventory if order is 1
                                                    if user.get_user_order() == 1:
                                                        the_product.set_inventory(the_product.get_inventory() +
                                                                                  user.get_user_basket()[p_id])
                                                    del user.get_user_basket()[p_id]
                                                    product_deleted = True
                                                    print("PRODUCT HAS BEEN DELETED FROM USER BASKET")
                                            b_copy = user.get_user_basket()

                                            if not product_deleted:
                                                print("PRODUCT NOT FOUND IN USER BASKET")
                                    else:
                                        print("PRODUCT DOESN'T EXIST")
                                        print("_______________________")

                            elif select == 6:
                                new_order = int(input("Enter 1--> ready\n0-->NOt ready: "))
                                user.set_user_order(new_order)
                                print("order HAS BEEN UPDATED")
                                print("_______________________")
                            elif select == 7:
                                break
                            print("_______________________")

                if not user_exist:
                    print("______________________")
                    print("USER DOESN'T EXIST")
                    print("_____________________")

            else:
                access_denied_method()

        elif choice == 6:
            if user_founded.role.lower() == "admin":
                print("LIST OF USERS:\n")
                print("___________________________")
                for user in users:
                    print(user)
                    print("-----------------------")
                print("___________________________")

            else:
                access_denied_method()

        elif choice == 7:
            while True:
                print("CHOOSE ONE OF THE OPTIONS: ")
                print("1-ALL")
                print("2-OFFERS")
                print("3-CATEGORY")
                print("4-NAME")
                print("5-EXIT")
                c = int(input("Enter your choice: "))

                if c == 1:
                    print("LIST OF Products:\n")
                    print("___________________________")
                    for p in products:
                        print(p)
                        print("-----------------------")
                    print("___________________________")

                elif c == 2:
                    print("LIST OF Products HAVING OFFERS:\n")
                    print("___________________________")
                    for p in products:
                        if p.has_an_offer == 1:
                            print(p)
                            print("-----------------------")
                    print("___________________________")

                elif c == 3:
                    category_name = input("Enter category name: ")
                    print(f"LIST OF Products in {category_name}:\n")
                    print("___________________________")
                    for p in products:
                        if p.get_product_category() == category_name:
                            print(p)
                            print("-----------------------")
                    print("___________________________")

                elif c == 4:
                    prod_name = input("Enter PRODUCT NAME: ")
                    print(f"{prod_name} INFO:\n")
                    print("___________________________")
                    for p in products:
                        if p.get_product_name() == prod_name:
                            print(p)
                            print("-----------------------")
                    print("___________________________")
                elif c == 5:
                    break

        elif choice == 8:
            if user_founded.role.lower() == "admin":
                while True:
                    print("=" * 32)
                    print("          SHOPPERS")
                    print("=" * 32)
                    print("CHOOSE ONE OF THE FOLLOWING: ")
                    print("1-ALL")
                    print("2-WITH ITEMS IN THE BASKET")
                    print("3-HAS UNPROCESSED ORDERS")
                    print("4-REQUESTED AN ORDER")
                    print("5-EXIT")
                    print("=" * 32)
                    c = int(input("YOUR CHOICE: "))

                    if c == 1:
                        print("______________________")
                        print("ALL SHOPPERS:")
                        print("-------------------")
                        for shopper in users:
                            if shopper.get_user_role().lower() == "shopper":
                                print(shopper)
                        print("_________________________")

                    elif c == 2:
                        print("______________________")
                        print("SHOPPERS WITH ITEMS IN THE BASKET:")
                        print("-------------------")
                        for shopper in users:
                            if shopper.get_user_basket() and shopper.get_user_role().lower() == "shopper":
                                print(shopper)
                                print("------------------")
                        print("_________________________")

                    elif c == 3:
                        print("______________________")
                        print("SHOPPERS WITH UNPROCESSED ORDER:")
                        print("-------------------")
                        for shopper in users:
                            if shopper.get_user_role().lower() == "shopper" and bool(shopper.get_user_basket()) and \
                                    shopper.get_user_order():
                                print(shopper)

                        print("_________________________")

                    elif c == 4:
                        print("______________________")
                        print("SHOPPERS WITH UNPROCESSED ORDER:")
                        print("-------------------")
                        for shopper in users:
                            if shopper.get_user_order() and shopper.get_user_role().lower() == "shopper":
                                print(shopper)
                                print("------------------")
                        print("_________________________")

                    elif c == 5:
                        break

            else:
                access_denied_method()

        elif choice == 9:
            if user_founded.role.lower() == "shopper":
                p_id = int(input("Enter product ID TO BE ADDED: "))

                p_exists = False
                the_product = None
                for p in products:
                    if p.get_product_id() == p_id:
                        p_exists = True
                        the_product = p

                if p_exists:
                    num_items = int(input("ENTER NUMBER OF ITEMS YOU WANT TO ADD: "))
                    if the_product.get_inventory() >= num_items:
                        user_founded.get_user_basket()[p_id] = num_items
                        print("BASKET HAS BEEN UPDATED")
                    else:
                        print("NO ENOUGH ITEMS IN THE INVENTORY")

                else:
                    print("PRODUCT DOESN'T EXIST")
                print("__________________________")
            else:
                access_denied_method()

        elif choice == 10:
            if user_founded.role.lower() == "shopper":
                sum = 0
                print("PRODUCTS: ")
                print("****************")
                for key in user_founded.get_user_basket():
                    # print(key)
                    for product in products:
                        if product.get_product_id() == key:
                            print(product)
                            print(f"NUMBER OF ITEMS OF THIS PRODUCT: {user_founded.get_user_basket()[key]}")

                            x = int(product.get_has_an_offer())
                            if int(x) == 0:
                                print(f"total coast of this product:{user_founded.get_user_basket()[key] * product.price}")
                                sum += user_founded.get_user_basket()[key] * product.price
                            elif int(x) == 1:
                                print(
                                    f"total coast of this product:{user_founded.get_user_basket()[key] * product.get_offer_price()}")
                                sum += user_founded.get_user_basket()[key] * product.get_offer_price()

                            print()

                            break
                print("*******************")
                print(f"TOTAL COAST :{sum}")
                print("*******************")

            else:
                access_denied_method()

        elif choice == 11:
            if user_founded.role.lower() == "shopper":
                while True:
                    print("=" * 32)
                    print("          UPDATE BASKET")
                    print("=" * 32)
                    print("Choose one of the following: ")
                    print("1- Edit the BASKET")
                    print("2- DELETE FROM BASKET")
                    print("3- clear")
                    print("4- Exit")
                    print("=" * 32)
                    c = int(input("Your choice: "))
                    if c == 3:
                        user_founded.get_user_basket().clear()
                        print("BASKET HAS BEEN CLEARED")
                    elif c == 4:
                        print(user_founded.get_user_basket())
                        break
                    else:
                        p_id = int(input("Enter product ID: "))
                        p_exists = None

                        for p in products:  # check if product exists
                            if p.get_product_id() == p_id:
                                p_exists = p

                        if p_exists:
                            if c == 1:
                                num_items = int(input("Enter number of items: "))
                                if num_items > p_exists.get_inventory():
                                    print("NO ENOUGH PRODUCTS IN THE STORE")
                                else:
                                    # let's update the inventory
                                    # print(user_founded.get_user_basket()[p_id])
                                    # if num_items > user_founded.get_user_basket()[p_id]:  # change num in inventory
                                    #     p_exists.set_inventory(p.get_inventory() - num_items)
                                    # else:
                                    #     p_exists.set_inventory(p.get_inventory() + num_items)
                                    # print(p_exists)
                                    user_founded.basket[p_id] = num_items
                                    print("PRODUCT HAS BEEN UPDATED")

                            elif c == 2:
                                # check if the product is in the basket
                                product_d = False
                                for key in user_founded.get_user_basket():
                                    if key == p_id:
                                        del user_founded.get_user_basket()[p_id]
                                        print("PRODUCT HAS BEEN REMOVED FROM BASKET")
                                        product_d = True
                                        break
                                if not product_d:
                                    print(f"PRODUCT DOESN'T EXIST IN {user_founded.get_user_name()} BASKET")

                        else:
                            print("PRODUCT DOESN'T EXIST")
                            print("_______________________")

            else:
                access_denied_method()

        elif choice == 12:
            if user_founded.role.lower() == "shopper":
                if not user_founded.get_user_basket():
                    print("THE BASKET IS EMPTY, YOU CAN'T PLACE ORDER")
                else:
                    user_founded.set_user_order(1)
                    print("ORDER HAS BEEN PLACED")
                print("_____________________________")
            else:
                access_denied_method()

        elif choice == 13:

            if user_founded.role.lower() == "admin":

                shopper_id = int(input("ENTER SHOPPER ID : "))
                shopper_user = None

                user_index = None
                for i, user in enumerate(users):
                    if user.get_user_id() == shopper_id:
                        user_index = i
                        shopper_user = user
                        break
                if shopper_user.get_user_order():

                    basket_copy = users[user_index].get_user_basket().copy()
                    if not basket_copy:
                        print("BASKET IS EMPTY")
                    else:
                        for key in basket_copy:
                            get_index = None
                            # get the index of the product
                            for i, p in enumerate(products):
                                if p.get_product_id() == key:
                                    get_index = i
                            if basket_copy[key] > products[get_index].get_inventory():
                                print(f"YOU CAN'T PLACE AN ORDER FOR {products[key]}")
                                print(f"NO ENOUGH {products[key]} IN THE STORE")
                                # print(f"{products[key]} ITEMS WILL BE REMOVED")
                                # del users[shopper_id].get_user_basket()[key]
                            else:
                                p_index = 0
                                i = 0
                                for item in products:
                                    if item.get_product_id() == key:
                                        p_index = i
                                        break
                                    i += 1
                                print(f"{products[p_index]}\n has BEEN EXECUTED")
                                print("__________________________________")
                                users[user_index].set_user_order(0)
                                # let's update the inventory
                                products[p_index].set_inventory(
                                    products[p_index].get_inventory() - basket_copy[key])
                                # print(users[user_index].get_user_basket()[key])
                                del users[user_index].get_user_basket()[key]
                            basket_copy = users[user_index].get_user_basket().copy()  # update the copy
                else:
                    print("SHOPPER HAS NOT PLACED AN ORDER")
            else:
                access_denied_method()

        elif choice == 14:
            if user_founded.role.lower() == "admin":
                file_name = input("Enter the name of the text file to save the products: ")
                try:
                    # Open the file in write mode
                    with open(file_name, 'w') as file:
                        # Iterate through products and write each product's information to the file
                        for product in products:
                            file.write(
                                f"{product.get_product_id()};{product.get_product_name()};{product.get_product_category()};{product.get_product_price()};{product.get_inventory()};{product.get_supplier()};{product.get_has_an_offer()};{product.get_offer_price()};{product.get_valid_until()}\n")
                    print(f"Products have been saved to {file_name}.")
                    print("___________________________________________")
                except IOError:
                    print(f"Error: Unable to save products to {file_name}.")

            else:
                access_denied_method()

        elif choice == 15:
            if user_founded.role.lower() == "admin":
                file_name = input("Enter the name of the text file to save the users: ")
                try:
                    # Open the file in write mode
                    with open(file_name, 'w') as file:
                        # Iterate through products and write each product's information to the file
                        for user in users:
                            file.write(
                                f"{user.get_user_id()};{user.get_user_name()};{user.get_user_dob()};{user.get_user_role()};{user.get_user_active()};{user.get_user_basket()};{user.get_user_order()}\n")
                    print(f"USERS have been saved to {file_name}.")
                    print("___________________________________________")
                except IOError:
                    print(f"Error: Unable to save products to {file_name}.")

            else:
                access_denied_method()

        elif choice == 16:
            answer = input("DO YOU WANT TO SAVE PRODUCTS AND USERS: Y/N: ")
            if answer.lower() == 'n':
                users.clear()
                products.clear()
            print("BYE :)")
            exit(0)

        elif choice == 17:
            user_id_input = int(input("Enter your ID: "))
            user_found = False
            for user in users:
                if user.user_id == user_id_input:
                    user_founded = user
                    print("=" * 32)
                    print("NEW USER HAS LOGGED IN")
                    print(user_founded)
                    print("=" * 32)
                    user_found = True
                    break
            if not user_found:
                print("USER WITH SUCH ID DOESN'T EXIST")

else:
    print("ACCESS DENIED: USER NOT FOUND ")
