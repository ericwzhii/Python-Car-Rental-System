def cus_service_staff2(staff_ID):
    import datetime as dt

    # Check customer ID format
    def is_valid_cusID(cus_ID):
        return cus_ID.startswith('C') and cus_ID[1:].isdigit() and len(cus_ID) ==  7
    
    # Check car register number format
    def is_valid_car(car_no):
        return car_no[:2].isalpha() and car_no[2:6].isdigit() and car_no[6:].isalpha()
    
    def car_is_registered(car_no):
        # Open car.txt file to check if the car is registered in the car.txt file
        for line in open("car.txt",'r'):
            car_info = line.split("|")
            # If the car is in the car register file return TRUE
            if car_info[1].strip() == car_no:
                return True
        return False
                
    def cus_is_registered(cus_id):      
        # Open customer.txt file to check if the customer is registered in the customer.txt file
        for line in open("customer.txt",'r'):
            cus_info = line.split("|")
            # Return TRUE if the customer is registered
            if cus_info[1].strip() == cus_id:
                return True
        return False

    # Check car's availability
    def car_is_available(car_no):
        for lines in open("car.txt","r"):                   
            car_info = lines.strip().split("|")
            # Return TRUE if the car given is available
            if car_info[1].strip() == car_no and car_info[11].strip() == "AVAILABLE":
                return True
        return False

    # Customer Service Staff 2 Menu
    def menu():
        print("\n"+"="*40)
        print("{:^40s}".format("**CUSTOMER SERVICE STAFF 2**"))
        print("="*40)
        print("Action Available".center(40))
        print("-"*40)
        # Display Actions Available
        print("1.Check Cars' Availability\n2.Accept and Record Rental Details\n3.Generate Bills\n4.Return Car\n5.View Rental Transaction\n6.Delete Transaction\n7.Update Own Profile\n8.Log Out")
        print("-"*40)        
        # Accept staff choice and return
        while True:
            try:
                choice = int(input("Please enter your selection in number (1, 2, 3...): "))
                if choice <= 8 and choice >= 1:
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

    # Check car availability function
    def check_availability():
        print("\n="+"="*39)
        print("{:^40s}".format("**CHECK CAR AVAILABILITY**"))
        print("="*40)
        # Default value for car available
        car_available = False
        # Accept request of paseenger from customer
        while True:
            passenger = input("\nEnter passenger number: ")
            # Check user's input
            if passenger.isdigit(): 
                break
            else:
                print("** Invalid Entry **")
        cars = []
        # Open car.txt file to read for the car availability
        for line in open('car.txt','r'):
            car_info = line.split("|")
            # Convert string data type (car_info[5]) into integer data type to make arithmetic comparison
            car_passenger = int(car_info[5].strip())
            # Show the car that are available and met the customer's requirements
            if int(passenger) <= car_passenger and car_info[11].strip() == "AVAILABLE":
                cars.append(line)
                # Change car available to TRUE
                car_available = True

        if car_available == True:
            header = ["Car Reg Num", "Manufacturer", "Car Model", "Year", "Capacity", "L_Svcs Date", "Insurance", "Ins_Exp_Date", "RTax Exp_Date", "Rate/Day", "Status"]
            print("-"*189)
            print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
            print("-"*189)
            for car in cars:
                print(car,end="")
        # Action if no car is available
        if car_available == False:
            print("\n"+"*"*40)
            print("{:^40s}".format("**NO CAR AVAILABLE**"))
            print("*"* 40)
            

    def rental_transaction():
        print("\n="+"="*39)
        print("{:^40s}".format("**NEW RENTAL TRANSACTION**"))
        print("="*40)
        while True:
            # Enter car registration number for record
            car_reg_no = input("Enter car register number: ")
            # Check is the car registered and available and it is input in a valid format
            if car_is_registered(car_reg_no) and car_is_available(car_reg_no) and is_valid_car(car_reg_no):
                    break   
            # If the car register number input is in wrong format
            elif not is_valid_car(car_reg_no):
                print("** Invalid car register number. **\n")
            # If the car is not registered
            elif not car_is_registered(car_reg_no):
                print("*"*40)
                print("{:^40s}".format("**CAR IS NOT REGISTERED**"))
                print("*"*40)
                return
            # If the car is not available
            elif not car_is_available(car_reg_no):
                print("*"*40)
                print("{:^40s}".format("**CAR IS NOT AVAILABLE**"))
                print("*"*40)
                return
        
        while True:
            # Get customer ID
            cus_ID = input("Enter customer ID: ")
            # Check if the customer is registered and it is input in a correct format
            if cus_is_registered(cus_ID) and is_valid_cusID(cus_ID):
                break
            # If the format of customer ID is wrong
            elif not is_valid_cusID(cus_ID):
                print("** Invalid customer ID. **\n")
            # If the customer is not registered
            elif not cus_is_registered(cus_ID):
                print("*"*40)
                print("{:^40s}".format("**CUSTOMER IS NOT REGISTERED**"))
                print("*"*40)
                return

        # Get rental date
        while True:
            rental_date = input("Enter rental date(DD-MM-YYYY): ")
            # Make sure the date entered is following the format DD-MM-YYYY
            try:
                dt.datetime.strptime(rental_date,"%d-%m-%Y")
                # Check if the date is greater than today's date
                if dt.datetime.strptime(rental_date,"%d-%m-%Y") < dt.datetime.now():
                    print("**Invalid Date Input.**\n")
                elif dt.datetime.strptime(rental_date,"%d-%m-%Y") >= dt.datetime.now():
                    break
            except ValueError:
                print("** Please enter date in format DD-MM-YYYY **\n")

        # Get return date
        while True:
            return_date = input("Enter return date(DD-MM-YYYY): ")
            # Make sure the date entered is following the format DD-MM-YYYY
            try:
                dt.datetime.strptime(return_date,"%d-%m-%Y")
                # Check is the return date given is after the rental date
                if dt.datetime.strptime(return_date,"%d-%m-%Y") <= dt.datetime.strptime(rental_date,"%d-%m-%Y"):
                    print("**The return date can't be earlier than the rental date.**")
                elif dt.datetime.strptime(return_date,"%d-%m-%Y") >= dt.datetime.strptime(rental_date,"%d-%m-%Y"):
                    break
            except ValueError:
                print("\n** Please enter date in format DD-MM-YYYY. **")

        # Calculate the rental period
        rental_period = dt.datetime.strptime(return_date,"%d-%m-%Y") - dt.datetime.strptime(rental_date,"%d-%m-%Y")

        # Convert rental_period into integer for calculation
        rental_period = rental_period.days

        # open car.txt to get the car renting rate per day
        for lines in open("car.txt",'r'):
            car_info = lines.split("|")
            if car_info[1].strip() == car_reg_no:
                # Split the string from RM999 to 999 for converting it to integer
                price = int(car_info[10][6:])
        
        # Calculate the total renting price
        total = int(price)*rental_period

        # Open rental.txt file and insert rental date, return date, rental period and rental price
        with open("rental.txt",'a') as rental:
            rental.write(f"|{car_reg_no:^20s}|{cus_ID:^20s}|{rental_date :^20s}|{return_date :^20s}|{str(rental_period) :^20s}|{str(total) :^20s}|\n")  
        
                # To store modified lines
        updated_lines = []
        # Open car file to update the availability from "AVAILABLE" to "RESERVED"
        with open("car.txt", "r") as file:
            for line in file:
                car_info = line.split("|")
                if car_info[11].strip() == "AVAILABLE" and car_info[1].strip() == car_reg_no:
                    car_info[11] = car_info[11].replace(car_info[11], "{:^13s}".format("RESERVED"))
                updated_lines.append("|".join(car_info))
        # Write the updated line into car file
        with open("car.txt", "w") as car:
            for updated_line in updated_lines:
                car.write(updated_line)
        
        print("\n="+"="*39)
        print("{:^40s}".format("**RENTAL TRANSACTION ACCEPTED**"))
        print("="*40)
        print("-"*40)
        print(f"Car Rented:    {car_reg_no}\nCustomer ID:   {cus_ID}\nRental Date:   {rental_date} ~ {return_date}\nRental Period: {rental_period} days\nTotal Price:   RM{total}")
        print("-"*40)

    def generate_bill():
        print("\n="+"="*39)
        print("{:^40s}".format("**GENERATE BILL**"))
        print("="*40)
        # Create empty list to store customers rental transaction
        bill_info = []
        # Create empty lost to store the transaction that has not been paid
        available_bill = []
        # Set a default value for the rental transaction to be paid
        choice = 1
        # Get customer ID
        while True:
            cus_ID = input("Enter customer ID: ")
            if is_valid_cusID(cus_ID):
                break
            else:
                print("**Invalid customer ID.**\n")
    
        # Open rental.txt file
        with open("rental.txt","r") as rental:
            # Default value for found_transaction
            found_transaction = False

            for lines in rental:
                rental_info = lines.split("|")
                # Get customer's rental transaction
                if cus_ID == rental_info[2].strip() and dt.datetime.strptime(rental_info[3].strip(),"%d-%m-%Y") > dt.datetime.now():
                    # Add customer's rental info into bill info
                    bill_info.append(rental_info)
                    # Change found transaction to TRUE if rental transaction found
                    found_transaction = True
            # Open car.txt file to check weather the transaction is paid or not 
            for lines in open("car.txt","r"):
                car_info = lines.split("|")
                for i in range(len(bill_info)):
                    # If the transaction is not yet paid, add it into available_bill
                    if car_info[1].strip() == bill_info[i][1].strip() and car_info[11].strip() == "RESERVED":
                        available_bill.append(bill_info[i])
                    # If the customer has more than one rental transactions
            if len(available_bill) > 1:
                # Ask the staff to select the rental transaction for billing if the cusotmer has more than one rental transaction
                print("="*40)
                print("**This customer has more than one rental transaction.**")
                print("="*40)
                header = ["Car_Reg Number", "Customer ID", "Rental Date", "Return Date", "Rental Period", "Total Price"]
                print("-------------------------------------------------------------------------------------------------------------------------------")
                print(f"{header[0]:^20s}|{header[1]:^20s}|{header[2]:^20s}|{header[3]:^20s}|{header[4]:^20s}|{header[5]:^20s}")
                print("-------------------------------------------------------------------------------------------------------------------------------")
                # Display all the rental transaction records of the customer
                for item in available_bill:
                    print(f"|{item[1]}|{item[2]}|{item[3]}|{item[4]}|{item[5]}|{item[6]}")

                # Select rental transaction for bill
                while True:
                    try:
                        choice = int(input("Please enter your selection in number (1, 2, 3...): "))
                        if choice <= len(available_bill):
                            break
                        else:
                            print("** Out of index. Please try again. **")
                    except ValueError:
                        print("** Invalid entry. Please enter your choice in number. **")
 
                print("\n==================================================================")
                print("{:^60s}".format("*****INVOICE*****"))
                print("==================================================================")
                print(f"Customer ID: {available_bill[choice-1][2].strip()}\nCar Rented: {available_bill[choice-1][1].strip()}\nRental Period: {available_bill[choice-1][3].strip()} ~ {available_bill[choice-1][4].strip()} ({available_bill[choice-1][5].strip()}) DAYS\nTotal Price: RM{available_bill[choice-1][6].strip()}")
                print("--------------")
                print("*****PAID*****")
                print("--------------")

                updated_lines = []
                # Open car file and change the car selected for bill's availability from "RESERVED" to "RENTED"
                with open("car.txt", "r") as file:
                    for line in file:
                        car_info = line.split("|")
                        if car_info[11].strip() == "RESERVED" and car_info[1].strip() == available_bill[choice-1][1].strip():
                            car_info[11] = car_info[11].replace(car_info[11],"{:^13s}".format("RENTED"))
                        # Join the modified car info back into a line
                        updated_lines.append("|".join(car_info))  
                # Write the updated lines back to the file
                with open("car.txt", "w") as car:
                    for updated_line in updated_lines:
                        car.write(updated_line)        

            # If there is only one rental transaction for the customer
            if len(available_bill) == 1:
                for lines in open("car.txt","r"):
                    car_info = lines.split("|")
                    if available_bill[0][1].strip() == car_info[1].strip() and car_info[11].strip() == "RESERVED":
                        print("\n==================================================================")
                        print("{:^60s}".format("*****INVOICE*****"))
                        print("==================================================================")
                        print(f"Customer ID: {available_bill[0][2].strip()}\nCar Rented: {available_bill[0][1].strip()}\nRental Period: {available_bill[0][3].strip()} ~ {available_bill[0][4].strip()} ({available_bill[0][5].strip()}) DAYS\nTotal Price: RM{available_bill[0][6].strip()}")
                        print("--------------")
                        print("*****PAID*****")
                        print("--------------")
                updated_lines = []
                # Open car file and change the car selected for bill's availability from "RESERVED" to "RENTED"
                with open("car.txt", "r") as file:
                    for line in file:
                        car_info = line.split("|")
                        if car_info[11].strip() == "RESERVED" and car_info[1].strip() == available_bill[0][1].strip():
                            car_info[11] = car_info[11].replace(car_info[11],"{:^13s}".format("RENTED"))
                        # Join the modified car info back into a line
                        updated_lines.append("|".join(car_info))  
                # Write the updated lines back to the file
                with open("car.txt", "w") as car:
                    for updated_line in updated_lines:
                        car.write(updated_line)   
            elif not cus_is_registered(cus_ID):
                print("\n"+"*"*40)
                print("{:^40s}".format("**CUSTOMER NOT FOUND**"))
                print("*"*40)
            elif len(available_bill) < 1:
                print("\n"+"*"*40)
                print("{:^40s}".format("**NO PENDING TRANSACTION**"))
                print("*"*40)

    def return_car():
        print("\n="+"="*39)
        print("{:^40s}".format("**RETURN CAR**"))
        print("="*40)
        # Default value for record found
        record_found = False
        # Open rental file and display the transaction record if the date return is equal or greater than today
        available_record = []
        for lines in open("rental.txt","r"):
            line = lines .split("|")
            for lines in open("car.txt",'r'):
                car_info = lines.split("|")
                if dt.datetime.strptime(line[4].strip(),"%d-%m-%Y") <= dt.datetime.now() and (line[1].strip() == car_info[1].strip() and car_info[11].strip() == "RENTED"):
                    available_record.append(line)
                    record_found = True
                if dt.datetime.strptime(line[4].strip(),"%d-%m-%Y") > dt.datetime.now() and (line[1].strip() == car_info[1].strip() and car_info[11].strip() == "RENTED"):
                    available_record = []
                    record_found = False

        # If there is a rental transaction record
        if record_found == True:
            print("-------------------------")
            print("** Car can be returned **")
            print("-------------------------")
            printed_item = []
            for item in available_record:
                if item[1] in printed_item:
                    continue
                else:
                    print(f"|{item[1]}|")
                    printed_item.append(item[1])
            print("-------------------------")
            while True:
                car_reg_no = input("Enter car register number for the car returned: ")
                # For loop in range of the length of available_record
                for i in range(len(available_record)):
                    # If the car register format is correct and the car register number is in the available_record
                    if is_valid_car(car_reg_no) and car_reg_no == available_record[i][1].strip():
                        # To store modified lines
                        updated_lines = []
                        # Open car file as file and update the car's availability from "RENTED" to "AVAILABLE"
                        with open("car.txt", "r") as file:
                            for line in file:
                                car_info = line.split("|")
                                if car_info[11].strip() == "RENTED" and car_info[1].strip() == car_reg_no:
                                    car_info[11] = car_info[11].replace(car_info[11], "{:^13s}".format("AVAILABLE"))
                                elif car_info[11].strip() == "RESERVED" and car_info[1].strip() == car_reg_no:
                                    print("Car is not rented.")
                                    return
                                # Join the modified car info back into a line
                                updated_lines.append("|".join(car_info))  
                        # Write the updated lines back to the file
                        with open("car.txt", "w") as car:
                            for updated_line in updated_lines:
                                car.write(updated_line)
                        # Display updated status
                        with open("car.txt","r") as car:
                            car.readline()
                            print("\n"+"*"*60)
                            print(f"**The status of car {car_reg_no} has been updated to 'Available'.**") 
                            print("*"*60)
                            return
                        
                    elif not is_valid_car(car_reg_no):
                        print("\n"+"*"*40)
                        print("**Invalid car register number.**")
                        print("*" *40)
                        return

                    else:
                        print("\n"+"*"*40)
                        print("**Car not found.**")
                        print("*" *40)
                        return
        else:
            print("\n"+"*"*40)
            print("**No car can be return at this time.**")
            print("*" *40)
            return
    

    def view_rental():
        print("\n="+"="*39)
        print("{:^40s}".format("**VIEW RENTAL TRANSACTION**"))
        print("="*40)
        # Get the date for view
        while True:
            date = input("Please enter a date(DD-MM-YYYY): ")
            try:
                date = dt.datetime.strptime(date,"%d-%m-%Y")
                break
            except ValueError:
                print("** Please enter the date in format DD-MM-YYYY **")

        # Default value for found transaction
        found_transaction = False
        rental_record = []
        # Open rental file and print the rental transaction between the date input
        for lines in open("rental.txt","r"):
            line = lines.strip().split("|")
            if dt.datetime.strptime(line[3].strip(),"%d-%m-%Y")<=date<=dt.datetime.strptime(line[4].strip(),"%d-%m-%Y"):
                rental_record.append(lines)
                # Update found transaction to TRUE
                found_transaction = True
        if found_transaction ==  True:
            header = ["Car_reg number","Customer ID","Rental Date","Return Date","Rental Period","Total Price(RM)"]
            print("-------------------------------------------------------------------------------------------------------------------------------")
            print(f"|{header[0]:^20s}|{header[1]:^20s}|{header[2]:^20s}|{header[3]:^20s}|{header[4]:^20s}|{header[5]:^20s}|")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            for line in rental_record:
                print(line,end="")

        # If no rental transaction found
        if not found_transaction:
            print("\n"+"*"*50)
            print("**No rental transaction found between this date.**")
            print("*"*50)

    def delete_transaction():
        print("\n"+"="*40)
        print("{:^40s}".format("**DELETE RENTAL TRANSACTION**"))
        print("="*40)
        # Create list to store available rental transaction record
        available_rental = []
        header = ["Car_reg number","Customer ID","Rental Date","Return Date","Rental Period","Total Price(RM)"]
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{header[0]:^20s}|{header[1]:^20s}|{header[2]:^20s}|{header[3]:^20s}|{header[4]:^20s}|{header[5]:^20s}|")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        # Open rental file and print the rental transaction if the rental date is greater or equal to today's date and add the rental transaction record into available rental
        for lines in open("rental.txt","r"):
            rental_info = lines.split("|")
            if dt.datetime.strptime(rental_info[3].strip(),"%d-%m-%Y") >= dt.datetime.now():
                print(lines,end="")
                available_rental.append(lines.split("|"))
        # If no rental transaction is available
        if len(available_rental) < 1:
            print("**There are no available rental transaction**")
            return
        # Input car register number to delete
        while True:
            car_reg_no = input("Enter car register number to delete: ")
            if is_valid_car(car_reg_no) and car_is_registered(car_reg_no):
                break
            # If car register number format is wrong
            elif not is_valid_car(car_reg_no):
                print("** Invalid car register number.**\n")
            # If car is not registered
            elif not car_is_registered(car_reg_no):
                print("\n"+"*"*40)
                print("{:^40s}".format("**CAR NOT FOUND**"))
                print("*"*40)
                return
        for item in available_rental:
            if item[1].strip() == car_reg_no:
                print("\n"+"="*40)
                print("{:^40s}".format("**CANCELLED RENTAL TRANSACTION**"))
                print("="*40)
                print(f"Car Reg Number: {item[1].strip()}\nCustomer ID: {item[2].strip()}\nRental Date: {item[3].strip()} ~ {item[4].strip()} ({item[5].strip()})Days\nTotal Price: RM{item[6].strip()}")
        # Empty list to store modified lines
        new_lines = []
        # Open rental file to get the lines except the line that user want to delete
        for line in open("rental.txt","r"):
            rental_info = line.split("|")
            if car_reg_no != rental_info[1].strip() or dt.datetime.strptime(rental_info[3].strip(),"%d-%m-%Y") <= dt.datetime.now():
                new_lines.append(line)

        # Write the new lines back to the file
        with open("rental.txt", "w") as file:
            file.writelines(new_lines)
        
        updated_lines = []
        # Open car file as file and update the car's availability from "RENTED" to "AVAILABLE"
        with open("car.txt", "r") as file:
            for line in file:
                car_info = line.split("|")
                if (car_info[11].strip() == "RESERVED" or car_info[11].strip() == "RENTED") and car_info[1].strip() == car_reg_no:
                    car_info[11] = car_info[11].replace(car_info[11], "{:^13s}".format("AVAILABLE"))
                # Join the modified car info back into a line
                updated_lines.append("|".join(car_info))  
        # Write the updated lines back to the file
        with open("car.txt", "w") as car:
            for updated_line in updated_lines:
                car.write(updated_line)
        
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
    
    # Display menu
    choice = menu()

    # Define user's choice and call related function
    if choice == 1:
        check_availability()
        return staff_ID
    elif choice == 2:
        rental_transaction()
        return staff_ID
    elif choice == 3:
        generate_bill()
        return staff_ID
    elif choice == 4:
        return_car()
        return staff_ID
    elif choice == 5:
        view_rental()
        return staff_ID
    elif choice == 6:
        delete_transaction()
        return staff_ID
    elif choice == 7:
        staff_ID = update_profile(staff_ID)
        return staff_ID
    elif choice == 8:
        return False



