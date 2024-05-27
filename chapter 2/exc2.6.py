# Original list of people to invite to dinner
guest_list = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci", "Isaac Newton"]

# Print invitation messages to each person
for guest in guest_list:
    print("Dear", guest + ",")
    print("You are cordially invited to dinner at my place.")
    print("I look forward to your presence!\n")

# Print a message saying only two people can be invited
print("Sorry, I can only invite two people for dinner.\n")

# Use pop() to remove guests from the list until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print("Sorry", removed_guest + ", I can't invite you to dinner.")

# Print invitation messages to each person remaining in the list
for guest in guest_list:
    print("Dear", guest + ",")
    print("You are still cordially invited to dinner at my place.")
    print("I look forward to your presence!\n")

# Use del to remove the last two names from the list
del guest_list[:]
print("Guest list after removing all guests:", guest_list) 