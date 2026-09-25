#Write a program to illustrate variable scope using local global and nonlocal variables. 

store_name = "Tech Shop"

def start_shopping():
  
    budget = 100 
    
    def buy_item(cost):
        nonlocal budget
        tax = 5
        
        budget = budget - (cost + tax)
        print("Budget left:", budget)
        
    buy_item(40)  
    buy_item(20)  

def change_store():
  
    global store_name
    store_name = "Mega Mart"
    
print("Store:", store_name)
start_shopping()

change_store()
print("New Store:", store_name)
