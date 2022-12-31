#!/usr/bin/env python
# coding: utf-8

# In[109]:


import matplotlib
import matplotlib.pyplot as plt
d = ['Geogrrafia','Química','Biologia','História']
prefere = [23,37,31,9]
cores = ['yellow', 'lightblue','orange','blue']
explode=(0,0,0,0)
plt.pie(prefere, explode=explode, colors=cores, labels=d)
plt.title('Preferência de Disciplinas')
plt.show()


# In[110]:


import matplotlib
import matplotlib.pyplot as plt
d = ['Geogrrafia','Química','Biologia','História']
prefere = [23,37,31,9]
cores = ['yellow', 'lightblue','orange','blue']
explode=(0,0,0,0)
plt.pie(prefere, explode=explode, colors=cores, labels=d)
plt.title('Preferência de Disciplinas')
#plt.legend()
plt.show()


# In[ ]:




