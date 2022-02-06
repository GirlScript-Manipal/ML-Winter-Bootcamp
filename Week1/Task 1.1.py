#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Remove all empty tuples from a list. Perform this task using both reverse() function and filter() function.
t = [() , (1,2,3) , ("A" , "B" , "C") ,() , ("git") , ("" , "") , (100)]
t.reverse()
l = filter(lambda x:x != () , t)
print ("original list:    " , t)
print ("after removal of empty tuples:  " , list(l))


# In[ ]:




