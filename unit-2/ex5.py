#Write a program to demonstrate the use of break continue and pass statements. 
cart_item=[
    {"name":"laptop","price":900,"status":"available"},
    {"name":"Sneakers","price":80 ,"status":"out_of_stock"},
    {"name":"Book","price":15,"status":"available"},
    {"name":"chamcho","price":0,"status":"blocked"},
]

total_cost=0
print("processing your cart...")
for item in cart_item:
    if item["status"]=="blocked":
        pass
    if item["status"]=="out_of_stock":
        print(f"{item["name"]}is out of stock! skipping...")
        continue
    if item["price"]>1000:
        print(f"Transaction stopped!{item["name"]} exceeds single-item limit")
        total_cost=0
        break
    total_cost=total_cost+item["price"]
    print(f"added {item['name']} to total")
    
print(f"\n final chechout amount:$ {total_cost} ")
