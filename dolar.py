#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

#%%
def carga():
    urlpage = "https://dolarhoy.com/"
    page = requests.get(urlpage)
    soup = BeautifulSoup(page.text, 'html.parser')
    valor = soup.find_all(class_="val")
    cotizaciones = {"blue_c":valor[0].text, "blue_v":valor[1].text, "ofi_c":valor[4].text, "ofi_v":valor[5].text, 
                    "mep_c":valor[6].text, "mep_v":valor[7].text, "ccl_c":valor[8].text, "ccl_v":valor[9].text, 
                    "cripto_c":valor[10].text, "cripto_v":valor[11].text}
    database = pd.DataFrame.from_dict(cotizaciones, orient ='index')
    database.columns =[datetime.now()]
    return(database)

#initial run to set up the pandas dataframe
data=carga()

#%%
#now, runing for multiple days
for i in range(50):
    #this is the number of seconds x day
    time.sleep(86400)
    data[datetime.now()] = carga()
    print(data)
    data.to_csv('data_test.csv')
