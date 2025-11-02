print("|| Shree Ganesh ||")
print (" Radha Radha ")

import sys
print(sys.version)

print("RadhaKrishna")

# Indentation very important thing in python.
# Statements

print("ParvatiShiv")

# Multiple statements
print("RadhaKrishna")
print("ParvatiShiv")
print("SaraswatiBrahma")

#Print text
print("*" * 30)

print("Radha",end = "")
print("Krishna")
#this displays both the statements without getting into the new line.

#print numbers
print(56)

print(2 * 2)

print(5000 + 1000054)

#this is how comments are performed in python.
 
# Variables in python
a = 10
b = 20
print(a * b)

c = 10
d = "Radha"
print(c, d)

e = "Saraswati"
e = "Brahma"
print(e)
#will consider brahma on priority and display the same.

F = "Parvati"
f = "Shiv"
print(F, f)

#casting
g = str("Radha")
print(g)
h = int(1)
print(h)
i = float(25.5)
print(i)

#get the type.
j = 2
print(type(j))

# Naming conventions in python
#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# #illegal names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#Camel Case
myVariableName = "Radha"
#Pascal Case
MyVariableName = "Krishna"
#Snake Case
my_variable_name = "RadhaKrishna"

#Assign multiple values to the multiple variables together
k,l,m = ["Radha","Krishna","Saraswati"]
print(k,l,m)

#Same value to multiple variables

n=o=p = "Radha"
print(n)
print(o)
print(p)

#unpack a collection
generator_operator_destroyer = ["Brahma","Vishnu","Mahesh"]
G,O,D = generator_operator_destroyer
print(G)
print(O)
print(D)

#Output Variables
q = "Radha "
r = "is "
s = "Awesome"
print(q,r,s)
print(q+r+s)

t = 10
u = 20
print(t + u)

v = 10
w = "Krishna"
print(v, w)

#Global variables
x = "Radha"

def myfunc():
    print("Devi is " + x)
    
myfunc()

y = "Krishna"

def merafunc():
    global y
    y = "Radha"
merafunc()
print("Devi is Radha" + y)

#Data types in python
# Str with typecasting
A = "Radha"
print(A)
B = str("Radha")
print(B)
#int with typecasting
C = 10
print(C)
D = int(10.0)
print(D)
#float with typecasting
E = float(14.5)
print(E)
F = 14.6
print(F)

#Complex with casting
G = 1j
print(G)
H = complex(1)
print(H)

#list with casting
I = ["RadhaKrishna","ParvatiShiv","SaraswatiBrahma"]
print(type(I))
J = list(("RadhaKrishna","ParvatiShiv","SaraswatiBrahma"))
print(J)

#tuple with casting
K = ("RadhaKrishna","ParvatiShiv","SaraswatiBrahma")
print(type(K))
L = tuple(("RadhaKrishna","ParvatiShiv","SaraswatiBrahma"))
print(L)

#Range with casting
M = range(0 , 10, 2)
print(M)

#Dictionary alongwith casting
N = {"Name" : "RadhaKrishna", "age" : 6000}
print(type(N), N)
O = dict(Name = "RadhaKrishna", age = 6000)
print(O)

#Set with Typecasting
P = {"RadhaKrishna","ParvatiShiv","SaraswatiBrahma"}
print(type(P), P)
Q = set(("RadhaKrishna","ParvatiShiv","SaraswatiBrahma"))
print(Q)

#Frozenset with type casting
R = frozenset({"RadhaKrishna","ParvatiShiv","SaraswatiBrahma"})
print(type(R),R)
S = frozenset(("RadhaKrishna","ParvatiShiv","SaraswatiBrahma"))
print(type(S),S)

#boolean with typecasting
T = True
U = bool(0)
V = bool(1)
print(type(T), T)
print(U)
print(V)

#Bytes with type casting

W = b'Ganeshay'
print(type(W),W)
X = bytes(10)
print(X)

#Bytearray wityh casting
Y = bytearray(5)
print(Y)
Z = bytearray(10)
print(Z)

#Memory view bytes with casting



