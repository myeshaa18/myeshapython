# Create a list of people to invite to dinner
guests = ["Aima", "Mohid", "Najam"]
# Print an invitation message to each person
print("Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for a delightful evening!")
# Print a message about the limited space
print("\nI'm sorry, but we can only invite two people for dinner.")
# Remove guests one at a time until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner this time.")
# Print a message to the two remaining guests
print("\nYou are still invited to dinner:")
for guest in guests:
    print(f"Dear {guest}, you are still invited. Please join us!")
# Clear the list using del
del guests[:]
# Print the empty list to confirm
print("\nList of guests after clearing:", guests)