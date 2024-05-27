while True:
    age_str = input("Please enter your age (or 'quit' to exit): ")
    if age_str.lower() == 'quit':
        break
    try:
        age = int(age_str)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"Your movie ticket will cost ${ticket_price}.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")
print("Thank you for using the ticket pricing system!")