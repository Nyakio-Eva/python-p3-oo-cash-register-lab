#!/usr/bin/env python3
'''
 the expression self.items = items if items is not None else [] ensures that the items attribute of the CashRegister instance is initialized as an empty list if no items are provided during initialization, and it is assigned the provided list of items if any are provided.A common pattern in Python to handle optional parameters with default values.

self.items.append((title, price, quantity)) = Using double brackets ensures that the tuple itself is treated as a single item in the list, rather than unpacking its elements into separate items.




'''
class CashRegister:
  def __init__(self,items=None,total=0,discount=0) -> None:
    self._total = total
    self._discount = discount
    self._items = items if items is not None else []
    
  
  @property
  def total(self):
    """the total property"""
    return self._total
  
  @total.setter
  def total(self, total):
    self._total = total

  @property
  def discount(self):
    """the discount property"""
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount
  

  @property
  def items(self):
    """the items property"""
    item_list = []  #initialize a list to store titles of items according to quantity
    #iterate over the items in the cashregister instance variable
    for item in self._items:
      #unpack the title and quantity elements of the item tuple into separate variables
      title = item[0]
      quantity = item[2]
      
      for _ in range (quantity): #repeat the title base on quantity
        item_list.append(title)

    #return an array of items added 
    return item_list  
  
  @items.setter
  def items(self,items):
      self._items = items
  
  def add_item(self,title,price,quantity=1):
    """accepts a title and a price and increases the total.Also accepts an optional quantity and doesn't forget about the previous total"""
    
    total_price = price * quantity
    self._total += total_price  #increases the total by price of item
    self._items.append((title,price,quantity)) #add title of item to list
  

  def  apply_discount (self):
    """applies the discount to the total price"""
    if self._discount == 0:
      print("There is no discount to apply.")

    else:
        
      discounted_price = self._total * (self._discount/100)
      discounted_total = self._total - discounted_price
      self._total = discounted_total
      updated_total = int(discounted_total)
      print(f"After the discount, the total comes to ${updated_total}.")
      

  def void_last_transaction(self):
    """subtracts last item from total"""
    #check if there are any items in the list
    if self._items:
      last_item = self._items.pop()   #remove last item from list
      #unpack the last item tuple to obtain the elements
      _, price, quantity = last_item

      total_price = price * quantity
      self._total -= total_price   #subtract total price of item from totals
    
    else:
      print("there is no transaction to void")

      



