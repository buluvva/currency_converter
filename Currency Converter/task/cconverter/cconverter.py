import json
import requests

data = dict()
cache = dict()
url = f'http://www.floatrates.com/daily/'

def convert(in_value):

    out_value = input()
    amount = int(input())
    r = requests.get(f'{url}{in_value}.json')
    data = r.json()
    if f'{in_value}' in cache.values():
       print(int(cache[f'{out_value}']['rate'])*amount)
    else:
        print("cache fail")
        #cache.update[f'{out_value}']['rate']
        result = float(data[f'{out_value}']['rate'])*amount
        print(f'{result} {out_value}')

in_value = input()

convert(in_value)
