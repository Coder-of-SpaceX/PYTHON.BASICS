# Normal Syntax of if statement
a = 200
b = 100
if a > b:
    print(f"Yes {a} is greater than {b} ")

number = 15
if number > 0:
    print(f"Yes the number {number} is a positive : ) number")
    
#Note as we discussed previously indentation is must in if statement else the code will throw an error

age = 26
if age > 20:
    print("Yes you are an adult now")
    print("You are eligible for marriage")
    print("You are an bread earner of the family now")
    print("Stay fit and follow your duties")
    
is_logged_in = True
if is_logged_in:
    print("Welcome Back !!")
    
# Normal syntax of Elif statement
c = 33
d = 33
if c > d:
    print(f"{c} is greater than {d}")
elif c == d:
    print(f"{c} & {d} both are equal to each other")
    
score = 75
if score >= 90:
    print("'A' Grade")
elif score >= 80:
    print("'B' Grade")
elif score >= 70:
    print("'C' Grade")
elif score >= 60:
    print("'D' Grade")

#Note - When you use elif, Python evaluates the conditions from top to bottom.
#As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
    
Age = 26
if Age < 14:
    print("You are still a child beta !")
elif Age < 20:
    print("You are a teenager beta !")
elif Age < 65:
    print("You are an adult as well as the bread earner of the family, Congratulations !!")
elif Age > 65:
    print("You are senior citizen now, best time to retire yourself and live your life peacefully")
    
#Note - Use elif when you have multiple mutually exclusive conditions to check.
#This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

day = 2
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
    
# Normal else statement syntax.
#Note - The else keyword catches anything which isn't caught by the preceding conditions.
#The else statement is executed when the if condition (and any elif conditions) evaluate to False.

e = 100
f = 50
if f > e:
    print(f"{f} is greater than {e}")
elif f == e:
    print(f"Both {f} & {e} are equal to each other.")
else:
    print(f"{e} is greater than {f}")

print("*" * 50)
#Else without Elif
g = 100
h = 50
if h > g:
    print(f"{h} is greater than {g}")
else:
    print(f"{g} is greater than {h}")
    
#Note - Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

Number = 1
if Number % 2 == 0:
    print(f"The given number {Number} is 'Even'")
else:
    print(f"The given number {Number} is 'Odd'")
    
# Complete if elif else chain -
temprature = 10
if temprature > 30:
    print("Weather is very 'Hot' Outside")
elif temprature > 20:
    print("Weather is 'Warm' outside")
elif temprature > 10:
    print("Weather is 'Cool' outside")
else:
    print("Weather is cold outside")
    
# Even erroro handling can be undertaken using else statement like  -
username = "RadhaKrishna"
if len(username) > 0:
    print(f"Welcome to our website ! {username}")
else:
    print("Error : Dear Mam/Sir Username cannot be empty")
    
# Normal syntax for shorthand if
# One line 'if statement' 
i = 50
j = 100
if i < j: print(f"{j} is greater")

# Shorthand if.....else
k = 100
l = 200
print(f"{k} is smaller") if k < l else print(f"{l} is smaller")

# Assign a value with if else
m = 10
n = 50
high_value = m if m > n else n
print(high_value)

# Mulitple coniditions on one line 
o = 200
p = 200
print (o) if o > p else print(p) if o < p else print(f"Both {o} & {p} are equal")

# Ternary operators are basically useful when simple assignments and return statements
q = 15
r = 20
max_value =  q if q < r else r
print(max_value)

#Setting a default value 
username = ""
print(username) if username else print("Guest User")

# Logical operators
s = 100
t = 200

if s < t and t > s :
    print("Yes T is greater and both the conidtions are correct due to which this code runned")
else:
    print("No its not meeting the condition as well as any one condition is wrong")

u = 100 
v = 200
w = 200
if u > v or v == w:
    print(True)
else:
    print(False)

x = 100 
y = 200
if not x > y:
    print(True)
else:
    print(False)

# combining mulitple operators
aging = 25
is_student = False
has_discount_code = True
if age > 0 or age < 65 and not is_student or has_discount_code :
    print("Discount available..")

temp = 25
is_raining = False
is_weekend = True
if temp > 20 and not is_raining or is_weekend:
    print("Best time for adventure trip")

uname = "RadhaKrishna"
passwd = "admin@123"
is_verified = True
if uname and passwd and is_verified:
    print(f"Welcome {uname} You logged in successfully")
else:
    print("User not verified and login unsucessfull")

# Range checking with logical operators
score = 80
if score > 0 and score < 100:
    print("Valid score")
else:
    print("Invalid score")

# Normal syntax of if statement in nested if 
z = 40
if z > 10:
    print("Number is above 10")
    if z > 20:
        print("Number is above 20")

years_old = 25
license_available = True
if years_old >= 18:
    print("Age is valid")
    if license_available:
        print("Yes you can drive")
    else:
        print("You are not eligible to drive without license")
else:
    print("Legal age of driving is 18 and you are still younger than that")    


result = 80
attendance = 90
assignment_submit = True
if result >= 60:
    print("Status : PASS")
    if attendance >= 80:
        print("Passed With Good attendance")
        if assignment_submit:
            print("Passed with perfect Assignment submition")
        else:
            print("passed but assignment not submitted")
    else:
        print("Passed but neeed to improve you attendance")
else:
    print("You are failed work hard next time")

weather_forcast = 25
is_sunny = True

if weather_forcast > 20:
    if is_sunny:
        print("Perfect beach Vibes!!!")

Username = "RadhaKrishna"
password = "admin@123"
is_active = True
if Username:
    if password:
        if is_active:
            print("Login Successfull")
        else:
            print("Login Unsuccessfull, user is inactive")
    else:
        print("Password Required")
else:
    print("Username Required")

goal = 92
credit = 5
if goal >= 90:
    if credit:
        print("A + Grade")
    else:
        print("A Grade")
elif goal >= 80:
    print("B Grade")
else:
    print("C GRADE OR BELOW")

# Normal syntax of if pass statement

# The pass statement is useful in several situations:
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

AB = 10
BC = 20
if AB < BC:
    pass

numeric = 2
if numeric % 2 == 0:
    pass
else:
    print("odd")

target = 80
if target > 60:
    pass
    print("Target Proccessed")

# if condition completed now initiate the practise for the same......
