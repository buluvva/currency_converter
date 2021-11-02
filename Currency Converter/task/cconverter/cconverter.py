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
            print(cache[f'{out_value}']['rate'])
        else:
            print("cache fail")
            #cache.update[f'{out_value}']['rate']
            print(data[f'{out_value}']['rate'])

in_value = input()

convert(in_value)
