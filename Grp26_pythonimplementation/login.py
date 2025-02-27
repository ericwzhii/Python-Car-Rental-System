# Login Function
def login():
    print("-------------------------------------------------------------------------------------------")
    print("***************************** CAR RENTAL SYSTEM GROUP 26 **********************************")
    print("-------------------------------------------------------------------------------------------")
    # Define the attemps time the user are allowed to enter
    count = 3
    # A loops that allow user to make three attemps for login
    while count >= 1:
        # Show the attemps left
        print(f"\n***ATTEMPTS LEFT: {count}***")
        # Accept username and password from the user
        print("="*40)
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        print("="*40)
        # Read username and password from username_password,tlogin_processt file
        for line in open('staff.txt','r'):
            # Split the line read and store in login_info
            login_info = line.split("|")
            # Check if the username and password is correct
            if username == login_info[2].strip() and password == login_info[4].strip():
                staff_ID = login_info[1]
                #Define user roles and return values according to their roles
                if login_info[3].strip().lower() == "manager":
                    return True,'manager',staff_ID
                elif login_info[3].strip().lower() == "carservicestaff":
                    return True, 'css',staff_ID
                elif login_info[3].strip().lower() == "customerservicestaff1":
                    return True, 'cs1',staff_ID
                elif login_info[3].strip().lower() == "customerservicestaff2":
                    return True, 'cs2',staff_ID
        # Decrease the attemps of the user
        count -= 1

    return False

# A function used to check if the user login successfully and what is the role of the user
def check_login(login_process):
    # Message display when the login is not successful
    if login_process == False:
        print("===========================================================================================")
        print("**You have reached the attempts!**\n**Please try again later.**")
        print("===========================================================================================")
        return False
    # Conditions when the login is successful and determine the user's role
    elif login_process[0] ==True:
        print("\n**Login successful!**")
        return login_process[1]
