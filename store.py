import customer

class store:

    def __init__(self, Currentuser = None):
        self.CurrentUser = Currentuser

    def set_CurrentUser(self, currentuser):
        self.CurrentUser = currentuser

    def get_CurrentUser(self):
        return self.CurrentUser


    def CreateAccount(FirstName, LastName, UserName, Password, ShippingAddress, CardNumber):
        newcustomer = customer.customer()
        newcustomer.set_FirstName(FirstName)
        newcustomer.set_LastName(LastName)
        newcustomer.set_Username(UserName)
        newcustomer.set_Password(Password)
        newcustomer.set_ShippingAddress(ShippingAddress)
        newcustomer.set_CardNumber(CardNumber)

        with open("shoppingCarts.txt", "a") as f:
            f.write(UserName + ",\n")

        with open("orderHistory.txt", "a") as f:
            f.write(UserName + ",\n")

        return newcustomer


    def Login(self):
        username = input("Enter username: ")

        with open("customer.txt", 'r') as f:
            
            current_user = ""
            
            while True:
                try:
                    lines = f.readline()
                    currentline = lines.split(",")
                    if currentline[2] == username:
                        password = input("Enter Password: ")
                        if currentline[3] == password:
                            self.CurrentUser = username
                            return
                
                        else: 
                            print("Incorrect Username or Password. ")
                except IndexError:
                    exit()
        


    def Logout():
        print("Logged out successfully")

