def manager(ID):
   def menu():
      print("\n"+"="*40)
      print("{:^40s}".format("**MANAGER**"))
      print("="*40)
      print("Action Available".center(40))
      print("-"*40)
      # Display Actions Available
      print("1.Register Staff\n2.Update Staff\n3.Delete Staff\n4.Update Car Rate\n5.View Rental Revenue\n6.Update Own Profile\n7.Log Out")
      # Accept staff choice and return
      while True:
         try:
               choice = int(input("Please enter your selection in number (1, 2, 3...): "))
               if choice <= 7 and choice >= 1:
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

   def register_staff():
      print("\n="+"="*39)
      print("{:^40s}".format("**REGISTER STAFF**"))
      print("="*40)
      import datetime
      ID = input("Enter Staff ID: ")
      while True:
         name = input("Enter Staff Name: ")
         if any(x.isdigit() for x in name):
               print("Name cannot contain digit,enter again.")
               continue

         else:
               break

      while True:
         choice = input("Enter Staff Role (1/2/3/4): \n 1)Manager \n 2)Customer Service Staff 1 \n 3)Customer Service Staff 2 \n 4)Car Service Staff \n Enter your choice: ")
         role = {
            "1": "Manager",
            "2": "CustomerServiceStaff1",
            "3": "CustomerServiceStaff2",
            "4": "CarServiceStaff"
               }

         if role[choice]:
               role = role[choice]
               break
         else:
               print("Please enter a valid selection.")

      password = input("Enter Password: ")
      date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      print("ID:", ID)
      print("Name:", name)
      print("Role:", role)
      print("Password:", password)
      print("Date:", date)

      with open('staff.txt', 'a') as staff:
         table_staff ="|" + ID.center(20) + "|" + name.center(20) + "|" + role.center(24) + "|" + password.center(20) + "|" + str(date).center(20) + "|\n"
         staff.write(table_staff)
         menu = ["Staff ID","Staff Name", "Role","Password","Register Date"]
         print("New staff detail below:")
         print(f"|{menu[0] :^20s}|{menu[1] :^20s}|{menu[2] :^24s}|{menu[3] :^20s}|{menu[4] :^20s}|")
         print("--------------------------------------------------------------------------------------------------------------")
         print(table_staff)   

   def update_staff():
      print("\n"+"="*40)
      print("{:^40s}".format("**UPDATE STAFF**"))
      print("="*40)
      with open("staff.txt", "r") as file:
         lines = file.readlines()
         id = input("Please enter id update:").strip()
         import datetime
         id_found = False
         for i,line in enumerate(lines):
               staff_info = [x.strip() for x in line.split("|") if len(x) > 0]
               date = staff_info[4]
               if staff_info[0] == id:
                  id_found = True
                  role = {
                  1: "Manager",
                  2: "CustomerServiceStaff 1",
                  3: "CustomerServiceStaff 2",
                  4: "CarServiceStaff"
                  }
                  while True:
                     modify_name = input("Please enter the modify name:")
                     if any(x.isdigit() for x in modify_name):
                           print("**Name cannot contain digit, please try again.**")
                           continue
                     else:
                           break

                  while True:
                     print("role:\n1)Manager \n2)Customer Service Staff 1 \n3)Customer Service Staff 2 \n4)Car Service Staff")
                     number = int(input("Please enter the modified role (1, 2, 3, 4): "))
                     if number in [1,2,3,4]:
                           modify_role = role[number]
                           break

                     else:
                           print("**Invalid role, please enter again.**")


                  modify_password = input("Please enter the new password: ")
                  lines[i] = "|{:^20}|{:^20}|{:^24}|{:^20}|{:^20}|\n".format(id, modify_name, modify_role,
                                                                           modify_password, date)
                  with open("staff.txt","w") as file:
                     file.writelines(lines)
                     print(lines[i])

         if not id_found:
               print("record not found")

   def delete_staff():
      print("\n"+"="*40)
      print("{:^40s}".format("**DELETE STAFF**"))
      print("="*40)
      with (open("staff.txt", "r") as file):
         lines = file.readlines()
         id = input("Please enter id staff that resigned:").strip()
         id_found = False
         for i,line in enumerate(lines):
               staff_info = [x.strip() for x in line.split("|") if len(x) > 0]
               if staff_info[0] == id:
                  id_found = True
                  lines[i] = ""
                  with open("staff.txt","w") as file:
                     file.writelines(lines)
                     print("\n============================")
                     print("*STAFF DELETED SUCCESSFULLY*")
                     print("============================")
                  break

      if not id_found:
         print("record not found")

   def update_car_rate():
      print("\n"+"="*40)
      print("{:^40s}".format("**UPDATE RENTING RATE**"))
      print("="*40)
      header = ["Car Reg Num", "Manufacturer", "Car Model", "Year", "Capacity", "L_Svcs Date", "Insurance", "Ins_Exp_Date", "RTax Exp_Date", "Rate/Day", "Status"]
      print("-"*189)
      print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
      print("-"*189)
      with open('car.txt', 'r') as file:
         # Read the file content
         car_details = file.read()
         # Print the file content
         print(car_details)
         car_reg_no = input("Enter the car registration number to modify the car renting rate: ")

         try:
            with open('car.txt', 'r') as file:
               lines = file.readlines()
            for i, line in enumerate(lines):
               details = line.strip().split("|")  # split each line car details
               if car_reg_no == details[1].strip():
                  while True:
                        car_renting_rate = input("Enter the new Car Renting Rate per day: ")
                        if car_renting_rate.isalpha():
                           print("**Invalid input, please enter a valid number.**")
                           continue
                        else:
                           break
                  # replace existing car renting rate to a new one
                  lines[i] = line.replace(details[10], f"RM{car_renting_rate}".center(13))
                  with open('car.txt', 'w') as car:
                        car.writelines(lines)
                        print("-"*189)
                        print(f"|{header[0]:^13s}|{header[1]:^17s}|{header[2]:^13s}|{header[3]:^18s}|{header[4]:^13s}|{header[5]:^18s}|{header[6]:^15s}|{header[7]:^22s}|{header[8]:^22s}|{header[9]:^13s}|{header[10]:^13s}|")
                        print("-"*189)
                        if car_reg_no == details[1].strip():  # Show the changes of the car details
                           print(lines[i], end="")
         except FileNotFoundError:
               print("The file 'car.txt' does not exist.")
               return


   def view_rental_revenue():
         print("\n"+"="*40)
         print("{:^40s}".format("**VIEW RENTAL REVENUE**"))
         print("="*40)
         with (open("rental.txt", "r") as rental):
            lines = rental.readlines()
            while True:
               month = input("\nEnter the month for the revenue (1-12): ").strip()
               if month.isdigit() and (int(month)<1 or int(month)>12):
                   print("\n** Invalid month **")
                   break
               if any(x.isdigit() for x in month):
                  monthly_revenue = 0
                  print("\n"+"="*40)
                  print("{:^40s}".format("**RENTAL REVENUE**"))
                  print("="*40)
                  header = ["Car_reg number", "Customer ID", "Rental Date", "Return Date", "Rental Period",
                              "Total Price(RM)"]
                  print("-------------------------------------------------------------------------------------------------------------------------------")
                  print(f"|{header[0]:^20s}|{header[1]:^20s}|{header[2]:^20s}|{header[3]:^20s}|{header[4]:^20s}|{header[5]:^20s}|")
                  print("-------------------------------------------------------------------------------------------------------------------------------")
                  for i,line in enumerate(lines):
                        rental_info = [x.strip() for x in line.split("|") if len(x) > 0]
                        extract_month = int(rental_info[2].split("-")[1])
                        if int(month) == extract_month:
                           monthly_revenue += int(rental_info[5].strip())
                           print(f"|{rental_info[0]:^20s}|{rental_info[1]:^20s}|{rental_info[2]:^20s}|"
                                 f"{rental_info[3]:^20s}|{rental_info[4]:^20s}|{rental_info[5]:^20s}|")
                  print("-------------------------------------------------------------------------------------------------------------------------------")
                  print("The monthly revenue is: RM", monthly_revenue)
                  break
               else:
                  print("**Please enter a valid month.**")
                  continue 


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
      register_staff()
      return ID
   elif choice == 2:
      update_staff()
      return ID
   elif choice == 3:
      delete_staff()
      return ID
   elif choice == 4:
      update_car_rate()
      return ID
   elif choice == 5:
      view_rental_revenue()
      return ID
   elif choice == 6:
      update_profile(ID)
      return ID
   elif choice == 7:
      return False
   else:
      print("invalid choice,try again~~")


