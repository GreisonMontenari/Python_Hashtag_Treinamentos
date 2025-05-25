import os
import time
import requests
from datetime import datetime
from random import uniform

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json'

for _ in range(10):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data_json = response.json()
        taxa = float(data_json[0]['valor'].replace(',', '.'))
    except Exception as e:
        print(f"Erro ao obter a taxa CDI: {e}")
        taxa = None

    if taxa is not None:
        data_e_hora = datetime.now()
        data = data_e_hora.strftime('%Y-%m-%d')
        hora = data_e_hora.strftime('%H:%M:%S')

        if not os.path.exists('taxa-cdi.csv'):
            with open('taxa-cdi.csv', 'w') as f:
                f.write('data,hora,taxa\n')

        with open('taxa-cdi.csv', 'a') as f:
            f.write(f'{data},{hora},{taxa}\n')

        print(f"Registro adicionado: {data} {hora} - {taxa}")
    time.sleep(uniform(1.5, 2.5))
