student_profile = [
    {
        "student_id": 12345,
        "name": "Joseph",
        "lastname": "Huelgas",
        "age": 24,
        "course": "BSCS",
        "year_level": 3,
        "section": "A"
    },
    {
        "student_id": 12346,
        "name": "Mark",
        "lastname": "Dela Cruz",
        "age": 26,
        "course": "BSIT",
        "year_level": 4,
        "section": "B"
    },
    {
        "student_id": 12347,
        "name": "Jose",
        "lastname": "Rodriguez",
        "age": 21,
        "course": "BSIS",
        "year_level": 1,
        "section": "C"
    }
]

allowed_courses = ("BSCS", "BSIT", "BSIS")
allowed_year_levels = (1, 2, 3, 4)
allowed_sections = ("A", "B", "C", "D")

student_ids = set()
unique_courses = set()
unique_sections = set()

for student in student_profile:
    student_ids.add(student["student_id"])
    unique_courses.add(student["course"])
    unique_sections.add(student["section"])
    
    
# main loop
while True:
    print("\n=== Student Profile Transactional Program ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Count Students")
    print("5. Display Students")
    print("6. Update Student")
    print("7. Display Unique Data")
    print("8. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "8": #Exit
        print("Program ended.")
        break
    elif choice == "1": #Add
        while True:
            try:  
                student_id = int(input("Enter Student ID: "))
            except ValueError:
                print("Only enter valid positive numbers.")
                break
            
            # validation same concept as remove
            exists = False
            for student in student_profile:
                if student["student_id"] == student_id: exists = True
                    

            if exists:
                print("Student ID already exists.")
                break
            elif not exists:
            
                name = input("Enter First Name: ")
                lastname = input("Enter Last Name: ")
                age = int(input("Enter Age: "))
                if age < 15 or age > 100:
                    print("Age is invalid. Only enter ages 15-100") 
                    break
                
                course = input("Enter Course: ")
                if course not in allowed_courses:
                    print("Course is not allowed.")
                    break
                
                year_level = int(input("Enter Year Level: "))
                if year_level not in allowed_year_levels:
                    print("Year level is not valid.")
                    break 
                
                section = input("Enter Section: ")
                if section not in allowed_sections:
                    print("Section is not valid.")
                    break
                
                
                new_student = {
                    "student_id" : student_id,
                    "name" : name,
                    "lastname": lastname,
                    "age" : age,
                    "course" : course,
                    "year_level" : year_level,
                    "section" : section
                }
                
                student_profile.append(new_student)
                print("Student Added Successfully!")
                break
    elif choice == "2": #Remove
        student_id = int(input("Enter Student ID to remove: "))
        
        found = False
        
        for student in student_profile:
            if student["student_id"] == student_id:
                student_profile.remove(student)
                found = True
                print("Student found and removed successfully.")
                
        if not found:
            print("Student not found")
    elif choice == "3": #Search
        student_id = int(input("Enter Student ID to search: "))
        
        found = False
        
        for student in student_profile:
            if student["student_id"] == student_id: found = True
                
                
        if found:
            print()
            for student in student_profile:
                if student["student_id"] == student_id:
                    
                    print("Student found!")
                    print(f"Student ID: {student["student_id"]}")
                    print(f"First Name: {student["name"]}")
                    print(f"Last Name: {student["lastname"]}")
                    print(f"Age: {student["age"]}")
                    print(f"Course: {student["course"]}")
                    print(f"Year Level: {student["year_level"]}")
                    print(f"Section: {student["section"]}")
                        
        elif not found:
            print("Student does not exist.")
    elif choice == "4": #Count
        total_students = len(student_profile)
        print(f"Total number of students: {total_students}")        
    elif choice == "5": #Display
        if len(student_profile) == 0:
            print("No Students found.")
        else:
            for s in range(len(student_profile)):
                id, name, lastname, age, course, level, section = student_profile[s]  
                
                print()
                print(f"Student ID: {student_profile[s].get(id)}")     
                print(f"First Name: {student_profile[s].get(name).upper()}")     
                print(f"Last Name: {student_profile[s].get(lastname).upper()}")     
                print(f"Age: {student_profile[s].get(age)}")     
                print(f"Course: {student_profile[s].get(course)}")     
                print(f"Year Level: {student_profile[s].get(level)}")     
                print(f"Section: {student_profile[s].get(section)}")     
    elif choice == "6": #Update
        student_id = int(input("Enter Student ID to update: "))
        
        found = False
        
        print()
        print("What would you like to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Age")
        print("4. Course")
        print("5. Year Level")
        print("6. Section")
        print("7. Done")
        num = input("Enter choice to update: ")
        
        updated = False
        while True:
            
            for student in student_profile:
                if student["student_id"] == student_id:
                    if num == "7": break
                    elif num == "1":
                        new_val = input("Enter new student first name: ")
                        student |= {"name" : new_val}
                        updated = True
                        break
                    elif num == "2":
                        new_val = input("Enter new student last name: ")
                        student |= {"lastname" : new_val}
                        updated = True
                    elif num == "3":
                        new_val = int(input("Enter new student age: "))
                        student |= {"age" : new_val}
                        updated = True
                    elif num == "4":
                        new_val = input("Enter new student course: ")
                        if new_val not in allowed_courses:
                            print("Course is not allowed.")
                            break
                        else: student |= {"course" : new_val}
                        updated = True
                    elif num == "5":
                        new_val = int(input("Enter new student year level: "))
                        if new_val not in allowed_courses:
                            print("Course is not allowed.")
                            break
                        else: student |= {"year_level" : new_val}
                        
                        updated = True
                    elif num == "6":
                        new_val = input("Enter new student section: ")
                        if new_val not in allowed_courses:
                            print("Course is not allowed.")
                            break
                        else: student |= {"section" : new_val}  
                        updated = True
                
            if updated:
                print("Student info successfully updated")
                break
            else:
                print("No updates were made") 
                break
    elif choice == "7": #Display unique
        if len(student_profile) == 0:
            print("No Students found.")
        else:
            print()
            print(f"Unique Student IDs: {student_ids}")
            print(f"Unique Courses: {unique_courses}")
            print(f"Unique Sections: {unique_sections}")
    