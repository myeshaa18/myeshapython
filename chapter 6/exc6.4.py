sandwich_orders = ['tuna', 'turkey', 'club', 'vegetarian']
# Create an empty list for finished sandwiches
finished_sandwiches = []
# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list  
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)