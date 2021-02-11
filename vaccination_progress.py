import pandas as pd

data = pd.read_csv('country_vaccinations.csv')

pd.set_option('max_columns', None)
print("Data Sample: ", data.head(5))
print("\n(Rows, Columns): ", data.shape) #-- (2555,15)
print("\nColumn Names: ", data.columns)

print("Which country is using what vaccine?")
country_vaccine = data[['country', 'vaccines']]
country_vaccine = country_vaccine.drop_duplicates()
print(country_vaccine)

print("Most common vaccine")
vaccine_count = country_vaccine['vaccines'].value_counts()
#print(vaccine_count)
print(vaccine_count.idxmax())






'''

print("\n--- United States --- ")
us_data = data.loc[data['country'] == "United States"]
print("\nUnited States Data Info: ", us_data.shape)

print("\nVaccines used: ", us_data['vaccines'].unique())
'''