#Product Stock Shortage Report
class Solution:
    def low_stock_products(self, inventory):
        result = []
        #Write your code here
        
        for product, qty in inventory.items():
            if qty < 10:
                result.append(product)
       
        return result