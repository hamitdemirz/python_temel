#!/usr/bin/env python
# coding: utf-8

# In[4]:


#patika python temel proje


# In[6]:


def flatten_list(nested_list):
    flattened_list = []
    
    for eleman in nested_list:
        if type(eleman) == list:
            flattened_list.extend(flatten_list(eleman))
        else:
            flattened_list.append(eleman)
    
    return flattened_list


# In[7]:


input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)
print(output_list)


# In[10]:


def reverse_list(lst):
    reversed_lst = []
    for eleman in lst[::-1]:
        if type(eleman) == list:
            reversed_lst.append(reverse_list(eleman))
        else:
            reversed_lst.append(eleman)
    
    return reversed_lst


# In[11]:


input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)


# In[ ]:




