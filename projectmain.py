import customer
import store
import Inventory
import ShoppingCart

currentuser = store.store()

def shop_menu():

    inventory = Inventory.Inventory()
    shoppingCart = ShoppingCart.ShoppingCart()
    while True:
        print("\nView Inventory - 1")
        print("View Inventory by Category - 2")
        print("Add Item to Cart - 3")
        print("Go Back - 4")
        print("Exit Program - 5")

        userinput = input("Select an option [1/2/3/4/5]: ")

        if userinput == "1":
            inventory.ViewInventory()
        elif userinput == "2":
            inventory.ViewInventoryByCategory()
        elif userinput == "3":
            itemIdInput = input("What is the Item ID of your item? ")
            if inventory.checkIfItemExists(itemIdInput) == True:
                amountInput = input("How much of this item do you want? ")
                if inventory.checkStock(itemIdInput, amountInput) == True:
                    shoppingCart.AddItem(currentuser.get_CurrentUser(),itemIdInput,amountInput)
                else:
                    print("Not enough stock available.\n")
            else:
                print("Item does not exist.\n")
        elif userinput == "4":
            return
        elif userinput == "5":
            exit()
        else:
            print("Not a valid input")

def cart_info_menu():
    shoppingCart = ShoppingCart.ShoppingCart()
    while True:
        print("\nView Cart - 1")
        print("Remove Item from Cart - 2")
        print("Checkout - 3")
        print("Go Back - 4")
        userinput = input("Select an option [1/2/3/4/]: ")

        if userinput == "1":
            shoppingCart.ViewCart(currentuser.get_CurrentUser())
        elif userinput == "2":
            shoppingCart.removeItem()
        elif userinput == "3":
            shoppingCart.Checkout()
        elif userinput == "4":
            return
        else:
            print("Not a valid input")


#function for the menu once logged in
def store_menu():
    while True:
        print("\nWelcome", str(currentuser.get_CurrentUser()), "\n")

        print("Shop - 1")
        print("Cart Information - 2")
        print("Order History - 3")
        print("Account - 4")
        print("Exit Program - 5")

        userinput = input("Select an option [1/2/3/4/5]: ")
        #Need to create functions for cat info, cart info, order history
        #They will be called here
        if userinput == '1':
            shop_menu()
        
        elif userinput == '2':
            cart_info_menu()

        elif userinput == '3':
            currentuser.ViewOrderHistory()

        elif userinput == '4':
            account_menu()

        elif userinput == '5':
            print("Exiting program...")
            exit()
        else:
            print("Not a valid input")




#function for menu when account is selected
def account_menu():
    print("-------", currentuser.get_CurrentUser(), " Account-------")
    print("Edit Shipping Information - 1")
    print("Edit Payment Information - 2")
    print("Delete Account - 3")
    print("Logout - 4")
    userinput = input("Select an option [1/2/3/4]: ")
    if userinput == '1':
        return
    
    elif userinput == '2':
        return

    elif userinput == '3':
        return

    elif userinput == '4':
        print("Logging out...")
        print("Returning to the main menu...\n")
        login_menu()

 

#menu function before login
def login_menu():
    print("-------------Welcome to the Store-------------\n")

    print("Login - 1")
    print("Create Account - 2")
    print("Exit Program - 3")

    userinput = input("Select an option [1/2/3]: ")


    while(True):
        if userinput == '1':
            #calls login() method and sets current user as the new logged in user
                currentuser.Login()
                #currentuser.set_CurrentUser(store.store.Login())
                #if Login() returned "", restart the loop
                if currentuser.get_CurrentUser() == "":
                    print()
                else:
                    #open store menu and end loop
                    store_menu()
                    return


        elif userinput == '2':
            print("Create account selected")

            #taking inputs for new customer
            first = str(input("Enter your first name: "))
            last = str(input("Enter your last name:"))
            username = str(input("Enter a new username:"))
            password = str(input("Enter a password: "))
            shippingaddress = str(input("Enter a shipping address: "))
            cardnumber = str(input("Enter a card number: "))

            #created new customer and calling createaccount method
            new_customer = customer.customer()
            new_customer = store.store.CreateAccount(first, last, username, password, shippingaddress, cardnumber)

            #creating a string with customer info seperated by commas
            tofile = (str(new_customer.get_FirstName()) + "," + str(new_customer.get_LastName()) + "," + str(new_customer.get_Username()) + "," + str(new_customer.get_Password())
                    + "," + str(new_customer.get_ShippingAddress()) + "," + str(new_customer.get_CardNumber()) + "\n")

            #writing string to customer file
            write_file("customer.txt", tofile)

            #setting current user as the customer
            currentuser.set_CurrentUser(str(new_customer.get_Username()))
            print("Account Created. Logged in as " + currentuser.get_CurrentUser() + '\n')
            #calling store_menu to go to the menu as the new logged in customer
            store_menu()


        elif userinput == '3':
            print("Exiting Program...")
            exit()
        else:
            userinput = input("Select an option [1/2/3]: ")




     
def write_file(filename, input):
    with open(filename, 'a') as f:

        f.write(input)
        f.close()



def main():
    login_menu()

if __name__ == "__main__":
    main()
