print("You wake up at the mouth of a dark cavern.")
print("It is night time and the stars are twinkling in the sky overhead.\n")

print("You know that there is a trail that leads down into the forest")
print("where your camp is waiting.\n")

print("Should you follow the trail into the forest,")
print("or should you stay in the cave during the night?\n")

print("\t1. Follow the trail into the forest")
print("\t2. Stay in the cave until morning")

choice = input("\nWhat is your choice? (1 or 2) ")

if choice == "1":
    print("\nYou carefully step onto the dark trail.")
    print("Suddenly your foot catches on a root!")
    print("You trip and fall hard.\n")
    print("\"Ouch!\" you cry out.")
    print("You have hurt your knee.")
    
    pain = float(input("\nHow much does your knee hurt? (example: 6.5) "))
    print(f"\nYour knee is throbbing at a pain level of {pain}.")
    print("This is going to make the rest of the night difficult...")

elif choice == "2":
    print("\nYou decide it is safer to stay in the cave.")
    print("You curl up against the cool stone wall and close your eyes.\n")
    print("Hours pass...")
    print("The first light of dawn begins to paint the sky.")
    print("You wake up feeling refreshed and strong.")
    
    energy = float(input("\nHow rested do you feel now? (example: 9.2) "))
    print(f"\nYour energy level is {energy} out of 10.")
    print("Now that it is light, you can clearly see the trail")
    print("leading safely down into the forest toward camp.")

else:
    print("\nThat was not one of the choices.")
    print("The night grows colder as you stand undecided...")

"""
What the student practices without noticing:
Escape characters: \n for spacing and dramatic pauses, \t for a clean numbered menu, \" for the spoken “Ouch!”
input(): Asking for the choice and later for a pain or energy number
Strings: All the story text and the player’s choice
Integers (as strings first): The menu options 1 and 2
Floats: Pain level or energy level so they get comfortable typing decimal numbers
The story stays short and atmospheric, so it still feels like a tiny adventure instead of a programming exercise. Students usually enjoy changing the dialogue, adding their own sound effects with extra \n, or inventing a third choice once they see how the if/elif works.
"""

# LogosTeach 2026 All rights reserved