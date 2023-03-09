import requests
import pandas
result = requests.get('https://api.chucknorris.io/jokes/random')
print(result.text)

df = pandas.DataFrame()
print(df)
