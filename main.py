import pandas as pd
import requests
import json
from tqdm import tqdm



cidades = [
    'São Paulo' , 'New York' , 'London' , 'Madrid' , 'Berlim' , 'Moscou' , 'Oslo'
]

planilha = {
    "Cidade": [],
    "Temperatura": [],
    "Sensação_térmica": [],
    "Máxima": [],
    "Mínima": []
}


for cidade in tqdm(cidades , colour='green'):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    dados = requests.get(url).json()
    # dados = dados.json()
    planilha["Cidade"].append(dados["name"])
    planilha["Temperatura"].append(dados["main"]["temp"])
    planilha["Sensação_térmica"].append(dados["main"]["feels_like"])
    planilha["Máxima"].append(dados["main"]["temp_max"])
    planilha["Mínima"].append(dados["main"]["temp_min"])

# print(planilha["Temperatura"])

df = pd.DataFrame(planilha)

df.to_excel('planilha.xlsx')
    
    