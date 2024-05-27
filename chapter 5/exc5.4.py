rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}
# Use a loop to print a sentence about each river
for river, country in rivers.items():
    print(f'The {river} runs through {country}.')
# Use a loop to print the name of each river
print("\nList of rivers:")
for river in rivers.keys():
    print(river)
# Use a loop to print the name of each country
print("\nList of countries:")
for country in rivers.values():
    print(country)