#!/usr/bin/env python
# coding: utf-8

# # List Methods
# ### The append():
# - It is the method in Python adds a single element to the end of a list. The element can be of any data type, including numbers, strings, other lists, or objects. 

# In[28]:


l=[1,2,13,24,85]
print(l)
l.append(6)
print(l)


# In[44]:


l1 = ['Samarth', 'Narayan']
print(l1)
l1.append('Omkar')
print(l1)


# ### list.sort()
# - This method sorts the list in ascending order. The original list is updated
# - Example 1:

# In[45]:


colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)


# In[46]:


name = ["Samarth", "Narayan", "More", "Omkar", "Rahul", "Prem"]
name.sort()
print(name)


# - What if you want to print the list in descending order? We must give reverse=True as a parameter in the sort method.
# - Example:

# In[47]:


num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


# In[48]:


colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


# ### reverse()

# In[52]:


colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


# ### index()
# This method returns the index of the first occurrence of the list item.

# In[56]:


num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.index(1))


# In[58]:


colors = ["voilet", "green", "indigo", "blue", "green"]
            #0         #1       #2        #3       #4
print(colors.index("green"))


# ### count()
# Returns the count of the number of items with the given value.

# In[59]:


num = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num.count(1))


# In[60]:


colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))


# ### copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# In[68]:


n = [4,2,5,3,6,1,2,1,2,8,9,7]
p=n
p[0]=0
print(n)
print(p)


# In[67]:


n = [4,2,5,3,6,1,2,1,2,8,9,7]
p=n.copy()
p[0]=0
print(n)
print(p)


# In[69]:


colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)


# ### insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# In[70]:


name = ["Ram", "Sham", "Govind", "Hari", "Rajesh", "Hrishi"]
name.insert(1,55)
print(name)


# In[71]:


colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)


# In[72]:


num = [12,13,14,15,16,17,18,19,20]
num.insert(1,500)
print(num)


# ### extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# In[74]:


num = [12,13,14,15,16,17,18,19,20]
colors = ["voilet", "indigo", "blue"]
num.extend(colors)
print(num)


# In[75]:


#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


# ### Concatenating two lists:
# You can simply concatenate two lists to join two lists.

# In[76]:


colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)


# In[77]:


name = ["Samarth", "Nagesh", "More"]
number = [1,2,3,4,5,6,7,8]
print(name+number)


# In[ ]:


name = ["Samarth", "Nagesh", "More"]
number = [1,2,3,4,5,6,7,8]
new=name+number
print(name)

