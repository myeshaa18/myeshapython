pets = [
    {
        'kind': 'Dog',
        'owner': 'Alice'
    },
    {
        'kind': 'Cat',
        'owner': 'Bob'
    },
    {
        'kind': 'Parrot',
        'owner': 'Charlie'
    }
]
# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  # Blank line to separate pet information