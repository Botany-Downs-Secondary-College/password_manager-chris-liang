#Password_Manager
#create and display passwords for users
#C.Liang, Feb 22
#Inital values
name= ""
age= ""
account = ""
password_holder= ""
eligblity = False
#List for storing account usernames and passwords
account_details=[]
account_password_list = []
#Sub routine
def criteria_checker(x):
    global eligblity
    while True:
        try:
            age = int(input("What is your age? : ").strip())
            if age >= 13:
                eligblity = True
                return eligblity
                break
            else:
                print("You are not eliglble to use this program, Users must be ages at; 13 or above")
                eligblity = False
                return eligblity
                break
        except ValueError:
            print("\nPlease enter a whole number")        
        

#main routine
while True:
    eligblity = criteria_checker(age)
    print("Sussessful")
    if eligblity == False:
        break
