alien_color = str(input("Enter the color of the alien "))
if alien_color == 'green':
    print("Player earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player earned 10 points for shooting the yellow alien.")
elif alien_color == 'red':
    print("Player earned 15 points for shooting the red alien.")
else:
    print("Player earned 0 points. Invalid alien color.")