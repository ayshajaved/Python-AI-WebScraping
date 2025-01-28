import os
from bs4 import BeautifulSoup
import pandas as pd
class CollectingData():
    def __init__(self):
        #Data of laptops to be read from html and stored in a dictionary to make dataframe by pandas
        self.data = {
            'Title' : [],
            'Link' :[],
            'Price' : []
        }
        self.read_data()
    def read_data(self):
        #Reading the html file
        for i in range(1,len(os.listdir("Data"))+1):
            file = open(f"Data/laptop_{i}.html", "r", encoding="utf-8")

            #Parsing the html file
            self.soup = BeautifulSoup(file, 'html.parser')
            
            # print(self.soup.prettify())
            
            #Collecting the data from the html file
            # Collecting the title
            title_div = self.soup.find('div', class_="RfADt")
            if title_div and title_div.a:
                title = title_div.a.get('title', '').strip()
                self.data['Title'].append(title)
            else:
                self.data['Title'].append(None)  # Append None if title is missing

            # Collecting the link and removing ".html"
            link_tag = title_div.a if title_div and title_div.a else None
            if link_tag:
                link = link_tag.get('href', '').strip()
                self.data['Link'].append(f"https:{link}")
            else:
                self.data['Link'].append(None)

            # Collecting the price
            price_div = self.soup.find('div', class_="aBrP0")
            if price_div:
                price = price_div.text.strip()
                self.data['Price'].append(price)
            else:
                self.data['Price'].append(None)
   
        
        self.create_dataframe()
    def create_dataframe(self):
        #Creating a dataframe from the data collected
        self.df = pd.DataFrame(self.data)
        self.df.to_csv('DarazLaptops.csv', index=False)

c = CollectingData()

            


        
