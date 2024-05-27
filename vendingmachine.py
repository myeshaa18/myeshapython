def process_payment(products_selected):
    total_price = sum(products_selected.values())
    print("Selected Products:")
    for code, price in products_selected.items():
        product_name, _ = products.get(code)
        print(f"{product_name}: ${price}")
    print(f"Total Price: ${total_price}")

    payment_method = input("Choose payment method (cash/credit): ").lower()

    if payment_method == "cash":
        inserted_money = float(input("Insert money: $"))
        if inserted_money == total_price:
            print("Money inserted is correct. Products will be dispensed shortly!")
        elif inserted_money < total_price:
            print("Money inserted is not enough!")
        else:
            change = inserted_money - total_price
            print(f"Money inserted is more than enough! Products and change (${change:.2f}) will be dispensed shortly!")
    elif payment_method == "credit":
        credit_card_number = input("Enter credit card number: ")
        print(f"Payment successful with credit card ending in {credit_card_number[-4:]}. Products will be dispensed shortly!")
    else:
        print("Invalid payment method. Please choose 'cash' or 'credit'.")

print("Welcome to X's vending machine\n")
print("Product Price Code")
products = {
    1111: ("KitKat", 2),
    2222: ("Coke", 3),
    3333: ("Sprite", 3),
    4444: ("Tea", 1),
    5555: ("Coffee", 1),
    1234: ("Sneakers", 2),
    2345: ("Lays", 2),
    3456: ("Milk", 3),
    4567: ("Fanta", 3),
    5678: ("Pepsi", 3)
}

selected_products = {}

while True:
    for code, (product, price) in products.items():
        print(f"{product:<8} ${price:<3} {code}")

    # Step-2: ask the user to type a code
    print("Type a product code to add to cart or 'x' to proceed to payment or 'q' to quit:")
    user_input = input()

    if user_input.lower() == 'q':
        break
    elif user_input.lower() == 'x':
        if not selected_products:
            print("Your cart is empty. Please select some products first.")
            continue
        else:
            process_payment(selected_products)
            break

    try:
        user_code = int(user_input)
        selected_product = products.get(user_code)
        if selected_product:
            product_name, product_price = selected_product
            selected_products[user_code] = product_price
            print(f"{product_name} added to cart.")
        else:
            print("You have entered an invalid code")
    except ValueError:
        print("Invalid input. Please enter a valid product code or 'q' to quit.")