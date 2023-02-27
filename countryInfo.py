
from countryinfo import CountryInfo


selectCountry = input("Enter the name of your country: ")

country = CountryInfo(selectCountry)


cap = country.capital()
pop = country.population()
cur = country.currencies()

print("Capital: ", cap)
print("Population: ", pop)
print("Country Currency: ", cur)




