guests = ["Mohid","sam","Aima","Najam"]
print("Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for evening!")
guest_cant_make_it = guests.pop(1)
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")
new_guest = "Sam"
guests.append(new_guest)
print("Updated Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for evening!")