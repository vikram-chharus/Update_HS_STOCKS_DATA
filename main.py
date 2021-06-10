#import the libraries 

import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

#read data from the csv and json files

hs_data = pd.read_json(r'loc\all_stock.json')
fdata = pd.read_csv(r'loc\filtered_Data.csv')

#add required columns

hs_data['Sector'] = np.nan
hs_data['Industry'] = np.nan

#method to find a match between csv and json file and update the json file

def findMatch(hs_data, fdata, company_name):
    company = company_name
    found = False
    last_word = ""
    while not found:
        data = fdata[fdata["CompanyName"].str.match(company) == True] 
        if not data.empty:
            d = hs_data[hs_data.name_of_company == company_name]
            d.iloc[0,4] = data.Sector
            d.iloc[0,5] = data.Industry
            hs_data[hs_data.name_of_company == company_name] = d
            found = True
        else:
            last_word = company
            company = company.rsplit(' ', 1)[0]
            if company == last_word:
                found = True

#Iterate through the company names and update the required columns if possibe otherwise skip

for company in hs_data.name_of_company:
    try:
        findMatch(hs_data, fdata, company)
    except:
        pass

#checking top 5 rows of the hs data

hs_data.head()
