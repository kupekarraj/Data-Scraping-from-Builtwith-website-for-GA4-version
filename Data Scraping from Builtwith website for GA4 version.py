#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing all the necessary libraries
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[ ]:


#initialise the web driver
browser=webdriver.Chrome("/Users/rajkupekar/chromedriver")


# In[ ]:


#accessing the Builtwith page
url="https://builtwith.com/"
browser.get(url)


# In[ ]:


#creating a data frame to append the output results
output_data=pd.DataFrame(columns=["Domain_URL","GA4?"])


# In[ ]:


#creating a list of inputs appended with the Builtwith page
text=["https://builtwith.com/www.visitdenmark.com","https://builtwith.com/www.egypt.travel"]


# In[ ]:


#looping through the company's list and fetching the required details.
for element in text:
    link=element
    browser.get(link)
    print(link)
    src=browser.page_source
    soup=BeautifulSoup(src,'lxml')
    if soup =='https://trends.builtwith.com/analytics/Google-Universal-Analytics':
        result= "NAN"
    else:  
        result= soup.find('a',href="https://trends.builtwith.com/analytics/Google-Analytics-4")
    #saving the data
    output_data=output_data.append({"Domain_URL":link,"GA4?":result},ignore_index=True)
    


# In[ ]:


#printing the top rows of the output
output_data.head()

