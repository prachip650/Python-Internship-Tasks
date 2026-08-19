## Task 1
name = ["Prachi", "Ranu", "Tanu"]
print(name)

# Access
print("First student",name[0])

# Add
name.append("Neha")
print(name)

# Update
name[1] = "Anjali"
print(name)

# Remove
name.remove("Neha")
print(name)

# sort
name.sort()
print(name)


# #Task 2
number = (10,40,30,50,20,70)
print(number)

# accessing
print(number[1])

# slicing
print(number[1:5])

# length
print(len(number))

# basic operations
print("concatention",number+(50,40))
print("rwpetition",number*2)

## Task 3
num = {1,2,4,5,6,7,3,2,5,3,2}
print(num)

# add
num.add(8)
print(num)

# remove
num.remove(7)
print(num)

# union
set1 = {1,2,3,4}
set2 = {3,5,6,8,}
print(set1.union(set2))

# interdection
print(set1.intersection(set2))

# difference
print(set1.difference(set2))


# Task 4
student ={"Name":"Prachi",
"Age":20,
"Course":"B.tech",
"City":"Indore"}

# Accessing value
print(student["Name"])

# Accessing new key-value
student["College"]="Swami Vivekanand College of Enngineering"

# Updating value
student["Age"] = 21

# Remmoving value
student.pop("City")

# Display key
print(student.keys())

# Display value
print(student.values())

# Display all key-value pairs
print(student.items())
print(student)


