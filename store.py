import customer

class store:

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
        return newcustomer

    def AddOrderHistory(self, orderHistory):
        self.OrderHistory = []
        self.OrderHistory.append(orderHistory)

    
    def ViewOrderHistory(self):
        print("Showing Order History...\n")
        for x in range(len(self.OrderHistory)):
            print(self.OrderHistory[x])    


    def Login():
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
                            current_user = store()
                            current_user.set_CurrentUser(username)
                            return current_user
                
                        else: 
                            print("Incorrect Username or Password. ")
                except IndexError:
                    exit()
        


    def Logout():
        print("Logged out successfully")

