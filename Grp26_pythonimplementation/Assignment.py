# Here is the main program
import login
import cs1
import cs2
import css
import manager

while True:    
    # Assign login() to identity
    identity = login.login()
    # Check user role using chek_login() function
    role = login.check_login(identity)
    # Break if login fail
    if role == False:
        break
    # Extract staff_ID from identity
    staff_ID = identity[2].strip()

    # While login is successful, Call specific function according to user's role
    while identity[0] == True:
        if role == 'cs2':
            staff_ID = cs2.cus_service_staff2(staff_ID)
            # If user select logout, break the loop and return to login page
            if staff_ID == False:
                break
        elif role == "css":
            staff_ID = css.car_service_staff(staff_ID)
            if staff_ID == False:
                break
        elif role == "manager":
            staff_ID = manager.manager(staff_ID)
            if staff_ID == False:
                break
        elif role == "cs1":
            staff_ID = cs1.cus_service_staff1(staff_ID)
            if staff_ID == False:
                break
