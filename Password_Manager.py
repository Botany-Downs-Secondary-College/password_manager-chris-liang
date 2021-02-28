#Password_Manager
#create and display passwords for users
#C.Liang, Feb 22

#Inital values
name= ""
age= ""
account = ""
pm_account = ""
pm_password = ""
password_holder= ""
num = 0
eligblity = False
logged_in = False


#List for storing account usernames and passwords
account_details=[]
account_details_list = [["Chris", "101Chris101", ["Youtube account", ["ChrisYT", "101Chris101"]]]]

#Sub routine
def criteria_checker(x):
    global eligblity

    while True:
        try:
            age = int(input("What is your age? : ").strip())
            if age >= 13:
                eligblity = True
                return eligblity
                break
            else:
                print("You are not eliglble to use this program, Users must be ages at; 13 or above")
                eligblity = False
                return eligblity
                break
        except ValueError:
            print("\nPlease enter a whole number")


def account_creator(x, y, z):
    repeat = 0
    confirm_pass = ""
    password_creator_message = "Please create a password that is 8 characters long, and has numbers : "
    num_count = 0
    password_check_1 = False
    password_check_2 = False
    create_new = False
    global account_details_list

    while True:
        name = input("What is your name? : ").strip()
        if name == "":
            print("\nError, nothing entered")
        else:
            break
    while True:
        x = input("Hello {}, please create a Username : ".format(name))
        if x != "":
            while repeat != 2:
                y = input("{}".format(password_creator_message)).strip()
                if len(y) >= 8 and repeat == 0:
                    password_check_1 = True
                    confirm_pass = y
                    password_creator_message = "Please enter the password again to confirm you know it : "
                    repeat += 1
                    y = ""
                elif len(y) < 8 and repeat == 0:
                    print("\nPassword has to be 8 characters long")
                elif y == "":
                    print("\nERROR, you did not enter anything")

                if repeat == 1 and y == confirm_pass:
                    z = True
                    break
                elif repeat == 1 and y != "":
                    print("\nERROR, password entered did not match")
                    while True:
                        try:
                            choice = int(input("1. Try again\n2. Make new password\n3. Exit\n").strip())

                            if choice == 1:
                                repeat = 1
                                break

                            elif choice == 2:
                                password_creator_message = "Please create a password that is 8 characters long, has numbers : "
                                num_count = 0
                                repeat = 0
                                break
                            elif choice == 3:
                                repeat += 1
                                break
                            else:
                                print("\nPlease enter an option between 1-3")
                        except ValueError:
                            print("\nPlease enter an option between 1-3")
            break
        else:
            print("ERROR, you have entered nothing")
    return x, y, z
    
def account_details_manager(x, y, z):     
    global pm_account
    global pm_password
    global account_details
    global account_details_list
    global account_details_manager

    if z == 1:
        account_details_list.append([x, y])
        return account_details_list
    if z == 2:
        while True:
            detail = input("What are these account details for? : ")
            if detail != "":
                for i in range(0, len(account_details_list)):
                    if account_details_list[i].count(pm_account) > 0:
                            account_details_list[i].append([detail, [x,y]])
                            print(account_details_list)
                            break
                break
            else:
                print("ERROR, you haven't entered anything")
        return account_details_list
    if z == 3:
        account_details_manager(account, password_holder, 4)
        while True:
            detail = int(input("Please enter in a number: "))
        for i in range(0, len(account_details_list)):
            if account_details_list[i].count(pm_account) > 0:
                account_details_list.pop(account_details_list[i][detail + 1])
            break
        break
    if z == 4:
        if len(account_details_list) > 0:
            for i in range(0, len(account_details_list)):
                if account_details_list[i].count(pm_account) > 0:
                    for l in range(2, len(account_details_list[i])):
                        print("{}. Purpose: {} Username: {} Password: {}".format(l - 1, account_details_list[i][l][0], account_details_list[i][l][1][0], account_details_list[i][l][1][1]))
                    break
        else:
            print("ERROR, There are no passwords stored on this account yet!") 
            

def login(z):
    global pm_account
    global pm_password
    global account_details_list
    repeat = 0
    username_check = False
    password_check = False
    while True:
        name = input("What is your name? : ")
        if name == "":
            print("ERROR, you did not enter in a name")
        else:
            break
    while repeat != 2:
        if repeat == 1:
            detail = input("Hello {}, please enter in the password: ".format(name))
        else:
            detail = input("Hello {}, please enter in your Username: ".format(name))
        for i in range(0, len(account_details_list)):
            if account_details_list[i].count(detail) > 0:
                if account_details_list[i]:
                    if repeat == 0:
                        pm_account = detail
                        username_check = True
                    else:
                        pm_password = detail
                        password_check = True
                    print("Match found!")
                    repeat += 1
                    break
            while True:
                if repeat == 0:
                    print("\nERROR, could not find Username, please check for Capitals and Spacebars")
                elif repeat == 1:
                    print("\nERROR, password was incorrect for {}, check for Capitals and Spacebars".format(pm_account))
                try:
                    if repeat == 0:
                        choice = int(input("Would you like to: \n1. Use another Username\n2. Exit\n"))
                        if choice == 1:
                            choice = 0
                        if choice == 2:
                            continue
                    if repeat == 1:
                        choice = int(input("Would you like to: \n1. Try again\n2. Use another Username\n3. Exit\n"))
                        if choice == 1:
                            repeat = 1
                        if choice == 2:
                            repeat = 0
                        if choice == 3:
                            continue
                    break
                except ValueError:
                    if repeat == 0:
                        print("\nPlease enter a option from 1-2, do NOT enter words or decimals")
                    else:
                        print("\nPlease enter a option from 1 to 3, do NOT enter words or decimals")
            break
    if username_check == True and password_check == True:
        z = True
        return z

        
#main routine
while True:
    eligblity = criteria_checker(age)
    if eligblity == False:
        break
    while True:
        try:
            choice = int(input("Would you like to: \n1. Sign up\n2. Login in\n3. Exit\n").strip())
            if choice <= 3 and choice > 0 and choice != 0:
                if choice == 1:
                    account, password_holder, logged_in = account_creator(account, password_holder, logged_in)
                    pm_account = account
                    pm_password = password_holder
                    account_details_list = account_details_manager(account, password_holder, 1)
                    print(account_details_list)
                if choice == 2:
                    if len(account_details_list) == 0:
                        print("Error you have not made any new accounts")
                    else:
                        logged_in = login(logged_in)
                if choice == 3:
                    print("Exiting Password Manager program")
                    exit()
                break
            else:
                print("\nPlease enter only numbers between 1-3: ")
        except ValueError:
            print("\nPlease enter in a Number, no letters/words or decimals")
    if logged_in == True:
        while True:
            try:
                choice = int(input("Logged in as : {}\nWould you like to: \n1. Add Username and Password details\n2. Remove Username and Password details\n3. View Usernames and Passwords\n4. Exit\n".format(pm_account)))
                if choice == 1:
                    account, password_holder, account_details = account_creator(account, password_holder, 1)
                    account_details_list = account_details_manager(account, password_holder, 2)
                elif choice == 2:
                    account_details_list = account_details_manager(account, password_holder, 3)
                elif choice == 3:
                    account_details_manager(account, password_holder, 4)
                elif choice == 4:
                    print("Logging out, leaving, thank you for using Password Manager")
                    exit()
                else:
                    print("\nERROR, please only enter a value from 1-4")
            except ValueError:
                print("ERROR, please only enter a value from 1-4, no words or decimals")