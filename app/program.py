"""
Application
"""

from os import system as os_system, name as os_name
from time import sleep

from .api.views import createRecord, listAllRecords, readRecord, updateRecord, deleteRecord
from .api.database.database import tableTypes


def main():
    """ Main program of this application """
    #try:
    while(True):
        # Clear the screen
        os_system('cls' if os_name == 'nt' else 'clear')

        # Start the interface with system's operator
        print("#" + "-" * 79)
        print("# SALES MANAGEMENT ")
        print("#" + "-" * 79)

        # Ask which control management to access
        print("Select which control to access:")
        print(f"\tCustomers: { tableTypes.CUSTOMER.value }")
        print(f"\tSellers:   { tableTypes.SELLER.value }")
        print(f"\tProducts:  { tableTypes.PRODUCT.value }")
        print(f"\tSales:     { tableTypes.SALE.value }")
        print("Any other input will quit the program.")

        mngtChoice :int = 0         # management's choice
        try:
            mngtChoice = int(input("Your choice: ") or "-1")
        except ValueError:
            mngtChoice = -1

        # Caso o usuario não entre com um numero
        if mngtChoice in [1,2,3]:
            # Then ask what to do with databases
            print("#" + "-" * 79)
            print("Select which action now:")
            print(f"\tAdd:      1")
            print(f"\tUpdate:   2")
            print(f"\tRemove:   3")
            print(f"\tList:     4")
            print("Any other input will return.")

            actChoice :int = 0      # action's choice
            try:
                actChoice = int(input("Your choice: ") or "-1")
            except ValueError:
                actChoice = -1

            # Variable to store the result of called operations
            result: bool = False

            # Note: passed parameter is the one related to management
            if actChoice == 1:
                # Call the view to handle record's inclusion    
                result = createRecord(tableTypes(mngtChoice))
            elif actChoice == 2:
                # Call the view to handle record's update
                result = updateRecord(tableTypes(mngtChoice))
            elif actChoice == 3:
                # Call the view to handle record's deletion
                result = deleteRecord(tableTypes(mngtChoice))
            elif actChoice == 4:
                # Call the view to list records in the table
                result = listAllRecords(tableTypes(mngtChoice))

            # Inform operator if the operation succeeded or not
            if result:
                print("\nSuccess!")
            else:
                print("\nError!")

            # Wait the user press any key before clear the screen
            #   and wait for new input
            input("\nPress <ENTER> to continue...")
        elif mngtChoice == 4:
            # TO BE DONE...
            print("\nSales management under development...")

            # Wait the user press any key before clear the screen
            #   and wait for new input
            input("\nPress <ENTER> to continue...")
        else:
            # Quit the looping
            print("\nSee you soon!\n")
            break
    #except:
    #    pass

if __name__ == "__main__":
    main()
