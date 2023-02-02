#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import*
import time
#This function shows and changes the time 
def t():
    c_t = time.strftime("%H : %M : %S")
    l_2.config(text= c_t)
    l_2.after(100,t)

def d():
    c_d = time.strftime("%d : %B : %Y")
    l_4.config(text = c_d)
    l_4.after(100,t)
root = Tk()

l_1 = Label(root, text = "Digital Clock By Bhargav",font = "times 20 bold",fg = "blue",bg="green" )
l_1.grid(row = 0 , column = 0) # l_1 will be displayed in first column of first row

l_2 = Label(root,font = "times 25 bold",fg = "violet")
l_2.grid(row = 1 , column = 0) # l_2 will be displayed in first column of second row
t()

l_3 =Label(root, text = "Hour   Minute   Second",font = "times 10 bold")
l_3.grid(row = 2 , column = 0) # l_3 will be displayed in first column of third row

l_4 =Label(root,font = "times 20 bold")
l_4.grid(row = 3 , column = 0) # l_4 will be displayed in first column of fourthrowY
d()

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




