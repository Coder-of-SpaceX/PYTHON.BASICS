print("Shree Ganesh")
# Normal syntax of match statement
day = int(input("Enter your lucky day here -  "))
print(day)
match day:
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

# If user inputs invalid value so for that default value has to be displayed
month = int(input("Enter the number of your birth month -  "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid number of birth month")

# Combine values if samething has to be printed for some of the things
# we use pipe symbol for combining the case values 
even_odd = int(input("Enter the number from 0 - 20 and check whether its even or odd -   "))
print(even_odd)
match even_odd:
    case 0|2|4|6|8|10|12|14|16|18|20:
        print("Even")
    case 1|3|5|7|9|11|13|15|17|19:
        print("Odd")
    case _:
        print("Numbers from 0 - 20 and within 0 - 20 are only allowed")
        
D = int(input("Enter the anyone number from 1 to 10 day -  "))
M = input("Enter any one month [May or June] -  ")
match D:
    case 1|2|3|4|5|6|7|8|9|10 if M == "May":
        print("It's Deepu's Birthday on this day")
    case 1|2|3|4|5|6|7|8|9|10 if M == "June":
        print("It's Rainy season now buddy")
    case _:
        print("Invalid date/month selected please select as per the limit mentioned")