#Password_Manager
#create and display passwords for users
#C.Liang, Feb 22

#Inital values
name= ""
age= ""
account = ""
password_holder= ""
eligblity = False

#List for storing account usernames and passwords
account_details=[]
account_password_list = []

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


def account_creator(x, y):
    global account_details
    x = 0
    y = 0
    main_loop = True
    repeat = 0
    confirm_pass = ""
    password_creator_message = "Please create a password that is 8 characters long, has numbers : "
    password_check_1 = False
    password_check_2 = False
    create_new = False


    name = input("What is your name? : ").strip()
    while main_loop == True:
        if len(account_details) == 0 or create_new == True:
            x = input("Hello {}, please create a Username : ".format(name))

            while repeat != 2:
                
                y = input("{}".format(password_creator_message))
                if len(y) >= 8:
                    password_check_1 = True
                else:
                    print("\nPlease enter a password that is 8 characters long")

                for i in range(0, len(y)):
                    if y[i].isnumeric() and password_check_1 == True:
                        password_check_1 = True
                        repeat += 1
                        break

                if repeat == 1: 
                    confirm_pass = y
                    password_creator_message = "Please enter the password again to confirm you know it : "
                else:
                    password_creator_message = "Please create a password that is 8 characters long, has numbers : "


                if repeat == 1 and y == confirm_pass:
                    break
                elif repeat == 1 and y != "":
                    while True:
                        print("\nERROR, password entered did not match")
                        choice = input("1. Try again\n2. Make new password\n3. Exit\n")
                        if choice == "1":
                            repeat = 1
                            break
                        elif choice == "2":
                            password_creator_message = "Please create a password that is 8 characters long, has numbers : "
                            repeat = 0
                            break
                        elif choice == "3":
                            repeat += 1
                            break
                        else:
                            print("\nPlease enter an option between 1-3")
                
        else:
            while True:
                choice = input("Would you like to create a new Account? (Y/N): ").strip().lower()
                if choice == "y":
                    continue
                elif choice == "n":
                    loop = False
                    break
                else:
                    print("\nPlease enter Y or N")
        return x, y
    
        
        


#main routine
while True:
    eligblity = criteria_checker(age)
    if eligblity == False:
        break
    account, password_holder = account_creator(account, password_holder)
