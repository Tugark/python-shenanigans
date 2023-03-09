import requests
import pandas
result = requests.get('https://api.chucknorris.io/jokes/random')
result.text

df = pandas.DataFrame()
df
