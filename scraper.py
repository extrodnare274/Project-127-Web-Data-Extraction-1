from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL) 

scraped_data =[] 

def scrape():
    for i in range(0,10):
        print(f'Scrapping page {i+1}...')

        soup = BeautifulSoup(browser.page_source, "html_parser")

        for ul_tag in soup.find_all("ul", attrs={"class", "stars"}):
            li_tags = ul_tag.find_all("li")

            temp_list =[]

            for index, li_tag in enumerate(li_tags):

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            scraped_data.append(temp_list)

        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

scrape()

headers = ["star_name","distance", "mass","radius","luminosity"]

stars_df_1= pd.DataFrame(scraped_data, columns=headers)

stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")