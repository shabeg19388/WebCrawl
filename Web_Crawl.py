#!/usr/bin/env python
# coding: utf-8

# In[269]:


#Shabeg Singh Gill
#IIITD

import pandas as pd 
import requests 
from bs4 import BeautifulSoup as b

#scraping tshirts
prods=[] 
name2=[] #list for product names
desc2=[] #list for tshirt description 

for x in range(1,8): #using pagination to iterate over multiple pages 
 
    #mainurl= "https://www.amazon.in/s?k=tshirts "https://www.amazon.in/s?k=t-shirts&page=3
    mainurl="https://www.amazon.in/s?k=t-shirts&page="
    #requesting for url
    req= requests.get(mainurl+str(x))
    #parsing using html/lxml
    soup =b(req.content,'html.parser')
    
    #https://www.amazon.in/s?k=t-shirts&qid=1622469644&ref=sr_pg_1
    
    #finding significant div class 
    proddiv2= soup.find_all('div', {'class':'a-section a-spacing-none a-spacing-top-small'})
    
    #iterating over all such divs 
    for i in proddiv2:
        #finding h5 in each div 
        head= i.find('h5', {'class':'s-line-clamp-1'})
        #print(head)
        
        #checking if h5 has any content or not 
        if head is not None:
            #it does so find span in order to get product name 
            sp=head.find('span',{'class':'a-size-base-plus a-color-base'}).text 
            #appending to product name list 
            name2.append(sp)
     
        #finding product description through span 
        dc=i.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'})
        #checking if span has any content or not 
        if dc is not None:
            #it does so appending to description 
            desc2.append(dc.text)
    
#making a dictionary
a= {'Company': name2,'Description': desc2}

#converting dict to data frame 
df1 = pd.DataFrame.from_dict(a, orient='index')

#taking transpose of data frame to make things / data clearer 
df1=df1.transpose()

#converting df to csv for stroing anf making things easier 
df1.to_csv('Amazon_Tshirts.csv')

#finally printing data frame for obtaining relevant data 
print(df1) 

#print(name2)
#print(" ")
#print(desc2)

    #req = requests.get(getnext(mainweburl))
    #soup = b(req.text, 'html.parser')
    
    #prodlist= soup.find_all('li',attrs={'class','product-base'}) #list of products
    
    #for i in prodlist:
        #prodname= i.find("h3",{"class":"product-brand"}).text 
        #productdesc= i.find("h4", {"class":"product-product"}).text
        #names.append(prodname)
        #desc.append(productdesc)
    
    
    

    


# In[ ]:





# In[ ]:





# In[ ]:




