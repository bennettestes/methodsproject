import Inventory
import store


class customer:

    def set_FirstName(self, first):
        self.FirstName = first

    def get_FirstName(self):
        return self.FirstName


    def set_LastName(self, last):
        self.LastName = last

    def get_LastName(self):
        return self.LastName


    def set_ShippingAddress(self, username, shippingaddress):
        userLine = 0

        with open("customer.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[2] == username:
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 4:
                            newLine += shippingaddress + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-2]+"\n"
                    with open("customer.txt", "w") as f1:
                        f1.write("")
                    with open("customer.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == userLine:
                                f2.write(newLine)
                            else:
                                f2.write(line)
                            i+=1
                else:
                    userLine += 1
        

    def get_ShippingAddress(self):
        return self.ShippingAddress


    def set_CardNumber(self, username, card):
        userLine = 0

        with open("customer.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[2] == username:
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 5:
                            newLine += card + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-2]+"\n"
                    with open("customer.txt", "w") as f1:
                        f1.write("")
                    with open("customer.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == userLine:
                                f2.write(newLine)
                            else:
                                f2.write(line)
                            i+=1
                else:
                    userLine += 1

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

    def DeleteAccount(self, username):
        choice = input("Are you sure you want to delete your account? [y/n]: ")
        if choice == "n":
            return False
        elif choice == "y":
            userLine = 0

            with open("customer.txt", "r") as f:
                done = False
                lines = f.readlines()
                for line in lines:
                    values = line.split(",")
                    if values[2] == username:
                        with open("customer.txt", "w") as f1:
                            f1.write("")
                        with open("customer.txt", "a") as f2:
                            i = 0
                            for line in lines:
                                if i == userLine:
                                    done = True
                                else:
                                    f2.write(line)
                                i+=1
                    else:
                        userLine += 1
            return True
        else:
            print("Please enter [y/n].")
