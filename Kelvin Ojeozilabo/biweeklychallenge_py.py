
name = input("Enter name: ")
age = input("Enter age: ")
print("Hi, my name is " + name + ", and I am " + age + " years old.")

year = 2021

dob = year- int(age)
print(dob)

age = 38
if (age <=1): 
  group = "infants"
elif (age >=1) & (age <=11):
  group = "Children"
elif (age >=11) & (age <=18):
  group = "Teens"
elif (age >=18) & (age <=65):
  group = "Adults"
else:
  group = "older Adult"
print(group)

dec_ago = age - 10

dec_ago

for i in range(10, 60, 10):
  print(i)

current_age =38
current_year =2020
new_age = []
new_year = []


for i in range(10, 60, 10):
  new = age + i
  new_age.append(new)
  print (new_age)
  new_y = year + i
  new_year.append(new_y)
  print(new_year)

new_year

new_age

len(new_age)

for i in range(len(new_age)):
 a = new_age[i]
 b = new_year[i]
 print (a, b)

new_age[1]

import numpy as np
next_fifty_age = np.array=([36,46,56,66,77])
next_fifty_age

next_fifty_year = np.array =([2030,2040,2050,2060,2070])
next_fifty_year

first_concat = "Hi, " +" Mr "+str(name)+" of "+ str(age) +" years old,"
print(first_concat)
second_concat = "Your year of birth is "+ str(dob)
print(second_concat)
third_concat = "As you are "+str(age)+" years old " +" you are an "+str(group) 
print(third_concat)
fourth_concat = "In 2011 you were-"+str(dec_ago)+" Years old, "
print(fourth_concat)
fifth_concat = "In "+str(new_year[0])+", You'll be "+str(new_age[0])+" years old"
print(fifth_concat)
sixth_concat = "In "+str(new_year[1])+", You'll be "+str(new_age[1])+" years old"
print(sixth_concat)
seventh_concat = "In "+str(new_year[2])+", You'll be "+str(new_age[2])+" years old"
print(seventh_concat)
eigth_concat = "In "+str(new_year[3])+", You'll be "+str(new_age[3])+" years old"
print(eigth_concat)
ninth_concat = "In "+str(new_year[4])+", You'll be "+str(new_age[4])+" years old"
print(ninth_concat)