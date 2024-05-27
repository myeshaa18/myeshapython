person_info = {
    'first_name': str(input("Enter your first name ")),
    'last_name': str(input("Enter your last name ")),
    'age': int(input("Enter your age ")),
    'city': str(input("Where do you live "))
}
# Print each piece of information stored in the dictionary
print("First Name:", person_info['first_name'])
print("Last Name:", person_info['last_name'])
print("Age:", person_info['age'])
print("City:", person_info['city'])