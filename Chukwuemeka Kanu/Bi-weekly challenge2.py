#!/usr/bin/env python
# coding: utf-8

# In[1]:


name_input = input('input your name: ')
age_input = int(input('input your age: '))
print('Hello', name_input,', you are', age_input, 'years old')

dob = 2021 - age_input
print('Your year of Birth is', dob)

if age_input<1:
    print('As you are', age_input, 'years old, you are an Infant')
elif age_input<=11:
    print('As you are', age_input, 'years old, you a an Child')
elif age_input<=17:
    print('As you are', age_input, 'years old, you are a Teen')
else:
    print('As you are', age_input, 'years old, you are an Adult')


decades = range(-10,51,10)
decade_age = 0
for i in decades:
    decade_calculation = 2021 + i
    decade_age = age_input + i
    print('In', decade_calculation, 'you were', decade_age, 'years old')

        


# In[ ]:




