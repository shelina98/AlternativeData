import pandas as pd

companies = pd.read_csv('companies_sample.csv', na_values='n/a')

df2 = companies[(companies['country'] == 'United Kingdom')]

df2.to_csv('companiesUK.csv')

companies.info()
