def cus_service_staff1(staff_ID):
    # Customer Service Staff 1 Menu
    def menu():
        print("\n="+"="*39)
        print("{:^40s}".format("**CUSTOMER SERVICE STAFF 1**"))
        print("="*40)
        print("Action Available".center(40))
        print("-"*40)
        print("1. Register customer\n2. Update customer details\n3. View registered customers\n4. Update profile\n5. Delete customers without transactions\n6. Log Out")
        print("-"*40)
        while True:
            try:
                choice = int(input("\nPlease enter your selection in number (1, 2, 3,...): "))
                if choice <= 6:
                    return choice
                elif choice == 7:
                    return False
                else:
                    print("\n==================")
                    print("*ACTION NOT EXIST*")
                    print("==================")
            except ValueError:
                print("\n===============")
                print("*INVALID INPUT*")
                print("===============")
                print("Please enter a valid number\n")
    
    # Function to update profile
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
                            print("Action does not exist. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
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
    
   # Function to update customer details
    def update_customer_details():
            print("\n"+"="*40)
            print("{:^40s}".format("**CAR REGISTER**"))
            print("="*40)
            while True:
                # prompt the user enter customer ID
                customer_id = input("Enter customer ID: ")
                # open customer.txt and read
                with open("customer.txt", "r") as file:
                    # read all the lines from file
                    lines = file.readlines()
                    # If found false then break
                    found = False
                    #Iterate each line of the file
                    for i, line in enumerate(lines):
                        #split the line into a list of customer
                        customer_info = line.strip().split("|")
                    
                        #check the insert customer id is it match to the file you find then print out
                        if customer_info[1].strip()== customer_id.strip():
                            found = True #if true
                            customer_id = customer_info[1].strip()
                            name = customer_info[2].strip()
                            nric = customer_info[3].strip() if customer_info[3].strip() != 'None' else 'N/A'
                            passport = customer_info[4].strip() if customer_info[4].strip() != 'None' else 'N/A'
                            driving_license = customer_info[5].strip()
                            address = customer_info[6].strip()
                            phone = customer_info[7].strip()
                            registration_date = customer_info[8].strip()
                            print("\n" + "="*170)
                            print("Current Customer Details:".center(170))
                            print("="*170)
                            print("{:^13} {:^13} {:^18} {:^18} {:^18} {:^40} {:^20} {:^15}\n".format(
                                "Customer ID", "Name", "NRIC", "Passport No", "License No", "Address", "Phone", "Reg. Date"
                            ))
                            print("-"*170)
                            print("{:^13} {:^13} {:^18} {:^18} {:^18} {:^40} {:^20} {:^15}".format(
                                customer_id,name,nric,passport,driving_license,address,phone,registration_date
                            ))
                            print("-"*170 + "\n")

                            new_passport_no = passport
                            new_license_no = driving_license
                            new_address = address
                            new_phone = phone

                            #choose which to update then proceed
                            while True:
                                # if foreigner have passport selection
                                if nric == "N/A":
                                    choice = input("**UPDATE CUSTOMER DETAILS**\n1. Phone\n2. Address\n3. License No\n4. Passport No\nEnter your choice (1-4): ")
                                else:
                                    # if local don't have passport selection
                                    choice = input("**UPDATE CUSTOMER DETAILS**\n1. Phone\n2. Address\n3. License No\nEnter your choice (1-3): ")

                                if choice == "1":
                                    while True:
                                        new_phone = input("Enter new phone number: ")
                                        customer_info[7] = new_phone
                                        # check format
                                        if len(new_phone.split('-')) == 2 and new_phone[0] == '0' and new_phone.split('-')[0][1:].isdigit() and len(new_phone.split('-')[0]) <= 4 and new_phone.split('-')[1].isdigit() and len(new_phone.split('-')[1]) in [7,8]:
                                            break
                                        else:
                                            print("**Invalid phone number format. Please try again.**\n")                                            

                                elif choice == "2":
                                    while True:
                                        new_address = input("Enter new address: ")
                                        customer_info[6] = new_address
                                        # check format
                                        if all(char.isalnum() or char in [' ', ',', '/', '#', '-'] for char in new_address):
                                            break
                                        else:
                                            print("**Invalid address format. Please try again.**\n")                                           

                                elif choice == "3":
                                    while True:
                                        new_license_no = input("Enter new license number: ")
                                        customer_info[5] = new_license_no 
                                        # check format
                                        if len(new_license_no) == 9 and new_license_no[0].upper() == 'D' and new_license_no[1:].isdigit():
                                            break
                                        else:
                                            print("**Invalid driving lincense format. Please try again.**\n")                                                                                      
                                            
                                elif choice == "4" and nric == "N/A":
                                    while True:
                                        new_passport_no = input("Enter new passport number: ")
                                        customer_info[4] = new_passport_no + "\n" 
                                        # check format
                                        if len(new_passport_no) == 13 and new_passport_no[0:2].isalpha() and new_passport_no[2:11].isdigit() and new_passport_no[-1].isalpha:     
                                            break                  
                                        else:
                                            print("**Invalid passport format. Please try again.**\n")                                           
                                                                                                                                    
                                else:
                                    print("Please try again\n")
                                    continue
                                                
                                if new_passport_no == "N/A":
                                    new_passport_no = None

                                # format the updated lines same as customer.txt format
                                updated_line = "|{:^13}|{:^20}|{:^20}|{:^20}|{:^20}|{:^50}|{:^20}|{:^20}|\n".format(
                                    customer_info[1], customer_info[2], customer_info[3], str(new_passport_no), str(new_license_no), new_address, new_phone, customer_info[8]
                                )
                                lines[i] = updated_line
                                break
                                
                                                    # replace the old info to updated info and open the file write the updated lines to the back                    
                            with open("customer.txt", "w") as file:
                                for line in lines:
                                    file.write(line)
                                print("\n=====================")
                                print("*UPDATED SUCCESSFULLY*")
                                print("======================")
                                print("**Customer details updated successfully!**\n")  
                            return
  
                # if custsmer not found end the loop and print message   
                    if not found:
                        print("**Customer not found.**\n")
                 


    # Function to delete customers who have no transaction
    def delete_customers():
        print("\n="+"="*39)
        print("{:^40s}".format("**DELETE CUSTOMER**"))
        print("="*40)
        # a set to store ID which have transaction
        customers_with_transactions = set()

        #Open rental file and read
        with open("rental.txt", "r") as rental_file:
            for line in rental_file:
                # Extract the customer ID
                customer_id = line.split("|")[2].strip()
                #Add customer ID to the set 
                customers_with_transactions.add(customer_id)


        # A list to store the lines of customers who have transaction
        updated_customer_lines = []

        customers_without_transactions = []

        # Open customer file and read
        with open("customer.txt", "r") as customer_file:
            for line in customer_file:
                customer_info = line.strip().split("|")
                customer_id = customer_info[1].strip()

                # If in the set, add line to the list
                if customer_id in customers_with_transactions:
                    updated_customer_lines.append(line)
                else:
                    # if not in the set, add to customer_without_transactiions list
                    customers_without_transactions.append(customer_info)

        # Print customers_without_transactions
        if customers_without_transactions:
            print("\nCustomers without transactions".center(40))
            print("-" * 40)
            for customer_info in customers_without_transactions:
                customer_id = customer_info[1]
                name = customer_info[2]
                print(f"{customer_id} | {name}")
            print("-" * 40)

        # Ask for confirmation
        confirmation = input("Do you want to delete these customers without transactions? (Y/N)\n")
        if confirmation.upper() == 'Y':
        # Open customer file and write updated info
            with open("customer.txt", "w") as customer_file:
                customer_file.writelines(updated_customer_lines)
            print("\n=====================")
            print("*DELETED SUCCESSFULLY*")
            print("======================")
            print("**Customers without transactions have been deleted.**")
        else:
            # if no print message
            print("\n=====================")
            print("*OPERATION CANCELLED*")
            print("=====================")            
            print("No customers were deleted")
     
    from datetime import date

    # Function to generate new customer id
    def generate_customer_ids(start_id=1):
        # try to read last exist customer id in customer.txt
        try:
            with open("customer.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    # Get last customer id from last line
                    last_customer_id = lines[-1].strip().split("|")[1]
                    # Remove C prefix then convert it to the integer
                    last_id = int(last_customer_id.replace("C", ""))
                    # new customer id should be last id + 1
                    start_id = last_id + 1
        except:
            pass
        
        #Format to C + six digits, padded with zeros
        customer_id = f"C{start_id:06d}"
        return customer_id

    # Function to register a new customer
    def register_customer():    
        print("\n="+"="*39)
        print("{:^40s}".format("**CUSTOMER REGISTER**"))
        print("="*40)    
        with open('customer.txt', 'a') as file:
            # loop to check name only alphabets and space
            while True:
                    name = input("Enter customer name (alphabets and spaces only): ")
                    if name.replace(" ", "").isalpha():
                        break
                    else:
                        print("**Invalid name format. Please try again.**")

            # loop to check nric format and passport format
            # if nric = N/A, then input passport with valid format(first two alphabets, 10 digits, 1 alphabet)
            # if nric with valid format(6 digits, dash, 2 digits, dash, 4 digits last)
            while True:
                        nric = input("Enter NRIC (or 'N/A' for foreigner): ")
                        if nric == 'N/A':
                            while True:
                                passport = input("Enter passport number: ")
                                if len(passport) == 13 and passport[0:2].isalpha() and passport[2:11].isdigit() and passport[-1].isalpha:                           
                                    break
                                else:
                                    print("**Invalid passport format. Please try again.**")
                            break
                        elif len(nric) == 14 and nric[0:6].isdigit() and nric[6] == '-' and nric[7:9].isdigit() and nric[9] == '-' and nric[10:].isdigit():
                            passport = "N/A"
                            break
                        else:
                            print("**Invalid passport format. Please try again.**")

            # loop to check driving license  format with First Alphabet "D" + rest of the 8 digits
            while True:
                    driving_license = input("Enter driving license number: ")
                    if len(driving_license) == 9 and driving_license[0].upper() == 'D' and driving_license[1:].isdigit():
                        break
                    else:
                        print("**Invalid driving license format. Please try again.**")

            # loop to check address format of alphanumeric or one of the characters which is space, comma, slash, hash, dash
            while True:
                    address = input("Enter customer address: ")
                    if all(char.isalnum() or char in [' ', ',', '/', '#', '-'] for char in address):
                        break
                    else:
                        print("**Invalid address format. Please try again.**")

            # loop to check phone number format starts with 0, followed by 1 to 3 digits, dash, last 7 to 8 digits
            while True:
                    phone = input("Enter customer contact number: ")
                    if len(phone.split('-')) == 2 and phone[0] == '0' and phone.split('-')[0][1:].isdigit() and len(phone.split('-')[0]) <= 4 and phone.split('-')[1].isdigit() and len(phone.split('-')[1]) in [7,8]:
                        break
                    else:
                        print("**Invalid phone number format. Please try again.**")

            if nric == "N/A":
                    nric = None
            if passport == "N/A":
                    passport = None
            
            registration_date = date.today().strftime("%Y-%m-%d")
            # call back generate_customer_ids function to find new_customer_id
            new_customer_id = generate_customer_ids()

            # save the data to customer file 
            with open('customer.txt', 'a') as file:
                file.write("|{:^13}|{:^20}|{:^20}|{:^20}|{:^20}|{:^50}|{:^20}|{:^20}|\n".format(
                    str(new_customer_id),
                    str(name),
                    str(nric),
                    str(passport),
                    str(driving_license),
                    str(address),  
                    str(phone),
                    registration_date
                ))

        print("\n="+"="*39)
        print("{:^40s}".format("**REGISTER SUCCESSFUL**"))
        print("="*40)    
    # Function to view all registered customers
    def view_registered_customers():
        print("="*180)
        print("List Of Registered Customers:".center(180))
        print("="*180)
        print("-" * 180)
        # print the header in the terminal
        print("{:^13} {:^13} {:^18} {:^18} {:^18} {:^45} {:^30} {:^20}".format(
            "Customer ID", "Name", "NRIC", "Passport No", "License No", "Address", "Phone", "Reg. Date"
        ))
        print("-" * 180)

        # open customer file and read all the lines
        with open("customer.txt", "r") as file:
            customers = file.readlines()

        # Iterate each line, split and extract customer info
        for customer in customers:
            customer_info = customer.split("|")
            customer_id = customer_info[1].strip()
            name = customer_info[2].strip()
            nric = customer_info[3].strip() if customer_info[3].strip() != 'None' else 'N/A'
            passport = customer_info[4].strip() if customer_info[4].strip() != 'None' else 'N/A'
            driving_license = customer_info[5].strip()
            address = customer_info[6].strip()
            phone = customer_info[7].strip()
            registration_date = customer_info[8].strip()

            # print all the customer info
            print("{:^13} {:^13} {:^18} {:^18} {:^18} {:^45} {:^30} {:^20}".format(
                customer_id,name,nric,passport,driving_license,address,phone,registration_date
            ))
        print("-" * 180 + "\n")

    # call back the menu and find the function
    while True:
        choice = menu()
        if choice == 1:
            register_customer()
        elif choice == 2:
            update_customer_details()
        elif choice == 3:
            view_registered_customers()
        elif choice == 4:
            update_profile(staff_ID)
            return staff_ID
        elif choice == 5:
            delete_customers()
        elif choice == 6:
            print("Exiting...")
            return False
        else:
            print("Invalid choice. Please try again.")



