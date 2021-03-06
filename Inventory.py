from optparse import Values
import Item

class Inventory:
    
            
    def ViewInventory(self):
        print("-------------Inventory-------------\n")
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                #print(value)
                print(value[0] + "  -PRICE: " + value[1] + "  -STOCK: " + value[3] + "  -CATEGORY: " + value[4] + "  -ITEM ID: " + value[2] + "\n")
        
    def ViewInventoryByCategory(self):
        categories = []
        print("-------------Categories-------------\n")
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                if value[4] not in categories:
                    categories.append(value[4])
        i = 1
        for category in categories:
            print("["+str(i)+"] - " +category+"\n")
            i+=1

        while True:
            userInput = input("Choose Category [1-"+str(i-1)+"]")
            category = None

            try:
                category = categories[int(userInput)-1]
                
                print("-------------"+category+ " Inventory-------------\n")
                with open("inventory.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        value = line.split(",")
                        if value[4] == category:
                            print(value[0] + "  -PRICE: " + value[1] + "  -STOCK: " + value[3] + "  -CATEGORY: " + value[4] + "  -ITEM ID: " + value[2] + "\n")
                        
                    return

            except:
                print("Not a valid Category\n")

    def checkIfItemExists(self, itemID):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                if value[2] == itemID:
                    return True
            return False

    def checkStock(self, itemID, amount):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                value = line.split(",")
                if value[2] == itemID:
                    if int(value[3]) >= int(amount):
                        return True
            return False
    
    def getItemNameandPrice(self, itemID):
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[2] == itemID:
                    returnValues = [values[0], values[1]]
                    return returnValues

    def SubtractItemStock(self, itemID, amount):
        itemLine = 0
        with open("inventory.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.split(",")
                if values[2] ==itemID:
                    newValue = str(int(values[3])-int(amount))
                    newLine = ""
                    i = 0
                    for value in values:
                        if i == 3:
                            newLine += newValue + ","
                        else:
                            newLine += value + ","
                        i+=1
                    newLine = newLine[0:len(newLine)-2]+"\n"
                    with open("inventory.txt", "w") as f1:
                        f1.write("")
                    with open("inventory.txt", "a") as f2:
                        i = 0
                        for line in lines:
                            if i == itemLine:
                                f2.write(newLine)
                            else:
                                f2.write(line)
                            i+=1
                else:
                    itemLine += 1
                