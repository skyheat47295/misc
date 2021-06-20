import requests
import numpy as np
import pandas as pd
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
#print(len(r.json()['data']))
answer = 0
for x in range(1,len(r.json()['data'].split(',')),2):
    if int((r.json()['data'].split(',')[x][5:])) >= 50:
      answer += 1
print(f'Answer = {answer}')