class customer:

    def set_FirstName(self, first):
        self.FirstName = first

    def get_FirstName(self):
        return self.FirstName


    def set_LastName(self, last):
        self.LastName = last

    def get_LastName(self):
        return self.LastName


    def set_ShippingAddress(self, shippingaddress):
        self.ShippingAddress = shippingaddress

    def get_ShippingAddress(self):
        return self.ShippingAddress


    def set_CardNumber(self, card):
        self.CardNumber = card

    def get_CardNumber(self):
        return self.CardNumber


    def set_Password(self, password):
        self.Password = password

    def get_Password(self):
        return self.Password

    
    def set_Username(self, username):
        self.Username = username

    def get_Username(self):
        return self.Username


    def AddOrderHistory(self, orderHistory):
        self.OrderHistory = []
        self.OrderHistory.append(orderHistory)

    
    def ViewOrderHistory(self):
        print("Showing Order History...\n")
        for x in range(len(self.OrderHistory)):
            print(self.OrderHistory[x])

    def DeleteAccount(self):
        choice = input("Are you sure you want to delete your account? [Y/n]: ")
        if choice == "n":
            return
        elif choice == "Y":
            del self
        else:
            print("Please enter [Y/n].")
