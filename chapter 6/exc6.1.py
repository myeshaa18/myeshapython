while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    
    print(f"You'll add {topping} to your pizza.")

print("Pizza order completed!")