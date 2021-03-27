#!/usr/bin/env python
# coding: utf-8

# # Singly_linked_list

# In[1]:


#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


# In[46]:


#creating_head
class LinkedList:
    def __init__(self):
        self.head=None
    
    
    #insertin_at_begin 
    def inserting_bgn(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.ref=self.head
            self.head=new_node
     
    
    #inserting_at_end
    def inserting_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            n=n.ref
        n.ref=new_node
        
            
        
    #traversing
    def traverse_LL(self):
        if self.head is None:
            print("Linked List is empty")
        n=self.head
        while n!=None:
            print(n.data)
            n=n.ref
    


# In[47]:


LL=LinkedList()
LL.inserting_end(20)
LL.inserting_end(10)
LL.inserting_end(30)
LL.traverse_LL()


# In[48]:


LL.inserting_bgn(40)


# In[49]:


LL.traverse_LL()


# In[ ]:




