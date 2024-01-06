#!/usr/bin/env python
# coding: utf-8

# In[1]:


# metacharchters
# []Find all lower case characters alphabetically between "a" and "m":
import re

txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


# In[2]:


#\dFind all digit characters:

import re
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)


# In[3]:


# .Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

import re
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)


# In[4]:


#Check if the string starts with 'hello':
import re
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")


# In[5]:


#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
import re
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)


# In[7]:


#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
import re
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)


# In[12]:


#Check if the string contains either "falls" or "stays":

import re
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[ ]:




