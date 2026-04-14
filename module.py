# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.

print("welcome to Kennedy's market")
print("1. check your cart")
print("2. add to thy cart")
print("3. show total price")
print("4. checkout")
print("5. Exit")
class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    print("\nInitializing POS system...")
    self.cart= []
   
    
  def start(self): # This is the function that should be used to start the application.
    print("\nThe app is not complete.")