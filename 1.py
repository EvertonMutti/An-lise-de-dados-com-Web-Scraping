# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:58:21 2022

@author: Everton SSD
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
sUrl = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
response = requests.get(sUrl)
response = requests.get(sUrl, headers=headers)
html = BeautifulSoup(response.content, 'html.parser')
html = BeautifulSoup(html.prettify(), 'html.parser')
tabela = html.find(name='table')
df_tabela = pd.read_html(str(tabela))[0]
df_tabela = df_tabela.drop(columns=['Posição','Código do IBGE'])
print(df_tabela)