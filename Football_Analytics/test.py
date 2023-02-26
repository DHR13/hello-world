# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:01:50 2022

@author: danie
"""

import pandas as pd

gameweek = [gw for gw in range(1, 39)]
csv_url = 'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/'    
dfs = []

for gw in gameweek:
   dfs1 = []     
   gw_url = csv_url+f"gw{gw}.csv"
   for p in gameweek:
       url = gw_url
       print(url)
       df = pd.read_csv(url)
       dfs1.append(df)
   dfs.append(pd.concat(dfs1).drop_duplicates()) 
#removed axis=1 as it duplicated columns
#added drop_duplicate to remove duplicate rows
result_pm10 = pd.concat(dfs, keys=gameweek)
                #.rename_axis(('location','data'))
                #.dropna(axis=1, how='all')
                #.reset_index()
print (result_pm10)
result_pm10.to_csv(r"D:\Programming\Python\Output\FPL\all_gw_export_data.csv", index = False, header=True)