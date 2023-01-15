#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Kosar Ahmadizadeh 


s = str(input())
sub = str(input())

def check(s,sub):
    if (len(s) < len(sub)) or (len(s)==len(sub) and s!= sub) or (sub == "" or s ==""):
        return ("no")
    
    if (s == sub):
        return ("yes")
    k=0
    i=0
    if len(s)> len(sub):
        while(i<len(sub)):
            if s[i]==sub[i]:
                k+=1
            i+=1   
                
    if k == len(sub):
        return("yes")
    if k != len(sub):
        s=s[1: ]
        
    return(check(s,sub))
            

check(s,sub)                 


# In[ ]:




