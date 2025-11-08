# Day of the Week
# Ask the user to enter a number from 1 to 7.
# Use match to print the corresponding day (e.g., 1 → Monday, 7 → Sunday).
# If the number is outside 1–7, print "Invalid day number".
print(" ~~~ Day of the Week ~~~ ")
days_of_week = int(input("Enter the day [as number] --  "))
match days_of_week:
    case 1: 
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4: 
        print("Thursday")
    case 5: 
        print("Friday")
    case 6: 
        print("Saturday")
    case 7: 
        print("Sunday")
    case _:
        print("Invalid day Number")

# Traffic Light System
# Ask the user to enter a color (red, yellow, green).
# Use match to print the action: "Stop" for red, "Wait" for yellow, "Go" for green.
# Handle unexpected inputs with a default case.

print(" ~~~ Traffic Light System ~~~ ")
traffic_signal_colour = input("Enter anyone Colour out of [red, yellow, green] --  ").lower().strip()
print(traffic_signal_colour)
match traffic_signal_colour:
    case "red":
        print("STOP")
    case "yellow":
        print("WAIT")
    case "green":
        print("GO")
    case _:
        print("Invalid Colour !!! : - (  ")

# Simple Calculator
# Ask the user to enter two numbers and an operator (+, -, *, /).
# Use match to perform the correct operation.
# Handle invalid operators with a default case.

print(" ~~~ Simple Calculator ~~~ ")
a = int(input("input(Enter Number 1 ---  "))
b = int(input("input(Enter Number 2 ---  "))
c = input("Enter any operator from given options [+, -, *, /] ---  ")
match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print("Invalid Operator")

# Grade Feedback
# Ask the user to enter a grade letter (A, B, C, D, F).
# Use match to print feedback: "Excellent", "Good", "Average", "Poor", "Fail".
# Handle any other input with "Invalid grade".
print(" ~~~ Grade Feedback ~~~ ")
user_grade = input("Enter Your Grade from [A,B,C,D,F] --  ").upper()
match user_grade:
    case "A": 
        print("Excellent")
    case "B": 
        print("Good")
    case "C": 
        print("Average")
    case "D": 
        print("Poor")
    case "F": 
        print("Fail")
    case _:
        print("Invalid Grade Entered")

# Language Greeting
# Ask the user to enter a language (english, hindi, gujarati, french, spanish).
# Use match to print a greeting in that language.
# If the language is not recognized, print "Language not supported".
print(" ~~~ Language Greeting ~~~ ")
greeting_language = input("Enter Greeting Language from [english, hindi, gujarati, french, spanish ] --  ").lower()
match greeting_language:
    case "english": 
        print("THANK YOU : ) ")
    case "hindi": 
        print("धन्यवाद : )")
    case "gujarati": 
        print("આભાર : )")
    case "french": 
        print("Merci : )")
    case "spanish": 
        print("Gracias : )")
    case _:
        print("Invalid Language Entered")



