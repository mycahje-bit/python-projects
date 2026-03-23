ITEMS = {
"notebook": 45.0,
"pen": 12.0,
"marker": 25.0,
"folder": 18.0
}

# rates
STUDENT_DISCOUNT = 0.10 # 10% discount
RUSH_PACKING_FEE_RATE = 0.15 # 15% extra fee

# cart
orders = []

# valid y and n
valid_disc = ["y", "n"]

# status
s_student = "[NORMAL]"
s_rush = "[NORMAL]"

# items sold
items_sold = []

# total fees
total_disc = 0
total_rush = 0
grandtotal = 0

#fees init
rush_fee = 0
discount = 0

# no of orders
no_of_orders = 0


def show_menu():
    print()
    print("=== SCHOOL SUPPLY MENU ===")
    for items in ITEMS:
        print(f"{items} : {ITEMS.get(items)}")
        
    print("Type done to finish")
    print()

show_menu()

# Main loop
while True:
    
    
    
    item = input("Enter item (or 'done'): ")
    #done finish
    if item == "done":
        break
    elif item not in ITEMS:
        print("Invalid item. Try again.")
        continue
          
    # for price
    price = ITEMS.get(item)

    #Quantity loop
    while True:
        try: 
            quantity = int(input("Enter quantity: "))
    
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
            else: break
                 
        except ValueError:
            print("Invalid input")
            continue


    #disc bools
    student = False
    rush = False

    #Student loop
    while True:
        is_student = input("Student buyer? (y/n): ").lower().strip()
        
        if is_student not in valid_disc:
            print("Invalid choice, type only y or n.")
            continue
        else:
            if is_student == "y":
                s_student = "[STUDENT]"
                student = True
                break 
            elif is_student == "n":   
                s_student = "[NORMAL]"
                student = False
                break
    #Rush loop
    while True:
        is_rush = input("Rush packing? (y/n):  ").lower().strip()
        
        if is_rush not in valid_disc:
            print("Invalid choice, type only y or n.")
            continue
        else:
            if is_rush == "y":
                s_rush = "[RUSH]"
                rush = True
                break
            elif is_rush == "n":   
                s_rush = "[NORMAL]"
                rush = False
                break
            
                
        
    # Totals 
    base = price * quantity

    if student: 
        discount = base * STUDENT_DISCOUNT
        total_disc += discount
    else: discount = 0

    if rush: 
        rush_fee = base * RUSH_PACKING_FEE_RATE
        total_rush += rush_fee
    else: rush_fee = 0

    subtotal = base - discount + rush_fee
    grandtotal += subtotal
    
    # adding item to item sold
    if item not in items_sold:
        items_sold.append(item)
    
    #parsing to cart:
    orders.append((item, quantity, s_student, s_rush, subtotal))
    
    no_of_orders += 1
    
    
    print()
    print("Order saved! ")
    print()
    

# == Out of loop == 

print()
print("------------------------------")
print("SCHOOL SUPPLY RECEIPT")
print("------------------------------")


if no_of_orders == 0:
    print("No orders recorded.")
    print("------------------------------")
else:
    current_num = 0
    for item, quantity, s_student, s_rush, subtotal in orders:
        current_num += 1
        print(f"{current_num}. {item} x{quantity} {s_student} {s_rush} {subtotal:.2f}")
    
    print("------------------------------") 
    print(f"TOTAL DISCOUNT: {total_disc:.2f}")    
    print(f"TOTAL RUSH FEES: {total_rush:.2f}")    
    print(f"GRAND TOTAL: {grandtotal:.2f}")    
        
        
    print("------------------------------") 
    print("ITEMS SOLD:")              
    for item in items_sold:
        
        print(f"- {item}")      

