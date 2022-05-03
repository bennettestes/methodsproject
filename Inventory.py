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
        
    def ViewInventoryByCategory(self, Category):
        print("Inventory: " + self.Category)