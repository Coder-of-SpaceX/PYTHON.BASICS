# # # Only IF Condition practise
# # # Check if a number is positive. 

# # a = 10
# # if a > 0:
# #     print("Its a Positive Number")



# # # Check if a user is eligible to vote.
# # User_Age = 18
# # if User_Age >= 18:
# #     print("User is Eligible to Vote")


# # # Check if a string contains the letter 'a'
# # Sentence_Draft = "RadhaKrishna"
# # if "a" in Sentence_Draft:
# #     print("Yes this character is available in the string")


# # # Check if a number is divisible by 5.
# # divisible_by = 15
# # if divisible_by % 5 == 0:
# #     print("Yes this number is divisible by 5")


# # # Check if a password length is valid
# # Username = input("Enter Your Username Here---  ")
# # Password = input("[Minimum 10 characters allowed] Enter your password here ---  ")
# # print(Username)
# # if len(Password) <= 10:
# #     print("Password Length is Valid, Logged in Successfully, Congratulations !!")


# # # only If......Elif... condition practise
# # # Grade classification based on marks. _Take a student's marks (0–100) and print the grade:

# # # If marks ≥ 90 → "Grade A"

# # # If marks ≥ 75 → "Grade B"

# # # If marks ≥ 60 → "Grade C"

# # # If marks ≥ 40 → "Grade D"_

# # marks = int(input("Enter your Marks---  "))
# # print(marks)
# # if marks >= 90:
# #     print("Grade A")
# # elif marks >= 75:
# #     print("Grade B")
# # elif marks >= 60:
# #     print("Grade C")
# # elif marks >= 40:
# #     print("Grade D")

# # # Check day type based on input. _Ask the user to enter a day name (e.g., "Monday").
# # # If it's "Saturday" or "Sunday" → "Weekend"
# # # If it's any other weekday → "Weekday"_

# # day_name = input("Enter the Day Name over Here---  ").lower()
# # print(day_name)
# # if day_name == "saturday" or day_name == "sunday":
# #     print("Congratulations! its \"weekend\" ")
# # elif day_name in ["monday","tuesday","wednesday","thursday","friday"]:
# #     print("Aww!! you have a job to do, its \"Weekday\" ")

# # # Temperature alert system. _Take temperature input in Celsius.

# # # If temp ≥ 40 → "Extreme Heat"

# # # If temp ≥ 30 → "Hot"

# # # If temp ≥ 20 → "Warm"

# # # If temp ≥ 10 → "Cool"_

# # weather_temprature = int(input('[limit from number 10 - 40] Enter the Temprature of umbergaon gujarat---  '))
# # print(weather_temprature,"Degree C")
# # if weather_temprature >= 40:
# #     print("Extreme Heat")
# # elif weather_temprature >= 30:
# #     print("Hot")
# # elif weather_temprature >= 20:
# #     print("Warm")
# # elif weather_temprature >= 10:
# #     print("Cool")

# # # Check number type. _Take an integer input.

# # # If number > 0 → "Positive"

# # # If number < 0 → "Negative"

# # # If number == 0 → "Zero"_

# # numb_type = int(input("Enter the number here and check whether the number is +, - or equals to 0---  "))
# # print(numb_type)
# # if numb_type > 0:
# #     print(f"{numb_type} is an positive number")
# # elif numb_type < 0:
# #     print(f"{numb_type} is an negative number")
# # elif numb_type == 0:
# #     print("number is equal to 0")

# # # Simple menu selection. _Ask the user to enter a number (1–3):

# # # If 1 → "You selected Coffee"

# # # If 2 → "You selected Tea"

# # # If 3 → "You selected Juice"_

# # simple_numb = int(input("Enter the simple number from [1-3] allowed ---  "))
# # print(simple_numb)
# # if simple_numb == 1:
# #     print("You selected Coffee")
# # elif simple_numb == 2:
# #     print("You selected tea")
# # elif simple_numb == 3:
# #     print("You selected Juice")

# # # Practise only if....else
# # # Even or Odd Checker _Ask the user to enter a number.
# # # If it’s divisible by 2 → print "Even number"
# # # Else → print "Odd number"_

# # check_even_odd = int(input("Enter and Check the number is even or odd ---  "))
# # print(check_even_odd)
# # if check_even_odd % 2 == 0:
# #     print("The Number you entered is 'EVEN' ")
# # else:
# #     print("The Number you entered is 'Odd' " )

# # # Password Match Validator _Ask the user to enter a password and confirm it.
# # # If both match → print "Password confirmed"
# # # Else → print "Passwords do not match"_

# # U_Name = input("Enter Your User Name ---   ")
# # password1 = input("Enter Your Password")
# # confrm_password = input("Enter Your Password Again")
# # if password1 == confrm_password:
# #     print("Password Confirmed")
# # else:
# #     print("Re-enter your password as passwords do not match")

# # # Age-Based Ticket Pricing _Ask the user for their age.
# # # If age is less than 12 → print "Child ticket: 50"
# # # Else → print "Regular ticket: ₹100"_

# # child_adult_age = int(input("Enter you age here ---   "))
# # print(child_adult_age)
# # if child_adult_age <= 12:
# #     print("Child Ticket : ₹ 50 /- ")
# # else:
# #     print("Regular Ticket : ₹ 100 /- ")


# # # Check if a number is zero or not _Ask the user to enter a number.
# # # If it’s zero → print "Number is zero"
# # # Else → print "Number is not zero"_

# # check_numb = int(input("Enter and check whether the number is 0 or not ---  "))
# # print(check_numb)
# # if check_numb == 0:
# #     print(f"{check_numb} is zero")
# # else:
# #     print(f"{check_numb} is not zero")

# # # Check if a string is empty _Ask the user to enter a string.
# # # If the string is empty → print "No input provided"
# # # Else → print "You entered: [user input]"_

# # user_input = input("Enter a String ---  ")
# # if len(user_input) == 0:
# #     print("no input provided")
# # else:
# #     print(f"You entered: {user_input}")

# # # Shorthand if practise 
# # # Check if a number is positive or negative Take a number input. Print "Positive" if it's greater than 0, otherwise "Negative" — all in one line.
# # no_enter = int(input("Enter the Number ---  "))
# # print("The number is positive") if no_enter > 0 else print("The Number is negative")

# # # Even or Odd in one line Take a number input. Print "Even" if divisible by 2, else "Odd" — using short-hand if.
# # ev_od = int(input("Enter the Number ---  "))
# # print("The Number is Even") if ev_od % 2 == 0 else print("The Number is Odd")

# # # Voting eligibility check Take age input. Print "Eligible to vote" if age ≥ 18, else "Not eligible" — in one line.
# # voter_age = int(input("Enter The age of the voter ---  "))
# # print("Eligible for voting") if voter_age >= 18 else print("Not Eligible for voting")

# # # Password match check Take two password inputs. Print "Match" if they are equal, else "Mismatch" — using short-hand if.
# # password_1 = input("Enter Your Password ---  ")
# # confirm_pass = input("Enter confirm password again ---  ")
# # print("Match") if password_1 == confirm_pass else print("Mismatch")

# # # String length check Take a string input. Print "Valid" if length ≥ 5, else "Too short" — in one line.
# # string_len = input("Enter the length of the string ---   ")
# # print("Valid") if len(string_len) >= 5 else print("Too Short")

# # Practise logical operatos in if condition
# # Login Validation
# # Ask the user for a username and password.
# # Check if the username is "admin" and the password is "1234".
# # If both match, print "Access granted", else "Access denied".

# USERNAME = input("Enter Your Username Here - - -  ").strip()
# PASSWORD = input("Enter Your Password Here - - -  ").strip()
# if USERNAME == "admin" and PASSWORD == "1234":
#     print("Access Granted")
# else:
#     print("Access Denied")

# # Discount Eligibility
# # Ask the user for their age and membership status (yes or no).
# # If the user is under 18 or over 60, or they are a member, they get a discount.
# # Print whether they are eligible or not.
# user_age = int(input("Enter Your Age ---  "))
# membership_status = input("Enter Your Membership Status 'yes' or 'no' - - -  ")
# if user_age < 18 or user_age > 60 or membership_status == 'yes':
#     print("Eligible for discount, Discount Applies !!!")
# else:
#     print("Not Eligible")

# # Even-Odd Range Check
# # Ask the user for a number.
# # Check if the number is even and lies between 10 and 50 (inclusive).
# # Print "Valid number" if true, else "Invalid number".

# e_o_number = int(input("Enter the number between 10 and 50 and check whether the number is even or odd - - -  "))
# print(e_o_number)
# if(e_o_number >= 10 and e_o_number <= 50):
#     print("The Number You Have Entered is 'Valid' : ) ")
#     print("It's Even Number") if e_o_number % 2 == 0 else print("It's Odd Number")
# else:
#     print("Invalid Number")

# # Password Strength Checker
# # Ask the user to enter a password.
# # Check if the password length is at least 8 characters and it contains the word "@" or "#".
# # Print "Strong password" or "Weak password".
# pass_strength_checker = input("Enter Your Password Here - - -  ").strip()
# if (len(pass_strength_checker) >= 8) and ('@' in pass_strength_checker or '#' in pass_strength_checker):
#     print("Strong Password")
# else:
#     print("Weak Password")

# # Temperature Alert System
# # Ask the user for the current temperature in Celsius.
# # If the temperature is below 0 or above 40, print "Extreme weather alert".
# # Otherwise, print "Weather is normal".
# current_temp = int(input("Enter the Cureent Temprature in Umbergaon Gujarat here - - -  "))
# print(current_temp,"Degree Celcius")
# if current_temp <= 0 or current_temp >= 40:
#     print("Extreme Weather Alert!!!")
# else:
#     print("Weather is Normal")

# Practise nested if statment
# ATM Withdrawal Check
# Ask the user for their account balance and withdrawal amount.
# If the balance is sufficient, check if the withdrawal amount is a multiple of 100.
# If both are valid, print "Transaction successful", else print the specific reason.
print(" ~~~ ATM WITHDRAWAL CHECK ~~~ ")
account_balance = int(input('Enter Your Account Balance Here - - -  ').strip())
withdrawal_amount = int(input('Enter Your Withdrawal Amount - - -  ').strip())
print(f"AVAILABLE BALANCE : {account_balance} WITHDRAWAL AMOUNT : {withdrawal_amount} ")
if account_balance >= withdrawal_amount:
    print("SUFFICIENT BALANCE : - ) ")
    if withdrawal_amount % 100 == 0:
        print("TRANSACTION SUCCESSFULL : - ) ")
    else:
        print("Please enter The withdrawal amount that is multiple of 100 i.e - 200, 300, 400, 500, 600, 1000 and so on....")
else:
    print(" INSUFFICIENT BALANCE : - ( ")

# Student Grade Evaluator
# Ask the user for their marks (0–100).
# If marks are 40 or above, check if they scored 75 or more.
# If yes, print "Distinction"
# Else, print "Pass"
# If marks are below 40, print "Fail"

print(" ~~~ STUDENT GRADE EVALUATOR ~~~ ")
students_marks = int(input("Enter [0 - 100] Your Marks Here - - -  ").strip())
print("Total Marks Acquired", students_marks)
if students_marks >= 40:
    if students_marks >= 75:
        print("Distinction")
        print("Passed With Good Marks") 
    else:
        print("Pass")
else:
    print("Fail")

# Online Shopping Eligibility
# Ask the user if they have an account (yes or no).
# If yes, ask if they have added items to the cart.
# If yes, print "Ready to checkout"
# Else, print "Add items to cart first"
# If no account, print "Please create an account"
print(" ~~~ ONLINE SHOPPING ELIGIBILITY ~~~ ")
confirm_user_account = input("Hello User : ) Do You Have An Online Shopping Eligibility Account ? yes or no ---  ").lower().strip()

if confirm_user_account == "yes":
    add_to_cart = input("Have You Added the Items to the Cart ? yes or no ---   ").strip().lower()
    if add_to_cart == "yes":
        print("Proceed To Checkout")
    else:
        print("Add Items to the Cart First")
else:
    print("Please Create an Account First")

# Driving License Eligibility
# Ask the user for their age.
# If age is 18 or above, ask if they have passed the driving test (yes or no).
# If yes, print "License Approved"
# Else, print "Test Required"
# If under 18, print "Not eligible for license"

print(" ~~~ DRIVING LICENSE ELIGIBILITY ~~~ ")
driver_age = int(input("Enter Your Age Driver ---  ").strip())
print(driver_age)
if driver_age >= 18:
    driving_test = input("Driver! Have You Passed The Driving Test 'yes' or 'no' ---  ").lower().strip()
    if driving_test == "yes":
        print("License Approved : - ) ")
    else:
        print("Retest Required, Passing Required - [Only then license will be approved]")
else:
    print("Not Eligible For License")

# Festival Offer Checker
# Ask the user for the current month (as a number).
# If the month is October or November, ask if they are a registered member.
# If yes, print "Festival offer applied"
# Else, print "Register to avail offer"
# If not October or November, print "No festival offers currently"

print(" ~~~ FESTIVAL OFFER CHECKER ~~~ ")
user_current_month = int(input('Enter Current Month [as a number] ---  '))
if user_current_month == 1:
    user_current_month = "january"
    print("January")
elif user_current_month == 2:
    user_current_month = "february"
    print("February")
elif user_current_month == 3:
    user_current_month = "march"
    print("March")
elif user_current_month == 4:
    user_current_month = "april"
    print("April")
elif user_current_month == 5:
    user_current_month = "may"
    print("May")
elif user_current_month == 6:
    user_current_month = "june"
    print("June")
elif user_current_month == 7:
    user_current_month = "july"
    print("July")
elif user_current_month == 8:
    user_current_month = "august"
    print("August")
elif user_current_month == 9:
    user_current_month = "september"
    print("September")
elif user_current_month == 10:
    user_current_month = "october"
    print("October")
elif user_current_month == 11:
    user_current_month = "november"
    print("November")
elif user_current_month == 12:
    user_current_month = "december"
    print("December")
else:
    print("Enter a valid number for month please.....")
    exit()   

if (user_current_month == "october") or (user_current_month == "november"):
    registered_member = input("Are You a Registered Member sir ? [yes or no] --  ").lower()
    if registered_member == "yes":
        print("Festival Offers Applied : - ) ")
    else:
        print("Register To Avail Festival Offers ")
else:
    print("No Festival Offers Currently : - (  ")