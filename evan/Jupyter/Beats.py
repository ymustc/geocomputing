
# coding: utf-8

# In[ ]:




# <h2> Beat frequencies </h2>
# 
# <p>Insert my story teliing here<p>

# A NumPy array can be auralized automatically. The `Audio` class normalizes and encodes the data and embeds the resulting audio in the Notebook.
# 
# For instance, when two sine waves with almost the same frequency are superimposed a phenomena known as [beats](https://en.wikipedia.org/wiki/Beat_%28acoustics%29) occur. This can be auralised as follows:

# In[2]:

import numpy as np
from IPython.display import display, Audio 


# # Make two sine waves.

# In[3]:

max_time = 3
f1 = 250.0
f2 = 251.0
rate = 8000.0
L = 4
times = np.linspace(0,L,rate*L)
phase = 180.0*(np.pi / 180.0)
signal = np.sin(2*np.pi*f1*times) + np.sin(2*np.pi*f2*times+phase)


# # A nice (but static) plot

# In[10]:


import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

plt.figure(figsize=(15,3))
plt.plot(times, signal, lw=0.15); plt.xlabel('time (s)'); plt.grid() 


# # An audio object

# In[6]:

Audio(data=signal, rate=rate)


# # Interactive widgets

# In[8]:

from ipywidgets import interact
from IPython.display import display, Audio, clear_output


# In[17]:

@interact(f1=(200.0,300.0), f2=(200.0,300.0))
def beat_freq(f1=250.0, f2=251.0, plot=False, color=['red','green','blue']):
    max_time = 3; rate = 10000
    times = np.linspace(0, max_time, rate*max_time)
    signal = np.sin(2*np.pi*f1*times) + np.sin(2*np.pi*f2*times)
    display(Audio(data=signal, rate=rate))
    if plot:
        plt.figure(figsize=(10,3))
        plt.plot(times[:rate], signal[:rate], color=color, lw=0.5)
    return signal


# In[ ]:



