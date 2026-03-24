SUBJECTS = {
    "math":    850.0,
    "science": 900.0,
    "english": 750.0,
    "history": 700.0,
    "pe":      500.0
}

# scholarship rates
SCHOLARSHIP_DISCOUNT = 0.30   # 30% discount on base
LAB_FEE_RATE         = 0.20   # 20% extra on base
MAX_UNITS            = 24     # overload threshold


#list for session
session = []

# totals
total_units = 0
total_discount = 0
total_lab_fee = 0
grandtotal = 0

# valid 
valid_c = ["y", "n"]

# bools
is_scholar = False
is_lab = False
subj_overload = False

# status
scholar_stat = "[REGULAR]"
lab_stat = "[NO LAB]"


# == HEADER ==  
print()
print("Welcome the Py University")
print("----------------------------------------------------")
print("We offer:")
for subject in SUBJECTS:
    print(f"{subject} - {SUBJECTS.get(subject):.2f}")


# main loop
while True:
    print()
    
    #== enrolled bool ==
    is_enrolled = False
    
    # == subject and done ==
    
    subject = input("Enter subject (or 'done'): ")
    if subject == "done":
        break
    elif subject not in SUBJECTS:
        print("Invalid subject. Please try again.")
        continue

    for i in range(len(session)): 
        if session[i][0] == subject: 
            is_enrolled = True
            break   
        
    if is_enrolled: 
        print(f"Already enrolled in {subject}. Try another subject.")
        continue
    
    # == units == 
    while True:
        try:
            units = int(input("Enter units (1-6): "))
            
            if units < 1 or units > 6:
                print("Invalid units. Please enter only 1-6.")
                continue
            else:
                total_units += units 
                break    
                           
        except ValueError:
            print("Only input numbers")
            
            
    # == cost per unit == 
    cost_per_unit = SUBJECTS.get(subject)
    
    
    # == scholar ==
    while True:
        scholar = input("Scholar? (y/n): ")
        if scholar not in valid_c:
            print("Only enter y or n")
            continue
        else:
            if scholar == "y":
                is_scholar = True
                scholar_stat = "[SCHOLAR]"
            else:
                is_scholar = False
                scholar_stat = "[REGULAR]"
            break        
    
    # == lab ==
    while True:
        lab = input("Lab fee? (y/n): ")
        if lab not in valid_c:
            print("Only enter y or n")
            continue
        else:
            if lab == "y":    
                is_lab = True
                lab_stat = "[LAB]"
            else:
                is_lab = False
                lab_stat = "[NO LAB]"
            break
        
        
    # == compute ==
    base = cost_per_unit * units
    
    if is_scholar: discount = base * SCHOLARSHIP_DISCOUNT
    else: discount = 0
    total_discount += discount 
    
    if is_lab: lab_fee = base * LAB_FEE_RATE 
    else: lab_fee = 0
    total_lab_fee += lab_fee
    
    subtotal = base - discount + lab_fee
    grandtotal += subtotal
    
    # == append ==
    session.append((subject, units, scholar_stat, lab_stat, subtotal))
    
    # == save exit == 
    if total_units > 24: 
        print("Warning! Units have exceeded 24.")
        subj_overload = True
    print("Enrollment saved!")
    

print()
print("----------------------------------------------------")
print("         UNIVERSITY ENROLLMENT FORM")
print("----------------------------------------------------")

if len(session) == 0:
    print("No enrollments recorded.")
    print("----------------------------------------------------")
else:
    for i in range(len(session)):
        subject, units, scholar_stat, lab_stat, subtotal = session[i]
        print(f"{i+1}. {subject} |  {units} units  |  {scholar_stat} {lab_stat}  =  {subtotal:.2f}")
           
    print("----------------------------------------------------")
    if subj_overload:
        print("⚠ OVERLOAD WARNING: Total units exceed 24! ⚠ ")
        print("----------------------------------------------------")
        
    
    print(f"TOTAL UNITS ENROLLED = {total_units}")
    print(f"TOTAL DISCOUNT = {total_discount:.2f}")
    print(f"TOTAL LAB FEES = {total_lab_fee:.2f}")
    print(f"GRAND TOTAL = {grandtotal:.2f}")

    print("----------------------------------------------------")
    print("SUBJECTS ENROLLED:")
    for i in range(len(session)):
        subject = session[i][0]
        print(f"- {subject}")
        
    print()