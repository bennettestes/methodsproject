import Inventory


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

    
    def ViewOrderHistory(self, username):
        inventory = Inventory.Inventory()
        firstLoop = True
        print("-------------"+username+ "'s Order History-------------\n")
        with open("orderHistory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    orderNum = 1
                    donePrinting = False
                    valueNum = 0
                    x = 1
                    while donePrinting == False:
                        i=1
                        print("Order "+str(orderNum)+": \n")
                        orderNum += 1
                        moveOn = False
                        while moveOn == False:
                            if x+i != len(values)-1:
                                if values[x+i] != username:
                                    returnValue = inventory.getItemNameandPrice(values[x+i])
                                    print("ItemID: " + values[x+i] + " -- " + returnValue[0] + " Amount: " + values[x+i+1]+ " Price: " + "{:.2f}".format(float(returnValue[1])*float(values[x+i+1])) +"\n")
                                    i+=2
                                else:
                                    moveOn = True
                                    x+=i
                            else:
                                moveOn = True
                                donePrinting = True

    def DeleteAccount(self):
        choice = input("Are you sure you want to delete your account? [Y/n]: ")
        if choice == "n":
            return
        elif choice == "Y":
            del self
        else:
            print("Please enter [Y/n].")
