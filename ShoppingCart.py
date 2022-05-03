from hashlib import new
from turtle import update
import Item
import Inventory
import store

class ShoppingCart:
    

    def AddItem(self, username, ItemID, Amount):
        cartline = 0
        alreadyExists = False
        with open("shoppingCarts.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[0] == username:
                    x = 0
                    for value in values:
                        if value == ItemID:
                            newValue = str(int(values[x+1])+int(Amount))
                            alreadyExists = True
                        x+=1
                    if alreadyExists == False:
                        newline = line[0:len(line)-1]+ItemID+","+Amount+",\n"
                    else:
                        newline = ""
                        updated = False
                        for value in values:
                            if value == ItemID:
                                newline += value + ","+ newValue + ","
                                updated = True
                            elif updated == True:
                                updated = False
                            else:
                                newline += value + ","
                        newline = newline[0:len(newline)-2]+"\n"
                        
                    with open("shoppingCarts.txt", "w") as f1:
                        f1.write("")
                    with open("shoppingCarts.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == cartline:
                                f2.write(newline)
                            else:
                                f2.write(line)
                            i+=1
                    print("\nAdded Item to cart\n")
                else:
                    cartline += 1

        
    def removeItem(self, username, ItemID):
        return
    def SetItemAmount(self, username, ItemID, Amount):
        return
    def GetItemAmount(self, username, ItemID):
        return
    def Checkout(self, username):
        return
