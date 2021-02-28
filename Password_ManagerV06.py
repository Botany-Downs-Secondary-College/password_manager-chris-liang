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
eligblity = False
logged_in = False


#List for storing account usernames and passwords
account_details=[]
account_details_list = []

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
    main_loop = True
    repeat = 0
    confirm_pass = ""
    password_creator_message = "Please create a password that is 8 characters long, and has numbers : "
    password_check_1 = False
    password_check_2 = False
    create_new = False

    while True:
        name = input("What is your name? : ").strip()
        if name == "":
            print("\nError, nothing entered")
        else:
            break
    while main_loop == True:
        if len(account_details) == 0 or create_new == True:
            x = input("Hello {}, please create a Username : ".format(name))

            while repeat != 2:
                y = input("{}".format(password_creator_message)).strip()
                if len(y) >= 8 and repeat == 0:
                    password_check_1 = True
                    confirm_pass = y
                elif len(y) < 8 and repeat == 0:
                    print("\nPassword has to be 8 characters long")
                elif y == "":
                    print("\nERROR, you did not enter anything")

                if repeat == 0 and password_check_1 == True:
                    for i in range(0, len(y)):
                        if y[i].isnumeric():
                            password_check_2 = True
                            password_creator_message = "Please enter the password again to confirm you know it : "
                            y = ""
                            repeat += 1
                            break
                        else:
                            print("\nPassword MUST have numbers in it!")
                            break

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
                                repeat = 0
                                break
                            elif choice == 3:
                                repeat += 1
                                break
                            else:
                                print("\nPlease enter an option between 1-3")
                        except ValueError:
                            print("\Please enter an option between 1-3")
        return x, y, z
    
def account_details_manager(x, y, z):     
    global pm_account
    global pm_password
    global account_details
    global account_details_list

    if z == 1:
        account_details_list.append([x, y])
            

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
                    account_details_list = account_details_manager(account, password_holder, 1)
                if choice == 2:
                    if len(account_details) == 0:
                        print("Error you have not made any new accounts")
                    else:
                        print("Logging in...")
                if choice == 3:
                    print("Exiting Password Manager program")
                    exit()
                break
            else:
                print("\nPlease enter only numbers between 1-3: ")
        except ValueError:
            print("\nPlease enter in a Number, no letters/words or decimals")
    
