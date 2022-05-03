class Item:

    def __init__(self, Name, Price, ItemID, Stock, Category):

        self.Name = Name
        self.Price = Price
        self.ItemID = ItemID
        self.Stock = Stock
        self.Category = Category

    
    def GetName(self):
    
        return self.Name 
    
    def GetPrice(self):
    
        return self.Price
    
    def GetItemID(self):
    
        return self.ItemID
    
    def GetStock(self):
    
        return self.Stock
    
    def GetCategory(self):
    
        return self.Category

    
