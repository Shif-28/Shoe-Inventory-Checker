from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    """ Adds each line as its own object to shoes_list from the inventory txt file. Excludes first line """
    try:
        with open('inventory.txt', 'r') as file:
            next(file) # skips first line
            for line in file:
                lines = line.strip().split(",")
                country = lines[0]
                code = lines[1]
                product = lines[2]
                cost = int(lines[3])
                quantity = int(lines[4])
                shoe_obj = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe_obj)
    except FileNotFoundError:
        print("Sorry that file does not exist.")

def capture_shoes():
    """ Allows user to add a shoe to the shoe list as a Shoe object """
    new_country = input("Please enter the country the shoe is from: ")
    new_code = input("Please enter the code for the shoe: ")
    new_product = input("Please enter the product name of the shoe: ")
    while True:
        try:
            new_cost = int(input("please enter how much the shoe costs: "))
            new_quantity = int(input("What is the quantity of the shoe available: "))
            break
        except ValueError:
            print("That is not a valid entry. Try again.")
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_shoe)
    view_all()

def view_all():
    """ Displays all the shoes in the shoe list """
    '''print(f"{'⸻'* 20}\n"
          f"All shoes in inventory\n"
          f"{'⸻'* 20}")
    for obj in shoe_list:
        print(obj)
    print('⸻'* 20)'''
    shoe_list_table = []
    for obj in shoe_list:
        x = obj.country, obj.code, obj.product, obj.cost, obj.quantity
        shoe_list_table.append(x)
    print(tabulate(shoe_list_table, headers=["Country", "Code", "Product", "Cost (£)", "Quantity"], tablefmt="rounded_grid"))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Finds shoe with the lowest quantity.
    low_stock = []
    for obj in shoe_list:
        x = obj.code, obj.product, obj.quantity
        low_stock.append(x)
    low_stock_shoe = list(min(low_stock, key = lambda x: x[2]))
    print(f"This shoe needs a restock:\n"
          f"{'⸻'* 20}\n"
          f"Product Name: {low_stock_shoe[1]}\n"
          f"Product Code: {low_stock_shoe[0]}\n"
          f"Quantity: {low_stock_shoe[2]}\n"
          f"{'⸻'* 20}")
    # Asks user how many shoes to add to stock.
    while True:
        try:
            add_quantity = int(input("Please enter how many of this shoe to add to the system: "))
            low_stock_shoe[2] += add_quantity
            print(f"\nThe quantity for the following shoe has been updated:\n"
                  f"{'⸻'* 20}\n"
                  f"Product Name: {low_stock_shoe[1]}\n"
                  f"Product Code: {low_stock_shoe[0]}\n"
                  f"Quantity: {low_stock_shoe[2]}\n"
                  f"{'⸻'* 20}")
            break
        except ValueError:
            print("\nThat is not a valid entry. Please enter the quantity of the shoe to add to the system\n")
    # Updates quantity of shoe in the main shoe_list.
    for obj in shoe_list:
        if low_stock_shoe[1] == obj.product:
            obj.quantity = low_stock_shoe[2]
    # Updates the inventory file with the new quantity.
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for obj in shoe_list: # shows it has been updated. Need to write this to file.
            f.write(f"{obj.country},{obj.code},{obj.product},{obj.cost},{obj.quantity}\n")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        find_shoe = input("Enter the shoe's product code to see additional information: ")
        for obj in shoe_list:
            if find_shoe == obj.code:
                print(f"{'⸻'* 20}"
                      f"\n{obj}\n"
                      f"{'⸻'* 20}")
                return
        else:
            print("\nSorry, that shoe could not be found. Try again.\n")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print(f"{'⸻'* 20}\n"
          f"The value of the stock for each shoe is as follows:\n"
          f"{'⸻'* 20}")
    shoe_list_table = []
    for obj in shoe_list:
        x = obj.country, obj.code, obj.product, (obj.cost + obj.quantity)
        shoe_list_table.append(x)
    print(tabulate(shoe_list_table, headers=["Country", "Code", "Product", "Stock Value (£)"], tablefmt="rounded_grid"))


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    high_stock = []
    for obj in shoe_list:
        x = obj.code, obj.product, obj.quantity
        high_stock.append(x)
    high_stock_shoe = list(max(high_stock, key = lambda x: x[2]))
    print(f"This shoe has the highest stock and is on sale:\n"
          f"{'⸻'* 20}\n"
          f"Product Name: {high_stock_shoe[1]}\n"
          f"Product Code: {high_stock_shoe[0]}\n"
          f"Quantity: {high_stock_shoe[2]}\n"
          f"{'⸻'* 20}")


#==========Main Menu=============
# Allow user to select what function they want.
while True:
    read_shoes_data()
    menu = input("\nPlease enter a menu number from the options below"
                 ":\n"
                 "1 - Add shoe to the inventory\n"
                 "2 - View all shoes in the inventory\n"
                 "3 - Check which shoe needs a re-stock and add more shoes to inventory if needed\n"
                 "4 - Search for a shoe to find additional information\n"
                 "5 - Check the stock value of each shoe in the inventory\n"
                 "6 - Display shoe with the highest quantity.\n"
                 "Quit - Exit the program\n\n"
                 "Enter: ").lower()
    print()

    # Option 1 will let user add a shoe to the shoe list.
    if menu == "1":
        capture_shoes()

    # Option 2 displays all shows in inventory.
    elif menu == "2":
        view_all()

    # Option 3 checks shoe with the lowest stock and lets user update quantity of shoe to inventory.
    elif menu == "3":
        re_stock()

    elif menu == "4":
        search_shoe()

    elif menu == "5":
        value_per_item()

    elif menu == "6":
        highest_qty()

    elif menu == "quit":
        print("Bye!")
        exit()

    # Display error message if invalid option entered and try again.
    else:
        print("That is not a valid option. Please try again")