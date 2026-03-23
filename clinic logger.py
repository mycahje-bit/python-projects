SERVICES = {
    "checkup": 300.0,
    "xray": 850.0,
    "bloodtest": 500.0,
    "vaccination": 200.0
}

# discount rates
SENIOR_DISCOUNT = 0.20       # 20% discount
PRIORITY_FEE_RATE = 0.12     # 12% extra fee

# valid y/n
valid_yn = ["y", "n"]

# status:
s_senior = "[NORMAL]"
s_priority = "[NORMAL]"

# for receipt
availed = []
all_availed = []

# fee init
discount = 0
priority_fee = 0

# bool init
senior = False
priority = False

total_discount = 0
total_priority_fee = 0
grandtotal = 0

def header():
    print()
    print("Welcome to Mycah's Dental Clinic")
    print("------------------")
    print("OUR SERVICES")
    
    for service in SERVICES:
        print(f"- {service}")
        
    print("------------------")
    print()
    print("type 'done' to finish session")
    
header()    

while True:
    
    
    print()
    
    # == service ==
    service = input("How can we help you today?: ").lower().strip()
    if service == "done":
        break
    elif service not in SERVICES:
        print("Invalid service. Kindly refer to our service list.")
        continue
    
    # == fee of service ==
    fee = SERVICES.get(service)
    
    # == sess of service == 
    while True:
        try:
            sessions = int(input("How much of this service will you avail? "))
            if sessions <= 0:
                print("Must be a positive integer")
                continue
            else:
                break
            
        except ValueError:
            print("Invalid value. Enter only a number.")
            continue
    
    # == is senior == 
    while True:
        is_senior = input("Are you a senior citizen (y/n): ").lower() 
        if is_senior not in valid_yn:
            print("Invalid input. Please enter y or n only.")
            continue
        else:
            if is_senior == "y": 
                s_senior = "[SENIOR]" 
                senior = True
            break
    
    # == is_priority == 
    while True:
        is_priority = input("Are you a priority patient (y/n): ").lower()
        if is_priority not in valid_yn:
            print("Invalid input. Please enter y or n only.")
            continue
        else:
            if is_priority == "y": 
                s_priority = "[PRIORITY]"
                priority = True
            break
    
    
    # == computation == 
    base = fee * sessions
    
    if senior: discount = base * SENIOR_DISCOUNT
    else: discount = 0
    
    if priority: priority_fee = base * PRIORITY_FEE_RATE
    else: priority_fee = 0
    
    subtotal = (base - discount) + priority_fee
    
    # == adding == 
    all_availed.append((service, fee, sessions, s_senior, s_priority, subtotal))
    if service not in availed: availed.append(service)
    
    total_discount += discount
    total_priority_fee += priority_fee
    grandtotal += subtotal
        

# == receipt ==
print()
print("------------------------------------------")
print("        CLINIC VISIT SUMMARY")
print("------------------------------------------")

if len(availed) == 0:
    print("No visits recorded.")
    print()
else:
    current_num = 0
    for service, fee, sessions, s_senior, s_priority, subtotal in all_availed:
        current_num += 1
        print(f"{current_num}. {service} x{sessions} {s_senior} {s_priority}  =  {subtotal}")

    print("------------------------------------------")
    print("SERVICES AVAILED:")
    for service in availed:
        print(f"- {service}")
        
    print("------------------------------------------")
    print(f"TOTAL DISCOUNT: {total_discount}")
    print(f"TOTAL PRIORITY FEE: {total_priority_fee}")
    print(f"GRANDTOTAL: {grandtotal}")
    