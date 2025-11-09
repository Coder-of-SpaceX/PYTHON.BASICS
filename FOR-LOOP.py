# Looping through list
gods = ["Generator", "Operator", "Destroyer"]
for a in gods:
    print(a)

# Looping Through strings 
love = "RadhaKrishna"
for b in love:
    print(b)

# The break statement 
devi_devta = ["Radha","Krishna","Parwati","Shiv", "Saraswati", "Brahma"]
for c in devi_devta:
    print(c)
    if c == "Shiv":break
    # O/P - Radha till Shiv


print("*" * 50)

# Break comes before the print 
bhakti = ["Hanuman Dada","Prahlad","Ganpati Bapa"]
for d in bhakti:
    if d == "Ganpati Bapa":break
    print(d)
    # O/P - Hanuman Data to Prahlad

# The continue statement 
numbers = [1,2,3,4,5,6,7,8,9]
for e in numbers:
    if e == 4:continue
    print(e)
print("--------------")
# Looping through range
ranger = range(0, 11, 2)
for f in ranger:
   if f == 6:continue
   print(f)


# Looping through tuple

fruits = ("Grapes","Apples","Banana","orange") 
for g in fruits:
    print(g)
    if g == "Banana":break

# looping through dictionary
dictionary = {"Name":"RadhaKrishna", "Describe" : "Devine Lovers","age":26, "Yuga":"Dwaparyuga"}
for h in dictionary:
    if h == "age":break
    print(h,":", dictionary[h])

# else block in for loops as well as looping through set
naam = {"Radha","Vallabh","Barsana","Vrishbhan","Vrindavan"}
for i in naam:
    print(i)
else:
    print("That's all")

list1 = [1,2,3,4,5,6,7,8,9,10]
for j in list1:
    if j == 8: continue
    print(j)
else:
    print("Finished!!")


print("*" * 50)
list2 = [1,2,3,4,5,6,7,8,9,10]
for k in list2:
    print(k)
    if k == 7:break
else:
    print("Finished!!")


# Nested loops 
list3 = ["Divine Lovers","God and Goddess","Creators"]
list4 = ["RadhaKrishna","Parwatishiv","SaraswatiBrahma"]
for l in list3:
    for m in list4:
        print(l,m)
    
# Pass Statement in  for loops
list5 = [1,2,3,4,5]
for n in list5:
    pass