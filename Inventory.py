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