sales_floor_quantity = int(input("How many pieces do you have on the sales floor? "))
stockroom_quantity = int(input("How many pieces do you have in stockroom? "))
total_store_inv = sales_floor_quantity + stockroom_quantity
sr_ratio = stockroom_quantity / total_store_inv * 100
print(f"You stockroom ratio is: {sr_ratio:.2f}")