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

print("\n--- United States --- ")
us_data = data.loc[data['country'] == "United States"]
print("United States Data Info: ", us_data.shape)
print("Vaccines used: ", us_data['vaccines'].unique())

print("Line Chart: People Fully Vaccinated over time")
plt.figure(figsize=(10, 6))
plt.plot(us_data['date'], us_data['people_fully_vaccinated_per_hundred'], marker = 'o')
plt.xlabel("Date")
plt.ylabel('Number of people fully vaccinated per hundred\n (Ratio in percent between population fully immunized \nand total population up to the date in the country')
plt.title('People Fully Vaccinated over time')
plt.xticks(rotation=90)
plt.show()
