import pandas as pd
import matplotlib.pyplot as plt

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

<<<<<<< HEAD
print("Bar Chart: Which Countries have the maximum number of total vaccinations?")
vaccinations_by_country = data.groupby(['country']).max()["total_vaccinations"]
vaccinations_by_country = vaccinations_by_country.sort_values(ascending=False)[:10]
print(vaccinations_by_country)
vaccinations_by_country.plot.bar(title = "Countries vs Total Vaccinations (Top 10)")
plt.show()

=======
>>>>>>> 06dfd454d143c9de3603f1a7e9280fc704e56d36
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
<<<<<<< HEAD




=======
>>>>>>> 06dfd454d143c9de3603f1a7e9280fc704e56d36
