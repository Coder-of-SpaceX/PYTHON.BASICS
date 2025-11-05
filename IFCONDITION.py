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
# One line if statement 
i = 5
j = 2
if i > j: print(f"{i} is greater")

# Short hand if...else
k = 50
l = 100
print(f"{k} is greater than {l}") if k > l else print(f"{l} is greater than {k}")

# Assing a value with if else
m = 100
n = 50
Elder =  m if m > n else n
print("Elder is...",Elder)
# Note you can't use print statement in this.

# Multiple conditions on one line
o = 100
p = 100
print(f"{0} is greater than {p}") if o > p else print(f"Both {o} & {p} are equal to each other") if o == p else print(f"{p} is greater than {o}")

