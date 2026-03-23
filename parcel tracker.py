ZONES = {
    "local":        50.0,
    "provincial":   120.0,
    "island":       200.0,
    "international": 450.0
}

# rates
FRAGILE_FEE_RATE  = 0.25   # 25% extra on base
BULK_DISCOUNT     = 0.10   # 10% off base if quantity >= 5
MIN_BULK_QTY      = 5      # minimum quantity for bulk discount

# valid
vc = ["y", "n"]

# totals 
total_bulk = 0
total_fragile = 0
grandtotal = 0

# status
bulk_stat = "[BULK: NO]"
fragile_stat = "[NORMAL]"

# bool init
is_fragile = False

# orders and zones
zones = []
shipped = []


def header():
    print()
    print("Welcome to myc's shipping services!")
    print("----------------------------------------------------")
    print("WE OFFER")
    for zone in ZONES:
        print(f"{zone}  =  {ZONES.get(zone)}")
        
    print("----------------------------------------------------")

header()

while True:
    
    print()
    
    # == zone ==
    zone = input("Enter zone: ")
    if zone == "done":
        break
    elif zone not in ZONES:
        print("invalid zone.")
        continue
    
    # == zone fee ==
    rate_per_kg = ZONES.get(zone)
    
    # == weight == 
    while True:
        try: 
            weight = float(input("Enter weight: "))
            
            if weight < 0.1 or weight > 50.0:
                print("Weight cannot be accomodated. Must be only 0.1-50.0 kg")
                continue
            else:
                break
        except ValueError:
            print("Enter only float values")
            continue
        
    # == quantity ==
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Must be positive integer.")
                continue
            else:
                break
        except ValueError:
            print("Invalid value. Only enter numbers")
            continue
    
    
    # is fragile
    while True:
        fragile = input("Is fragile (y/n): ")
        if fragile not in vc:
            print("Invalid input, only input y or n")
        else:
            if fragile == "y": is_fragile = True
            else: is_fragile = False
            break
       
    # == computations == 
    base = rate_per_kg * weight * quantity
    
    if quantity >= 5: 
        bulk_discount = base * BULK_DISCOUNT
        bulk_stat = "[BULK: YES]"
    else: bulk_discount = 0
    total_bulk += bulk_discount
    
    if is_fragile: 
        fragile_fee = base * FRAGILE_FEE_RATE
        fragile_stat = "[FRAGILE]"
    else: fragile_fee = 0
    total_fragile += fragile_fee
    
    subtotal = base - bulk_discount + fragile_fee
    grandtotal += subtotal
    
    # == append ==
    if zone not in zones:
        zones.append(zone)
          
    shipped.append((zone, rate_per_kg, weight, quantity, fragile_stat, bulk_stat, subtotal))
    
    # == confirmation == 
    print("Order added!")
    

# ==== output =====

print("----------------------------------------------------")
print("           WAREHOUSE SHIPPING MANIFEST")
print("----------------------------------------------------")
if len(shipped) == 0:
    print("No parcels recorded.")
    print("----------------------------------------------------")
else:
    cn = 0
    for zone, rate_per_kg, weight, quantity, fragile_stat, bulk_stat, subtotal in shipped:
        cn += 1
        print(f"{cn}. {zone}  |  {weight:.2f} x{quantity}  |  {fragile_stat} {bulk_stat}  =  {subtotal}")

    print("----------------------------------------------------")
    print(f"TOTAL BULK DISCOUNTS = {total_bulk}")
    print(f"TOTAL FRAGILE FEES = {total_fragile}")
    print(f"GRANDTOTAL = {grandtotal}")
    print("----------------------------------------------------")
    print("ZONNE SHIPPED TO:")
    for zone in zones:
        print(f"- {zone}")
    
print()