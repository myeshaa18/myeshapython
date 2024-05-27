def make_shirt():
    size = input("Enter the shirt size (e.g., Small, Medium, Large): ")
    message = input("Enter the message for the shirt: ")
    if size.lower() not in ["small", "medium", "large"]:
        print("Invalid shirt size. Defaulting to Large.")
    if not message:
        message = "I love Python"
    print(f"Shirt size: {size}, Message: {message}")
# Create a large shirt with the default message
make_shirt()
# Create a medium shirt with the default message
make_shirt()
# Create a custom-sized shirt with a different message
make_shirt()
