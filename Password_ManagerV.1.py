#Password_Manager
#create and display passwords for users
#C.Liang, Feb 22

#Inital values
name=""
age=""
password_holder= ""
eligblity = False

#List for storing account usernames and passwords

acount_details=[]

#Sub routine
def criteria_checker(x):
    while True:
        try:
            age = int(input("What is your age? : "))
            if age >= 13:
                eligblity = True
                return eligblity
                break
            else:
                print("You are not eliglble to use this program, Users must be ages at; 13 or above")
                break
        except ValueError:
            print("\nPlease enter a whole number")
        
        


#main routine
while True:
    eligblity = criteria_checker(age)
    print("Sussessful")
