#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data structures assignment


# In[28]:


# 1.Discuss string slicing and provide examples?

# String slicing in Python is a way to get specific parts of a string by using starting, end middle values.one of the example is
# shown below

string1= "aishwarya singh"
string2=string1[0:9]
print(string2)


# In[ ]:
"""  """

# 2.Explain the key features of lists in Python?

# key features of lists in python are listed below:
#     1. It is an ordered data structure
#     2. It is mutuable object which means values in list can be modified as well.
#     3. slicing, indexing concept is also there within the lists


# In[23]:


# 3.Describe how to access, modify, and delete elements in a list with examples?

# accessing the list
my_list=[10,"apple",3.14,True,[1,2,3]]
print(my_list[2])

# modifying the list
my_list[4]=False
print(my_list)

# delete elements
del my_list[4]
print(my_list)


# In[ ]:


# 4.Compare and contrast tuples and lists with examples?

# Tuples- Tuples are ordered but immutable collection of elements in python. We can do indexing, slicing but we cannot modify a 
# tuple which has a collection of elements within itself.

# Lists - Lists are ordered but mutable collection of elements in python. We can do indexing, slicing as well as we can modify a 
# list which has a collection of elements within itself.


# In[26]:


# 5.Describe the key features of sets and provide examples of their use?

# Key features of sets are-
# 1.It stores unique values within itself. No duplicate value exists in it. 
# 2.It is unordered in nature which means the elements present inside it are not in an order which basically results into that we 
# cannot access the eleemnts in sets by indexing. Since, there is no particular arranged order of the elements.
# 3.We cannot even modify the elements once they are listed in sets. It is unchangeable.


the_fruits={"apple","banana","grapes","mango","mango"}
print(the_fruits)


# In[ ]:


# 6.Discuss the use cases of tuples and sets in Python programming?

# Use Case of Tuple- Since tuples are immutable, they are ideal for storing fixed data like coordinates, database query results, or configuration 
# values that should not change.

# Use Case of Set- Sets automatically eliminate duplicate elements, making them ideal for deduplication tasks.


# In[34]:


# 7.Describe how to add, modify, and delete items in a dictionary with examples?

# adding items in dictionary
this_dict={
    "color":"red",
    "vehicle":"mustang",
    "model":"latest",
    "year":2024
}

this_dict["brand"]="ford"
print(this_dict)


# modify items in dictionary
this_dict.update({"year":2020})
print(this_dict)

# delete items in dictionary
this_dict.pop("model")
print(this_dict)


# In[ ]:


# 8.Discuss the importance of dictionary keys being immutable and provide examples?

# Dictionary keys must be immutable to ensure reliable and efficient operation.Dictionary keys are stored in a hash table, where
# the hash value of a key determines its location.If keys are mutable,their hash value could change,leading to inconsistencies
# or making the key inaccessible.

