# Print i as long as i is less than 6:
a = 1
while a < 6:
	print(a)
	a+= 1

# Print i as long as i is less than 10:
b = 1
while b<11:
	print(b)
	if b == 6:break
	b += 1

print("*" * 50)
# Continue to the next iteration if i is 3:
c = 0
while c < 10:
	c += 1
	if c == 3:continue
	print(c)

# print 10 numbers using while loop 
d = 1
while d < 11:
	print(d)
	d += 1
else:
	print("Finally finished")

# print 10 numbers using while loop break on 6 use else statement in this too...
e = 1
while e < 11:
	print(e)
	if e == 6:break
	e += 1
else:
	print("Done")


print("*" * 50)
# continue after 3
f = 0
while f < 10:
	f += 1
	if f == 3:continue
	print(f)
else:
	print("Done")