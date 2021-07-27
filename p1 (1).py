from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd
import lxml


driver = webdriver.Chrome("chromedriver.exe")
products=[] 
prices=[]
brands=[]



driver.get("https://www.ajio.com/men-sports-shoes/c/830207008")
content = driver.page_source
soup = BeautifulSoup(content,'lxml')
for a in soup.findAll(attrs={'class':'item rilrtl-products-list__item item'}):
    brand=a.find(attrs={'class':'brand'})
    name=a.find(attrs={'class':'name'})
    price=a.find(attrs={'class':'price'})
    brands.append(brand.text)
    products.append(name.text)
    prices.append(price.text)
  
        
df = pd.DataFrame({'Brand':brands,'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

                        

