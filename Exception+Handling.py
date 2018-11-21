
# coding: utf-8

# Exception Handling
# 1.	Write a python program to handle the following exceptions

# In[5]:


#Question 1.a
#IO error
try:
    f=open('SomeFile.txt','r')
except:
    print('IO error')


# In[6]:


#Question 1.b
#Value error
try:
    a=int('Sakshi')
except:
    print('Value Error')


# In[7]:


#Question 1.c
#Import error
try:
    from math import anything
except:
    print('Import Error')


# In[8]:


#Question 1.d
#Arithmetic error
try:
    x=2/0
except:
    print('Arithmetic error')


# In[9]:


#Question 1.e
#Overflow error
import math
try:
    print(int(math.pow(2, 1024)))
except:
    print('Overflow Error')


# In[10]:


#Question 1.f
#Zero division error
try:
    x=2/0
except:
    print('Zero division error')


# In[11]:


#Question 1.g
#Floating point error
a=9.345
b=0.00
try:
    print(a/b)
except:
    print('Floating point error')


# In[12]:


#Question 1.h
#Name error
try:
    print(x)
except:
    print('Name error')


# In[13]:


#Question 1.i
#Index error
a='Sakshi'
try:
    print(a[100])
except:
    print('Index error')

