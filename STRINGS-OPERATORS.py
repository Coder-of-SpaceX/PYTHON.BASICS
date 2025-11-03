# Strings
print("Shree Ganesh")
print("Radha")

# Quotes inside Quotes
print("Radha's Krishna")
print('"RadhaKrishna" Both are pure lovers')

# Assign string to a variable
a = "RadhaKrishna"
print(a)

#Multiline Strings
#Double Quotes
b = """
Radha radha radha radha radha radha radha
radha radha radha radha radha radha radha
radha radha radha radha radha radha radha
radha radha radha radha radha radha radha
radha radha radha radha radha radha radha 
"""
print(b)

# or Single Quotes
c = '''
Radha Radha Radha Radha Radha Radha Radha Radha
Radha Radha Radha Radha Radha Radha Radha Radha
Radha Radha Radha Radha Radha Radha Radha Radha
Radha Radha Radha Radha Radha Radha Radha Radha
Radha Radha Radha Radha Radha Radha Radha Radha 
'''
print(c)

# String are arrays
d = "RadhaKrishna"
print(d[0:5])

#Looping through a string
for e in "RadhaKrishna":
    print(e)

# Find the length of the string
f = "RadhaKrishna"
print(len(f))
print(f)

# Check  the string
g = "RadhaKrishna both are pure lovers"
print("both" in g) # True
print("RADHAKRISHNA" in g) # False
print("RadhaKrishna" in g) # True

# Check using if statement
if "RadhaKrishna" in g:
    print("Yes God's name is available")
else:
    print("No God's name is not available or the string is case sensitive ")

# Check If not
if "RADHAKRISHNA" not in g:
    print("The name is in Pascal Case and not in upper case")
else:
    print("Yes the  name is in pascal case and is available")

# Slicing Strings
h = "RadhaKrishna"
print(h[0:5])
print(h[:12])
print(h[0:])
print(h[-12:])
print(h[-12 :-7])

#Modify Strings
# Upper case
i = "radhakrishna"
print(i.upper())

# Lower case
j = "RADHAKRISHNA"
print(i.lower())

# Strip
k = "  RadhaKrishna  "
print(k.strip())

# Replace
l = "PrachiDeepu"
print(l.replace("Deepu","Dhaval"))

# Split string
m = "Prachi.Deepu"
print(m.split("."))

# Concatenate strings
n = "Radha"
o = "Krishna"
print(n + o)

# add a space between the names
p = "Prachi"
q = "Deepu"
print(p + "    " + q)

# Format Strings
r = "Radha"
print(f"Krishna loves {r}")

# place holder as well as modifier
price = 60
print(f"The price of the product is {60}$")
# add a modifier with it
print(f"The price of the product is {price : .2f}$")

# perform a math operation in the placeholder
print(f"the price of the product is {60 * 18 : .2f}$")

# More String Methods will see in free time.....

# Escape characters
s = "Radha\'s Krishna"
print(s)
t = "RadhaKrishna\\ParvatiShiv\\SaraswatiBrahma"
print(t)
u = "RadhaKrishna\nParvatiShiv\nSaraswatiBrahma"
print(u)
v = "Prachi\t \t Deepu"
print(v)
w = "Radha \bKrishna"
print(w)

#Booleans

print(10>9)
print(9>12)
print(11==12)

# Bool using conditional statements
print("*" * 50)
x = 400
y = 300
if x > y:
    print(x > y)
else:
    print(x > y)

print("*" * 50)

print (bool("RadhaKrishna")) #True
print (bool(123456)) #True
print (bool(["RadhaKrishna","ParvatiShiv","SaraswatiBrahma"])) #True
print (bool()) #False
print (bool(0)) #False
print (bool(None)) #False
print (bool([])) #False

#Operators in python
#Arithmatic Operators
z = 10
A = 20
add = z + A
sub = z - A
multiply = z * A
divide = z / A # Note Division Returns before and after decimal values that is 10.12
Modulus = z % A
floordivide = z // A #Note Floor division only returns value before decimal that is 10 it will skip .12. 
exponentiation = z ** A
print(add, sub, multiply, divide, Modulus, floordivide, exponentiation)

print("*" * 50)
#Assignment Operators
B = 10
B += 5
print(B)
B -= 5
print(B)
B *= 5
print(B)
B /= 2
print(B)
B %= 10
print(B)
B **= 5
print(B)
B //= 5
print(B)

#Comparison operators
C = 10
D = 20
print(C > D) #False
print(C < D) #True
print(C == D) #False
print(C != D) #True
print(C >= D) #False #Greater than or equal to 
print(C <= D) #True #Less than or equal to

#Logical Operators
#and, or, not
E = 10
F = 20
#and
if E >= F and F <= E:
    print("Yes 'e' is greater")
else:
    print("No 'f' is greater")
#or
if E != F or F <= E:
    print("Anyone condition is true")
else:
    print("No condition is true")
    
#not
if not E >= F:
    print(True)
else:
    print(False)
    
print("*" * 50)
    
# Identity Operators
G = ['RadhaKrishna','ParvatiShiv','SaraswatiBrahma']
H = ['RadhaKrishna','ParvatiShiv','SaraswatiBrahma']
I = G
print(G is H) #False
print(G is not H) #True
print(G is I) #True
print(G is not I) #False
print(H is I) #False
print(H is not I) #True
print("*" * 50)
print(G == H) # True
print(I == G) # True
print("*" * 50)

J = 10
K = 10
L = J
print(J is K) #True
print(K is J) #True
print(J is L) #True
print(K is L) #True
#note - 
# | Data Type         | Changeable?                  | Memory Reuse? | Why                                         |
# | ----------------- | ---------------------------- | ------------- | ------------------------------------------- |
# | **int** / numbers | ❌ Not changeable (immutable) | ✅ Yes         | Value kabhi change nahi hoti, so reuse safe in memory |
# | **list**          | ✅ Changeable (mutable)       | ❌ No          | Value badal sakti hai, so reuse risky in memory|

#Membership operators
#in,not in
print("*" * 50)
M = "RadhaKrishna Are pure Lovers"
if "Are" in M:
    print(True)
else:
    print(False)

if "pure" not in M:
    print(True)
else:
    print(False)

print("RadhaKrishna" in M)
print("RADHAKRISHNA" not in M)
# Bitwise operators will see later when free time......

# Operators Precedence
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) #O/P - 0

#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(100 + 5 * 3) # O/P - 115

#Please even check bitwise operators in  this operators precedence it necessary
#If two operators have the same precedence, the expression is evaluated from left to right.
#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5+4-7+3) #O/P - 5






