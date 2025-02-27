#car service staff menu
def car_service_staff(staff_ID):
    def menu():
        print("\n"+"="*40)
        print("{:^40s}".format("**CAR SERVICE STAFF**"))
        print("="*40)
        print("Action Available".center(40))
        print("-"*40)
        # Display Actions Available
        print("1. Register New Car\n2. Update Car Details\n3. View Car List\n4. Delete Disposed Cars\n5. Update Own Profile\n6. Log Out")
        print("-"*40)        
        # Accept staff choice and return
        try:
            choice = int(input("Please select the actions you want to proceed (1, 2, 3,...): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("\n==================")
                print("*ACTION NOT EXIST*")
                print("==================")
        except ValueError:
            print("\n===============")
            print("*INVALID INPUT*")
            print("===============")
            print("Please enter your action in NUMBER (1, 2, 3,...)\n")

    # ACTION 1: Car Resgister Function
    def car_register():
        print("\n"+"="*40)
        print("{:^40s}".format("**CAR REGISTER**"))
        print("="*40)
        import datetime
        # Accept car details
        # Accept car registration number
        while True:
            car_reg_no = input("Enter car registration number in the format AB1234C: ")
            is_existing = False  # check if the registration number already exists in the car.txt file

            with open('car.txt', 'r') as file:
                lines = file.readlines()

            for line in lines:
                car_details = line.strip().split("|")
                if car_reg_no == car_details[1].strip():
                    print("\n=======================================")
                    print("*CAR REGISTRATION NUMBER ALREADY EXIST*")
                    print("=======================================")
                    print("Please try again\n")
                    is_existing = True
                    break  # Exit the for loop if the registration number exists

            # if the flag is set to True, continue the while loop
            if is_existing:
                continue

            # Check the car registration number is in a AB1234C format
            if len(car_reg_no) == 7 and car_reg_no[2:6].isdigit() and car_reg_no[:2].isupper() and car_reg_no[6].isupper():
                break # Loop breaks when car reg no. format correct
            else:
                print("\n================")
                print("*INVALID FORMAT*")
                print("================")
                print("Please enter the data in the AB1234C format\n")     
        # Accept car manufacturer and model details
        while True:
            # Accept car manufacturer details
            car_manufacturer = input("Enter car manufacturer: ").lower()
            try:
                with open('car_model.txt', 'r') as file:
                    lines = file.readlines()
                
                manufacturer_found = False # Set manufacturer found as false
                models = [] # Create list for car model

                for line in lines: 
                    car_info = line.strip().split(" ")
                    if car_manufacturer == car_info[0]:
                        models.append(car_info[1])
                        manufacturer_found = True # if car manufacturer found, set as true

                if manufacturer_found:
                    print(f"------ List of models for {car_manufacturer} ------")
                    for model in models:
                        print(model) # Show the car model that is relevant to the input car manufacturer
                    
                    # Accept car model details
                    car_model = input("Enter car model: ").lower()
                    if car_model in models: 
                        break # Loop breaks when input car model is relevant to input car manufacturer
                    else:
                        print("\n===============================================")
                        print("*CAR MODEL NOT UNDER RELEVANT CAR MANUFACTURER*")
                        print("===============================================")
                        print("Please try again\n")
                else:
                    print("\n============================")
                    print("*CAR MANUFACTURER NOT FOUND*")
                    print("============================")
                    print("Please try again\n")

            except FileNotFoundError:
                print("The file 'car_model.txt' does not exist.")
                return
        # Accept year of manufacturer    
        while True:
            manufacture_year = input("Enter year of manufacturer: ")
            # Ensure the year is in 4 digit
            if len(manufacture_year) != 4:
                print("\n====================================")
                print("*YEAR MUST BE EXACTLY 4 DIGITS LONG*")
                print("====================================")
                print("Please try again\n")
                continue
            # Ensure the year are in digit form
            if not manufacture_year.isdigit():
                print("\n===============================")
                print("*YEAR MUST CONTAIN ONLY DIGITS*")
                print("===============================")
                print("Please try again\n")                
                continue
            # Convert to integer
            manufacture_year_int = int(manufacture_year)
            # Ensure the year is between 2000 and 2024
            if manufacture_year_int < 2000 or manufacture_year_int > 2024:
                print("\n====================================")
                print("*YEAR MUST BE BETWEEN 2000 AND 2024*")
                print("====================================")
                print("Please try again\n")
                continue
            else:
                break # Loop breaks when all condition fullfilled
        # Accept car capacity details
        while True:
            capacity = input("Enter the capacity of the car: ")
            if capacity.isdigit() and int(capacity) in [4, 7, 9]:
                capacity = int(capacity)
                break
            else:
                print("\n====================================")
                print("*SEATING CAPACITY MUST BE IN DIGITS*")
                print("           *4 OR 7 OR 9*")
                print("====================================\n")

        #Accept last service date 
        while True:
            last_service_date = input("Enter last service date(dd-mm-yyyy): ")
            # split the date into integers
            try:
                day,month,year= map(int,last_service_date.split('-'))
                # convert into date format
                last_service_date = datetime.datetime.strptime(last_service_date,"%d-%m-%Y")
                # set today's date
                today = datetime.datetime.now()
                # Ensure the date is larger than today's date
                if last_service_date > today:
                    print("\n==============")
                    print("*INVALID DATE*")
                    print("==============")
                    print("Date cannot be greater than today's date\n")
                # Ensure the date is larger than the year of manufacturer
                elif year < manufacture_year_int:
                    print("\n==============")
                    print("*INVALID DATE*")
                    print("==============")
                    print("Date cannot be earlier than the year of manufacturer\n")
                else:
                    break # loop breaks when all condition met
            except ValueError:
                print("\n==============")
                print("*INVALID DATE*")
                print("==============")
                print("Enter the Last Service Date in DD-MM-YYYY format\n")
        # Convert to string to write into car.txt file
        last_service_date_str = last_service_date.strftime("%d-%m-%Y")
        # Accept insurace policy number
        while True:
            insurance = input("Enter insurance policy number in the format of AB123456: ")
            is_existing = False  # check if the insurance policy number already exists in the car.txt file

            with open('car.txt', 'r') as file:
                lines = file.readlines()

            for line in lines:
                car_details = line.strip().split("|")
                if insurance == car_details[7].strip():
                    print("\n=======================================")
                    print("*INSURANCE POLICY NUMBER ALREADY EXIST*")
                    print("=======================================")
                    print("Please enter a unique insurance policy number\n")
                    is_existing = True
                    break  # Exit the for loop if the insurance policy number exists

            # if the flag is set to True, continue the while loop
            if is_existing:
                continue
            # Ensure insurance policy is in the AB123456 format
            if len(insurance) == 8 and insurance[:2].isupper() and insurance[2:8].isdigit():
                break
            else:
                print("\n================")
                print("*INVALID FORMAT*")
                print("================")
                print("Please enter the data in AB123456 format\n")     
        # Accept insurance expiry date
        while True:
            insurance_expiry_date = input("Enter insurance policy expiry date(dd/mm/yyyy): ")
            try:
                # convert into date format
                insurance_expiry_date = datetime.datetime.strptime(insurance_expiry_date,"%d-%m-%Y")
                # set today's date
                today = datetime.datetime.now()
                # Ensure date is larger than today's date
                if insurance_expiry_date > today:
                    break
                else:
                    print("\n==============")
                    print("*INVALID DATE*")
                    print("==============")
                    print("Insurance Expiry Date cannot be earlier and equal to today's date\n")
            except ValueError:
                print("\n==============")
                print("*INVALID DATE*")
                print("==============")
                print("Enter the date in DD-MM-YYYY format\n")
        # Convert to string to write into car.txt file
        insurance_expiry_date_str = insurance_expiry_date.strftime("%d-%m-%Y")
        # Accept road tax expiry date
        while True:
            roadtax_expiry_date = input("Enter road tax expiry date(dd/mm/yyyy): ")
            try:
                # Convert into date format
                roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry_date,"%d-%m-%Y")
                today = datetime.datetime.now()
                # Ensure date is larger than today's date
                if roadtax_expiry_date > today:
                    break
                else:
                    print("\n==============")
                    print("*INVALID DATE*")
                    print("==============")
                    print("Road Tax Expiry Date cannot be earlier and equal to today's date\n")
            except ValueError:
                print("\n==============")
                print("*INVALID DATE*")
                print("==============")
                print("Enter the date in DD-MM-YYYY format\n")
        # Convert to string to write into car.txt file
        roadtax_expiry_date_str = roadtax_expiry_date.strftime("%d-%m-%Y")
        # Set renting rate through car seating capacity
        renting_rate = 0 # set renting rate to 0 at first
        if capacity ==4:
            renting_rate = 200
        elif capacity == 7:
            renting_rate = 300
        elif capacity == 9:
            renting_rate = 400
        # Rental Availability set as available
        rental_availability = "AVAILABLE"
    # Open car.txt file as car to record data
        with open('car.txt','a') as car:
            car.write("|")
            car.write(str(car_reg_no).center(13))
            car.write("|")
            car.write(str(car_manufacturer).center(17))
            car.write("|")
            car.write(str(car_model).center(13))
            car.write("|")
            car.write(str(manufacture_year).center(18))
            car.write("|")
            car.write(str(capacity).center(13))
            car.write("|")
            car.write((last_service_date_str.center(18)))
            car.write("|")
            car.write(str(insurance).center(15))
            car.write("|")
            car.write(insurance_expiry_date_str.center(22))
            car.write("|")
            car.write(roadtax_expiry_date_str.center(22))
            car.write("|")
            car.write(str(f"RM{renting_rate}").center(13))
            car.write("|")
            car.write(rental_availability.center(13))
            car.write("|")
            car.write('\n')
        header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
        print("------------------------------------------------------------------------------**New Car Details**--------------------------------------------------------------------------------------------")
        print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        with open ('car.txt','r') as file:
            lines = file.readlines()
            new_cardetails = lines[-1]
            print(new_cardetails)

        

    # Action 2: Update Car Details Function
    def update_car_details():
        import datetime
        import css
        # Accept car registration number to change the car details
        with open('car.txt', 'r') as file:
            # Read the file content
            car_details = file.read()
            # Print the file content
            header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
            print("--------------------------------------------------------------------------------**Car Details**----------------------------------------------------------------------------------------------")
            print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")            
            print(car_details)
            
        print("**UPDATE CAR DETAILS*")
        car_reg_no = input("Enter the car registration number to modify the car details: ")

        while True:
            try:
                with open('car.txt', 'r') as file:
                    lines = file.readlines()
                
                for i, line in enumerate(lines):
                    details = line.strip().split("|") # split each line car details
                    if car_reg_no == details[1].strip():
                        header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
                        print("--------------------------------------------------------------------------------**Car Details**----------------------------------------------------------------------------------------------")
                        print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print(line.strip())
                        print("**UPDATE CAR DETAILS**\n1.Insurance Policy Number\n2.Insurance Expiry Date\n3.Road Tax Expiry Date\n4.Car Renting Rate\n5.Car Availability\n")

                        while True:
                            try:
                                choice = int(input("Please enter your selection in number (1/2/3/4/5): "))
                                if 1 <= choice <= 5:
                                    break
                                else:
                                    print("\n==================")
                                    print("*ACTION NOT EXIST*")
                                    print("==================")
                                    print("Please try again\n")
                            except ValueError:
                                print("\n===============")
                                print("*INVALID INPUT*")
                                print("===============")
                                print("Enter a valid number\n")
                        
                        # **Update new details**
                        # if key in choice as 1
                        if choice == 1:
                            print("\n===============================")
                            print("*UPDATE INSURANCE POLICY NUMBER*")
                            print("===============================")
                            while True:
                                # Accept new insurance policy number details 
                                insurance = input("Enter new insurance policy number in the format of AB123456: ")
                                existing_insurance_number = {line.strip().split("|")[7].strip() for line in lines if len(line.strip().split(" ")) > 7}
                                
                                if len(insurance) == 8 and insurance[:2].isupper() and insurance[2:8].isdigit(): # Ensure insurance policy is in the AB123456 format
                                    if insurance not in existing_insurance_number: # Ensure new insurance policy number is not exist before in the car.txt file
                                        # replace existing insurance policy number to a new one
                                        lines[i] = line.replace(details[7],insurance.center(15))
                                        # write into car.txt file
                                        with open('car.txt', 'w') as car:
                                            car.writelines(lines)
                                        break 
                                    else:
                                        print("\n=======================================")
                                        print("*INSURANCE POLICY NUMBER ALREADY EXIST*")
                                        print("=======================================")
                                        print("Please enter a unique insurance policy number\n")
                                else:
                                    print("\n================")
                                    print("*INVALID FORMAT*")
                                    print("================")
                                    print("Please enter the data in AB123456 format\n")     
                            
                        # if key in choice as 2
                        if choice == 2:
                            print("\n==============================")
                            print("*UPDATE INSURANCE EXPIRY DATE*")
                            print("==============================")
                            while True:
                                # Accept new insurance expiry date details
                                insurance_expiry_date = input("Enter new insurance policy expiry date (DD-MM-YYYY): ")
                                try:
                                    insurance_expiry_date = datetime.datetime.strptime(insurance_expiry_date, "%d-%m-%Y")
                                    today = datetime.datetime.now()
                                    current_insurance_expiry_date = datetime.datetime.strptime(details[8].strip(), "%d-%m-%Y")
                                    # Calculate the date one year from the current insurance expiry date
                                    one_year_from_current_expiry = current_insurance_expiry_date + datetime.timedelta(days=365)

                                    # Ensure the new date is larger than today's date
                                    if insurance_expiry_date < today:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Insurance Expiry Date cannot be smaller than today's date\n")
                                    # Ensure the new date is not same and larger than the existing date in the car.txt file
                                    elif insurance_expiry_date <= current_insurance_expiry_date:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Insurance Expiry Date cannot be the same or smaller than the existing date\n")
                                    # Ensure the new date is more than one year from the existing insurance expiry date in the car.txt file
                                    elif insurance_expiry_date < one_year_from_current_expiry:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Insurance Expiry Date must be more than one year from the current expiry date\n")
                                    else:
                                        # Convert to string to write into car.txt file
                                        insurance_expiry_date_str = insurance_expiry_date.strftime("%d-%m-%Y")
                                        # replace existing insunrace expiry date to a new one 
                                        lines[i] = line.replace(details[8],insurance_expiry_date_str.center(22))
                                        # write into car.txt file
                                        with open('car.txt', 'w') as car:
                                            car.writelines(lines)
                                        break
                                except ValueError:
                                    print("\n==============")
                                    print("*INVALID DATE*")
                                    print("==============")
                                    print("Enter the date in DD-MM-YYYY format\n")

                        # if key in choice as 3
                        if choice == 3:
                            print("\n=============================")
                            print("*UPDATE ROAD TAX EXPIRY DATE*")
                            print("=============================")                            
                            while True:
                                # Accept new road tax expiry date details
                                roadtax_expiry_date = input("Enter new road tax expiry date(dd/mm/yyyy): ")
                                # Ensure that road tax expiry date is greater than current date
                                try:
                                    roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry_date,"%d-%m-%Y")
                                    today = datetime.datetime.now()
                                    current_roadtax_expiry_date = datetime.datetime.strptime(details[9].strip(),"%d-%m-%Y")
                                    # Calculate the date one year from the current road tax expiry date
                                    one_year_from_current_expiry = current_roadtax_expiry_date + datetime.timedelta(days=365)
                                    # Ensure road tax expiry date greter than today's date
                                    if roadtax_expiry_date < today:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Road Tax Expiry Date cannot be smaller than today's date\n")
                                    # Ensure road tax expiry date greater than the existing date in the car.txt file                           
                                    elif roadtax_expiry_date <= current_roadtax_expiry_date:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Road Tax Expiry Date cannot be the same or smaller than the existing date\n")
                                    # Ensure the new date is more than one year from the existing insurance expiry date in the car.txt file
                                    elif roadtax_expiry_date < one_year_from_current_expiry:
                                        print("\n==============")
                                        print("*INVALID DATE*")
                                        print("==============")
                                        print("New Road Tax Expiry Date must be more than one year from the current expiry date\n")                                       
                                    else:
                                        # Convert to string to write into car.txt file
                                        roadtax_expiry_date_str = roadtax_expiry_date.strftime("%d-%m-%Y")
                                        # replace existing road tax expiry date to a new one
                                        lines[i] = line.replace(details[9],roadtax_expiry_date_str.center(22))
                                        # write into car.txt file
                                        with open('car.txt', 'w') as car:
                                            car.writelines(lines)                                
                                        break
                                except ValueError:
                                    print("\n==============")
                                    print("*INVALID DATE*")
                                    print("==============")
                                    print("Enter the date in DD-MM-YYYY format\n")

                        # if key in choice as 4
                        if choice == 4:
                            print("\n=========================")
                            print("*UPDATE CAR RENTING RATE*")
                            print("=========================")                            
                            # Accept new car renting rate
                            while True:
                                car_renting_rate = input("Enter the new Car Renting Rate per day: ")
                                # replace existing car renting rate to a new one
                                if car_renting_rate.isdigit():
                                    lines[i] = line.replace(details[10],f"RM{car_renting_rate}".center(13))
                                    with open('car.txt', 'w') as car:
                                        car.writelines(lines) 
                                        break  
                                else:
                                    print("\n===============")
                                    print("*INVALID INPUT*")
                                    print("===============")
                                    print("Enter a valid number\n")

                        # if key in choice as 5
                        if choice == 5: 
                            print("\n=========================")
                            print("*UPDATE CAR AVAILABILITY*")
                            print("=========================")
                            while True:
                                # Accept new availability of car details
                                car_availability = input("\n*Available*\n*Reserved*\n*Rented*\n*Under Service*\n*Disposed*\nEnter the new car_availability details:").upper()
                                if car_availability == "AVAILABLE" or car_availability == "RESERVED" or car_availability == "RENTED" or car_availability== "UNDER SERVICE" or car_availability == "DISPOSED":
                                    # replace new availability of car as a new one
                                    lines[i] = line.replace(details[11],car_availability.center(13))
                                    with open('car.txt', 'w') as car:
                                        car.writelines(lines) 
                                    break # loop breaks when condition met
                                else: 
                                    print("\n=================")
                                    print("*INVALID DETAILS*")
                                    print("=================")

                        print("\n=====================")
                        print("*UPDATED SUCESSFULLY*")
                        print("=====================")
                        header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
                        print("------------------------------------------------------------------------------**Updated Car Details**----------------------------------------------------------------------------------------")
                        print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        
                        if car_reg_no == details[1].strip(): #Show the changes of the car details
                            print(lines[i],end="")
                        return

                print("\n===============")
                print("*CAR NOT FOUND*")
                print("===============")
                print("Please try again\n")


                car_reg_no = input("Enter the existing car registration number: ")  

            except FileNotFoundError:
                print("The file 'car.txt' does not exist.")
                return

    # Action 3: View Car List in Table Format
    def view_carlist_table():
        print("\n"+"="*40)
        print("{:^40s}".format("**VIEW CAR LIST**"))
        print("="*40)
        header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
        print("----------------------------------------------------------------------------------**Car Details**--------------------------------------------------------------------------------------------")
        print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        with open('car.txt', 'r') as file:
            # Read the file content
            car_details = file.read()
            # display the file content
            print(car_details)

    #Action 4: Delete Disposed Cars
    def delete_disposed_cars():
        print("\n"+"="*40)
        print("{:^40s}".format('**DELETE "DISPOSED" CAR**'))
        print("="*40)
        try:
            with open('car.txt', 'r') as file:
                lines = file.readlines()

            disposed_cars = [line for line in lines if "disposed" in line.lower()]
            remaining_cars = [line for line in lines if "disposed" not in line.lower()]

            if not disposed_cars:
                print("\n==================")
                print("*NO DISPOSED CARS*")
                print("==================")
                return
            
            header = ["Car_reg No.","Car Manufacturer","Car Model","Manufacture Year","Capacity","Last Service Date","Insurance No.","Insurance Expiry Date","RoadTax Expiry Date","Rental Rate","Availability"]
            print("-----------------------------------------------------------------------------**DISPOSED Car Details**----------------------------------------------------------------------------------------")
            print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

            for car in disposed_cars:
                print(car)  # Display the disposed cars

            # Loop until user input either yes or no
            while True:
                confirmation = input("\nDo you want to delete all disposed cars? (yes/no): ")
                if confirmation.lower() == "yes":
                    with open('car.txt', 'w') as file:
                        file.writelines(remaining_cars)  # Write the remaining cars

                    print("\n====================================")
                    print("*DISPOSED CARS DELETED SUCCESSFULLY*")
                    print("====================================")
                    break  # Exit the loop after deleted disposed cars
                elif confirmation.lower() == "no":
                    print("\n======================")
                    print("*OPERATION CANCELLED*")
                    print("*No cars were deleted*")
                    print("======================\n\n")
                    break  # Exit the loop if operation is cancelled
                else:
                    print("\n===============")
                    print("*INVALID ENTRY*")
                    print("===============")
                    print("Enter 'Yes' or 'No' only.")

        except FileNotFoundError:
            print("The file 'car.txt' does not exist.")

    # Action 5: Update Own Profile
    def update_profile(ID):
        print("\n==============================================================================================================")
        print("{:^104s}".format("**PROFILE**"))
        print("==============================================================================================================")
        # Display Staff Information
        menu = ["Staff ID","Name","Role","Password","Registered Date"]
        updated_lines = []
        # Open staff file and print the staff's profile
        for lines in open("staff.txt",'r'):
            staff_info = lines.split("|")
            if staff_info[1].strip() == ID:
                print(f"|{menu[0] :^20s}|{menu[1] :^20s}|{menu[2] :^24s}|{menu[3] :^20s}|{menu[4] :^20s}|")
                print("--------------------------------------------------------------------------------------------------------------")
                print(lines)
                print("UPDATE PROFILE:\n1.Staff ID\n2.Name\n3.Password\n")
                # Select item to update
                while True:
                    try:
                        choice = int(input("Please enter your selection in number (1/2/3): "))
                        if choice <= 3:
                            break
                        else:
                            print("** Action does not exist. Please try again. **\n")
                    except ValueError:
                        print("** Invalid input. Please enter a valid number. **\n")
                # Define user selection
                if choice == 1:
                    # Update staff ID
                    new_staff_ID = input("Enter your new staff ID: ")
                    staff_info[1] = new_staff_ID.center(20)
                    ID = new_staff_ID
                elif choice == 2:
                    # Update staff name
                    new_staff_name = input("Enter your new name: ")
                    staff_info[2] = new_staff_name.center(20)
                elif choice == 3:
                    # Update password
                    new_password = input("Enter your password: ")
                    staff_info[4] = new_password.center(20)
                updated_lines.append("|".join(staff_info).strip())
            else:
                updated_lines.append(lines.strip())
        # Open staff filr and write updated line
        with open("staff.txt", "w") as staff:
            for updated_line in updated_lines:
                staff.write(updated_line + "\n")
        # Open staff file and display the updated line of the staff
        for lines in open("staff.txt",'r'):
            staff_info = lines.split("|")
            if staff_info[1].strip() == ID:
                print("\n==============================================================================================================")
                print("{:^104s}".format("**UPDATED PROFILE**"))
                print("==============================================================================================================")
                print(f"|{menu[0] :^20s}|{menu[1] :^20s}|{menu[2] :^24s}|{menu[3] :^20s}|{menu[4] :^20s}|")
                print("--------------------------------------------------------------------------------------------------------------")
                print(lines)
        return ID        
            

    choice = menu()

    if choice == 1:
        car_register()
        return staff_ID
    elif choice == 2:
        update_car_details()
        return staff_ID
    elif choice == 3:
        view_carlist_table()
        return staff_ID
    elif choice == 4:
        delete_disposed_cars()
        return staff_ID
    elif choice == 5:
        staff_ID = update_profile(staff_ID)
        return staff_ID
    elif choice == 6:
        return False

