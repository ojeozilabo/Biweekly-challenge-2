#!/usr/bin/env python
# coding: utf-8

# In[8]:


#printing users name and age
name = input()

age = input()

print("my name is "+ name +", my age is "+ str(age))


# In[10]:


#users date of birth
year = 2021
dob = year- int(age)
print(dob)


# In[177]:


#users age group
age = 27
if (age <1):
    Group = "Infant"
elif (age >=1) & (age <=11):
    Group = "Child"
elif (age >=12) & (age <=17): 
    Group = "Teens"
elif (age >=18) & (age <=64):
    Group = "Adult"
else:
    Group = "Older Adult"
print(Group)


# In[61]:


#users age a decade ago
decade=10
decade_ago =int(age)- decade
decade_ago


# In[71]:


# what the users age will be for the next 50 years
for i in range (10,60,10):
    print(i)


# In[89]:


current_age =26
current_year =2020
new_age = []
new_year = []

for i in range(10,60,10):
    new_a = current_age + i
    new_age.append(new_a)
    print(new_age)
    new_y = current_year + i
    new_year.append(new_y)
    print(new_year)


# In[86]:


new_age


# In[90]:


new_year


# In[104]:


for i in range(len(new_age)):
    c= new_age[i]
    d= new_year[i]
    print(c,d)


# In[132]:


import numpy as np
next_fifty_age = np.array=([36,46,56,66,77])
next_fifty_age


# In[133]:


next_fifty_year = np.array =([2030,2040,2050,2060,2070])
next_fifty_year


# In[219]:


#printing the final statement
first_concat = "Hello, " +"Miss "+str(name)+" You are " + str(age) + " years old,"
print(first_concat)
second_concat = "Your year of birth is "+ str(dob)
print(second_concat)
third_concat = "As you are "+str(age)+" years old, "+" you are an "+str(Group) 
print(third_concat)
fourth_concat = "In 2011 you were-"+str(decade_ago)+" Years old, "
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

