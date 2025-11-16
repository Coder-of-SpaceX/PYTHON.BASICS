# Normal Syntax of list
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

# List items are ordered, changeable, allow duplicate values
# ordered and changeable exmaples further.... and now allows duplicate values examples
b = ["Radha","Radha","Radha","Radha","Radha","Radha"]
print(b)

# Check the length of the list 
c = ["Radha","Radha","Krishna","Krishna"]
print(c)
print(len(c))

# Different data type elements can be stored 
d = ["Radha","Krishna","Parvati","Shiv","Saraswati","Brahma"]
e = [1,2,3,4,5,6,7,8,9,10]
f = [True, False, True, False]
g = [1.5,2.5,3.5,4.5]
print(d,e,f,g)
print(type(d),type(e),type(f),type(g))
# ------------------OR---------------------
# Mixed Data types
h = ["Radha",1,1.5,True]
print(h)
print(type(h))

# The list constructor 
i = list(("Radha","Radha","Radha","Radha","Radha"))
print(i)
j = list((1,2,3,4,5,6,7,8,9,10,1.5,2.5,3.5,4.5,True,False,True,"Radha"))
print(j)

# # ACCESS LIST ITEMS 
# List elements can be accessed using index, list also consists index number alike strings.
# 1. Access Items
k = [1,2,3,"Radha","Krishna",1.5,True]
print(k[3])
# 2. Negative Indexing
l = ["Radha","Krishna","Parvati","Shiv","Saraswati","Brahma"]
print(l[-2])
# 3. Range of indexes
m = [1,2,3,4,5,6,7,8,9,10,"Radha","Radha","Radha","Radha",True, True]
print(m[0:13])
# Leaving out the start value of the index
n = ["Radha","Radha","Radha","Radha","Krishna","Krishna"]
print(n[:4])
# Leaving out the end value of the index
o = [1,2,3,4,5,6,7,8,9,10]
print(o[4:])
# Range of Negative indexes
p = ["Radha","Radha","Radha","Radha"]
print(p[-3:-1])
# Check if item exists
q = ["Radha","Radha","Radha","Radha"]
if q == "radha":
	print("Yes this Goddess name is available")
else:
	print("No the name is not available or the spelling is case sensitive or there is an spelling mistake")

# # CHANGE LIST ITEMS 
# For changing the Specific element in the list # we have to refer the index number of that element 
r = ["Radha","Krishna","Parvati","Shiv","Saraswati","ketu"]
print(r)
r[5] = "Brahma"
print(r)
# Change the elements as per range indexing of the index number
s = ["Radha","Radha","Radha","Krishna","Krishna","krishna"]
print(s)
s[1:3] = ["RadhaKrishna","ParvatiShiv"]
print(s)
# Change the single second value by replacing it with 2 values
t = [1,2,3]
print(t)
t[1:2] = ["Radha","Krishna"]
print(t)
# Change the second and third value by replacing it with one value
u = [1,2,3]
print(u)
u[1:3] = ["Radha"]
print(u)

# Insert new item without replacing the existing list 
# user insert() for the same 
v = ["Radha","Radha","Krishna","Krishna"]
v.insert(0,"RadhaKrishna")
print(v) 

# ADD LIST ITEMS
# Following are methods of adding list items that is - 
# insert()
# append()
# extend()

# Append items
w = ["Radha","Krishna","Parvati","Shiv","Saraswati","Brahma"]
print(w)
w.append("Surya")
print(w)

x = ["Radha","Krishna","Parvati","Shiv","Saraswati","Brahma"]
print(x)
x.append("All Are Trilok Patni and Pati")
print(x)

# Insert items
y = [1,2,3,4,5,6,7,8,9,10]
print(y)
y.insert(3,"Radha")
print(y)

z = [1,2,3,4,5,6,7,8,9,10]
print(z)
z.insert(10,"This all are 1-10 digits")
print(z)

print("*" * 50)
# Extend items 
A = [1,2,3,4,5]
B = [6,7,8,9,10]
print(A)
print(B)
A.extend(B)
print(A)

C = ["Laxmi","Parvati","Saraswati"]
D = ["Vishnu","Shiv","Brahma"]
print(C)
print(D)
C.extend(D)
print(C)

# # REMOVE LIST ITEMS 
# Following are the methods - 
# Remove()
# pop()
# del - keyword
# clear()

# Remove items
E = [1,2,3,4,5,6,7,8,9,11]
print(E)
E.remove(3)
print(E)

# F = [1,2,3,4,5,6,7,8,9,11]
# print(F)
# F.remove(2,3,4,5)
# print(F)
# Note - this code will throw an error as it won't allow to remove multiple elements from the list.
print(">>>>>")
G = [1,3,3,3,5,6,7,3,9,10]
print(G)
G.remove(3) # throws an error if not specified any value in it for deletion.
print(G)

# In remove method we dont specify index so will have to use pop method for the same.
H = [1,2,3,4,5,6,7,8,9,10]
print(H)
H.pop(0) # But can only specify the index in here & allows only single deletion
print(H)

I = [1,2,3,4,5,6,7,8,9,10]
print(I)
I.pop(3)
print(I)
# If won't specify any index value in the pop method so by default it'll delete the last item
J = [1,2,3,4]
print(J)
J.pop()
print(J)

# Del Method
K = [1,2,3,4,5]
print(K)
del K[3]
print(K)

L = [6,7,8,9,10]
print(L)
del L[2]
print(L)
# For deleting the entire list using del keyword
M = [1,2,3]
print(M)
del M
pass

# Clear Method
# Clear the list using the clear method
N = [1,2,3]
print(N)
N.clear()
print(N)

O = [1,2,3]
print(O)
O.clear()
print(O)