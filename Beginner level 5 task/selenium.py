from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# driver = webdriver.Chrome()
# Output = {}
# name_list = []
# price_list = []
# shipping_list = []
# save_list = []

# for page in range(1,21):
#     driver.get("https://www.newegg.com/p/pl?N=100027683&page=" + str(page))
#     parent = driver.find_element(By.CLASS_NAME, "item-cells-wrap")
#     children = parent.find_elements(By.CLASS_NAME, "item-cell")
#     for child in children:
#         name = child.find_element(By.CLASS_NAME, "item-title").text
#         price = child.find_element(By.CLASS_NAME, "price-current").text
#         shipping = child.find_element(By.CLASS_NAME, "product-delivery-new").text
#         save = child.find_element(By.CLASS_NAME, "price-save").text
#         name_list.append(name)
#         price_list.append(price)
#         shipping_list.append(shipping)
#         save_list.append(save)
# Output['name'] = name_list
# Output['price'] = price_list
# Output['shipping'] = shipping_list
# Output['save'] = save_list

# df = pd.DataFrame(Output)
# df.to_csv('selenium.csv')
# print(df)


df = pd.read_csv('selenium.csv')
newdf = df.fillna('NaN')
print(newdf)
newdf.to_csv('selenium.csv', index=False)
