import interface
from customer import *
import inventory

def main():
    current_inventory = inventory.Inventory()
    print("----Welcome to Miners Music Shop----")
    which_interface = input("are you a customer or an employee: ").lower()
    while which_interface not in ['customer', 'employee', 'c', 'e']:
        which_interface = input("command not recognized enter customer or employee").lower()
    if which_interface == 'customer' or which_interface == 'c':
        Customer_Interface(current_inventory)
    else:
        interface.Employee_Interface(current_inventory)
    print("thank you come again")

if __name__ == "__main__":
    main()