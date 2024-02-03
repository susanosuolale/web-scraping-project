from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
import time
import pandas as pd
import numpy as np
import ast

# def pages_data(item_url): 
# start_url = "https://www.airbnb.com/s/Lagos--Nigeria/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=lagos%20nigeria&date_picker_type=calendar&source=structured_search_input_header&search_type=search_query&price_filter_num_nights=5"
# current_url = start_url


# amn_list = []
# dimen_list = []
# Output = {}
# name_list = []
# price_list = []
# # driver = webdriver.Chrome()



# for page in range(4):
#     #sorry couldnt do more than four pages because of poor network
#     #iterating through the pages
#     result = requests.get(current_url)
#     doc = BeautifulSoup(result.text, 'html.parser')
#     listings = doc.findAll("div", {"class": "c4mnd7m atm_9s_11p5wf0 atm_dz_1osqo2v dir dir-ltr"})
#     #get list of listings

#     for listing in listings:
#     #iterate through each listing
#         amts_list = []
#         #amenities storage
#         dim_list = []
#         #dimension storage
#         a_tag = listing.find('a')
#         name = listing.find("div", {"class": "fb4nyux atm_da_cbdd7d s1cjsi4j atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_kb7nvz atm_7l_12u4tyr atm_ks_zryt35__1rgatj2 dir dir-ltr"}).string
#         price = listing.find("span", {"class": "a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_mk_stnw88 atm_vv_1q9ccgz atm_vy_t94yts dir dir-ltr"}).string
#         name_list.append(name)
#         price_list.append(price)
#         #get name and price and append to name_list and price_list
#         href = a_tag['href']
#         #get link to listing details
#         print(href)
#         url_two = "https://www.airbnb.com/" + href
#         driver = webdriver.Chrome()
#         driver.get(url_two)
#         #initialize selenium driver and get listing details
#         try:
#             partial_text = "Show all"
#             wait = WebDriverWait(driver, 300)
#             button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{partial_text}')]")))
#             #wait until specific button is on page then store button in button then click
#             button.click()
#             element_locator = (By.XPATH, "//div[@class='twad414 atm_7l_18pqv07 atm_9j_1kw7nm4 atm_bx_1ltc5j7 atm_c8_8ycq01 atm_g3_adnk3f atm_fr_rvubnj dir dir-ltr']")
#             amenities= wait.until(EC.presence_of_all_elements_located(element_locator))
#             #wait until div with class is on page then store div with class in amenities
#             for a in amenities:
#                 amts_list.append(a.text)
#                 #store text of each amenities in amts_list
#             amn_list.append(amts_list)
#             #store each amts_list in amn_list
#             driver.back()
            
#             lists = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
#             for li in lists[:4]:
#                 dim_list.append(li.text)
#                 #store text of each dimension in dim_list
#             dimen_list.append(dim_list)
#             #store each dim_list in dimen_list
#         finally:
#             driver.close()
#             #close page
       
#     result_next = requests.get(current_url)
#     soup = BeautifulSoup(result_next.text, 'html.parser')
#     next_button = soup.find('a', {'aria-label': 'Next'})
#     print(next_button)
#     #get next button to go to next page
#     first_href = next_button.get('href')
#     current_url = "https://www.airbnb.com/" + first_href

# # print(name_list)

# # Output["name"] = name_list
# # Output["price"] = price_list
# # Output["dimension"] = dimen_list
# # Output["amenities"] = amn_list

# df = pd.DataFrame(Output)
# df.to_csv('beautifulsoup.csv')
# print(df)


df = pd.read_csv('beautifulsoup.csv')
# print(df)


def replace_string_with_nan(row):
    my_list = ast.literal_eval(row)
    for i in range(len(my_list)):
        if my_list[i] == "":
            my_list[i] = np.nan
    return my_list
df['amenities']= df['amenities'].apply(replace_string_with_nan)
# applies formula to each row of a column

df.to_csv('beautifulsoup.csv', index=False)


