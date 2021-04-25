import datetime
import random

userData = {}
now = datetime.datetime.now()

#STARTUP MESSAGE
def startup():

    print('Welcome to Bank Knightwalkha')

    prompt = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(prompt == 1):

        login()

    elif(prompt == 2):

        register()

    else:

        print("You have selected invalid option")
        startup()



#LOGIN AREA
def login():

    print("********* LOGIN ***********")

    prompt = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in userData.items():
        if(accountNumber == prompt):
            if(userDetails[4] == password):
                bankOperation(userDetails)


    print('Invalid account or password')
    login()


#REGISTRATION AREA
def register():

    print("****** REGISTER *******")

    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    phoneNumber = int(input('What is your phone number? \n'))
    email = input("What is your email address? \n")
    password = input("create a password for yourself \n")

    accountNumber = accountNumberGeneration()

    userData[accountNumber] = [ firstName, lastName, phoneNumber, email, password, balance]

    print("Your Account Has been created")
    print(" ************************* ")
    print("Your account number is: %d \n" % accountNumber)
    print("Make sure you keep it safe")
    print(" ************************* \n")

    login()


def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) + 'and you logged-in at: \n' + now.strftime('%Y-%m-%d %H:%M:%S') )

    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout \n"))

    if(selectedOption == 1):

        depositOperation()

    elif(selectedOption == 2):

        withdrawalOperation()
    
    elif(selectedOption == 3):

        exit()

    else:

        print("Invalid option selected")
        bankOperation(user)


#BALANCE AREA
def balance():

    initialBalance = 0    

def getBalance(userDetails, balance):

    userDetails[5] = balance

    return balance


#WITHDRAWAL AREA
def withdrawalOperation():
    
    print("****** WITHDRAWAL ******* \n")
    withdrawal = int(input('How much do you want to withdraw? \n $'))

    if(withdrawal >= balance):

        print('You do not have sufficient amount in your account.')

    else:

        newBalance = withdrawal - balance

        print('Your new balance is $' % newBalance)


#DEPOSIT AREA
def depositOperation():

    print("****** DEPOSIT ******* \n")
    deposit = int(input('How much do you want to deposit? \n $'))

    balance = deposit + getBalance()

    print('Your new balance is \n $' % balance)


#GENERATION OF ACCOUNT NUMBER
def accountNumberGeneration():

    return random.randrange(1111111111,9999999999)


#LOG-OUT AREA
def logout():
    exit()


startup()

