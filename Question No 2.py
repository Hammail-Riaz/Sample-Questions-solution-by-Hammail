# Qno2: Write a Python program that simulates a login system. The program should ask for username and password and allow only three attempts. Display appropriate messages for success and failure

# sol no 2

# Defining correct cradentials
db_username = "userabc"    
db_password = "password123"

print("Welcome Back! Enter your Cradentials to login...")
print("Notes: You have only 3 attempts to login..")

# initialization
limit = 3
attempts = 0

while attempts < limit:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    attempts += 1
    
    if username == db_username and password == db_password:
        print('Correct Cradentials...')
        break
    
    elif username != db_username or password != db_password:
        print("Wrong Cradentials... Invalid username or Password")
        print(f"Attempts Left: {limit - attempts}")
