def make_shirt(size):
    message = input("Enter the message for the shirt: ")
    print(f"Shirt size: {size}, Message: {message}")
# Call the function using positional arguments to specify the size
size1 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
make_shirt(size1)
# Call the function using keyword arguments to specify the size and message
size2 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
message2 = input("Enter the message for the shirt: ")
make_shirt(size=size2, message=message2)