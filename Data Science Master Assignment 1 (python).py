#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data: (i) string (ii) list (iii) float (iv) tuple

# In[2]:


a = "Prathmesh"
b = ["Prathmesh", 180, 80.4, 23]
c = 23.3
d = (1, 2, 3, 4, 5)


# In[3]:


print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Q2. Given are some following variables containing data:
#     (i) var1 = ''
#     (ii) var2 = '[ DS , ML , Python]'
#     (iii) var3 = [ 'DS' , 'ML' , 'Python']
#     (iv) var4 = 1.

# In[4]:


var1 = ''
print(type(var1))
var2 = '[ DS , ML , Python]'
print(type(var2))
var3 = [ 'DS' , 'ML' , 'Python']
print(type(var3))
var4 = 1.
print(type(var4))


# Q3. Explain the use of the following operators using an example: (i) / (ii) % (iii) // (iv) **

# In[5]:


# / Devision
34/2


# In[7]:


# % Modulus or remainder
35%2


# In[8]:


#// Floar devision

45//7


# In[9]:


# ** Power

2 ** 6


# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the element and its data type.

# In[10]:


A = ["Prathmesh", "Pj", 179, 23.3, 80.4, "Pulsar", 135, 10, "XL", 36]


# In[11]:


for i in A:
    print(i)
    print(type(i))


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[20]:


a = int(input())
b = int(input())
i = 0
while a%b == 0:
     a = a/b
     i +=1
if i>0:
    print(f"{b} devides {a} times.")
else:
    print(f"{b} does not devide {a}. ")


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

# In[31]:


for i in range(1,100,4):
    if i%3 == 0:
        print(i, "value is completely devisible by 3")
    else: 
        print(i, "value is not ccompletely devisible by 3")


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# 
# Mutable objects are those that allow you to change their value or data in place without affecting the object’s identity. 
# In contrast, immutable objects don’t allow this kind of operation. You’ll just have the option of creating new objects 
# of the same type with different values For eg List, Dictionary and sets are mutable datatype
# 

# In[36]:


#Mutable List Datatype
Fruits = ["Apple", "Banana", "Mango", "Papaya", "Cherry"]
Fruits.remove("Banana")
Fruits


# In[39]:


#change List items
Fruits[2] = ("orange")
Fruits


# In[40]:


Fruits.append("Banana")
Fruits


# In[41]:


# tuple is immutable object

No = (1, 2, 3, 4, 5, 6)


# In[42]:


No[1] = 9


# In[ ]:




