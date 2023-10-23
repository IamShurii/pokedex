import random
import json , requests


pokename = input("digite o nome do pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokename}"
requi = requests.get(url)

if requi.status_code == 200:
    pok = requi.json()
    
    print(f"nome: {pok['name']}")
    print(f"altura: {float(pok['height'])/ 3.281:.2f}")
    print(f"Hp: {pok['stats'][0]['base_stat']}")
    print(f"Atq: {pok['stats'][1]['base_stat']}")
else:
    print(f"Pokemon n econtrado")