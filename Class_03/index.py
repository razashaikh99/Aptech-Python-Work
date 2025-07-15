# RANDOM PASSWORD GENERATOR

# import random
# import string
# import sys

# import pyperclip

# print("------------ RANDOM PASSWORD GENERATOR ------------\n")

# uppercaseLength = int(input("- How many Upper Letters Do you want? "))
# if uppercaseLength <= 0 or uppercaseLength > 10:
#     print("At least 1 uppercase is required and maximum 10 ")
#     sys.exit()
# lowercaseLength = int(input("- How many Lower Letters Do you want? "))
# if lowercaseLength <= 0 or uppercaseLength > 10:
#     print("At least 1 Lowercase is required and maximum 10 ")
#     sys.exit()
# digitLength = int(input("- How many Numbers Do you want? "))
# if digitLength <= 0 or uppercaseLength > 10:
#     print("At least 1 Digit length  is required and maximum 10 ")
#     sys.exit()
# specialCharacterLength = int(input("- How many Special Characters Do you want? "))
# if specialCharacterLength <= 0 or uppercaseLength > 10:
#     print("At least 1 special character length is required and maximum 10 ")
#     sys.exit()

# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase
# numbers = string.digits
# specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# upperList, lowerList, numberList, specialList = [], [], [], []

# for i in range(uppercaseLength):
#     upperList.append(random.choice(uppercase))

# for i in range(lowercaseLength):
#     lowerList.append(random.choice(lowercase))

# for i in range(digitLength):
#     numberList.append(random.choice(numbers))

# for i in range(specialCharacterLength):
#     specialList.append(random.choice(specialCharacters))

# PasswordList = upperList + lowerList + specialList + numberList
# random.shuffle(PasswordList)

# passwordString = "".join(PasswordList)
# print("\n- Your Generated Password is:", passwordString)


# choice = input("- Do you want to copy this password? (yes/no): ")
# if choice.lower() == "yes":
#     pyperclip.copy(passwordString)
#     print("- Password has been copied to clipboard.")

# ------------------------------------------------------------------------------

# USER SALARY & EXPENSES CALCULATOR

user_salary = int(input("- Enter Your Salary : "))
print('Expenses.....')

userHome = input("- Do You Live In Your Own House...?  (yes/no) : ")

if userHome.lower() == "no" :
    rentExpense = int(input("- Enter Your Rent Expense : "))
else :
    rentExpense = 0

keBill =  int(input("- Enter Your K-E Bill Expence : "))
groceryBill =  int(input("- Enter Your Grocery Expence : "))
gasBill =  int(input("- Enter Your Gas Bill Expence : "))
waterBill =  int(input("- Enter Your Water Bill Expence : "))
internetBill =  int(input("- Enter Your internet Bill Expence : "))
GarbageBill =  int(input("- Enter Your Garbage Bill Expence : "))

totalExpense = keBill + groceryBill + gasBill + waterBill +  internetBill + GarbageBill + rentExpense

print("Your Total Expense is : RS." , totalExpense)
