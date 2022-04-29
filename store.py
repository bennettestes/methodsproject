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



    def Login():
        username = input("Enter username: ")

        with open("customer.txt", 'r') as f:
            lines = f.readlines()
            current_user = ""
            while current_user == "":
                for line in lines:
                    currentline = line.split(",")
                    if currentline[2] == username:
                        password = input("Enter Password: ")
                        if currentline[3] == password:
                            current_user = store()
                            current_user.set_CurrentUser(username)
                            return current_user
                        else:
                            print("Incorrect password for", username)
                            return ""
                    else:
                        print("Error: Username not found.")
                        return ""
        f.close()
            


    def Logout():
        print("Logged out successfully")

