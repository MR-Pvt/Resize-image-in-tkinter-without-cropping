#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from resizeimage import resizeimage

root = tk.Tk()

# the path of image 
path = ("C:/Users/rafay/images/1.jpg")

img = Image.open(path)

# the size of resizement
#      width /  height
size =  600,      700

#image resizing
img2 = img.resize(size,Image.ANTIALIAS)

img1 = ImageTk.PhotoImage(img2)
label = tk.Label(root, image=img1)
label.pack()

root.mainloop()


# In[ ]:





# In[ ]:




