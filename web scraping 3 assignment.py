#!/usr/bin/env python
# coding: utf-8

# In[19]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# In[20]:


driver=webdriver.Chrome()


# In[21]:


driver.get("https://www.amazon.in/")


# In[22]:


guitar_title=[]


# In[23]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
for i in title_tags:
    title=i.text
    guitar_title.append(title)


# In[24]:


print(len(guitar_title))


# In[35]:


import pandas as pd
df=pd.DataFrame({'Guitar':guitar_title})
df


# In[28]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# In[29]:


driver=webdriver.Chrome()
driver.get("https://www.digit.in/")


# In[30]:


laptop_title=[]


# In[31]:


title_tags=driver.find_elements(By.XPATH,'//h3[@class=" text-clamp text-clamp-2"]')
for i in title_tags:
    title=i.text
    laptop_title.append(title)


# In[32]:


print(len(laptop_title))


# In[34]:


import pandas as pd
df=pd.DataFrame({'Best_Gaming_laptop':laptop_title})
df


# In[1]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay=5


# In[3]:


driver=webdriver.Chrome()
driver.get("https://www.forbes.com/")


# In[12]:


Rank_title=[]


# In[7]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="card--large__title"]')
for i in title_tags:
    title=i.text
    Rank_title.append(title)


# In[8]:


print(len(Rank_title))


# In[9]:


import pandas as pd
df=pd.DataFrame({'BIllionare':Rank_title})
df


# In[17]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay=5


# In[18]:


driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[19]:


brand_title=[]
price_title=[]
description_title=[]


# In[20]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="KzDlHZ"]')
for i in title_tags:
    title=i.text
    brand_title.append(title)
title_tags=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj _4b5DiR"]')
for i in title_tags:
    title=i.text
    price_title.append(title)
title_tags=driver.find_elements(By.XPATH,'//div[@class="_6NESgJ"]')
for i in title_tags:
    title=i.text
    description_title.append(title)


# In[21]:


print(len(brand_title),len(price_title),len(description_title))


# In[22]:


import pandas as pd
df=pd.DataFrame({'Brand_Name':brand_title,'Price':price_title,'Desciption':description_title})
df


# In[26]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay=5


# In[34]:





# In[28]:





# In[ ]:




