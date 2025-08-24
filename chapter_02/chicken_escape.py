# Chicken Escape Adventure Game
import os

# Function to clear the terminal screen
def clear_screen():
    # Check if running on Windows or Unix-based system
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Function to ask if the player wants to play again
def play_again():
    clear_screen()
    print("Thanks for playing Chicken Escape!")
    print("Would you like to play again? (1 for Yes, 2 for No)")
    play_again_choice = input("\nEnter your choice (1-2): ")
    
    clear_screen()
    if play_again_choice == "1":
        print("Clucky's ready for another wild escape!")
        print("Is Clucky feeling extra feathery today? (1 for Yes, 2 for No)")
        feather_choice = input("\nEnter your choice (1-2): ")
        clear_screen()
        if feather_choice == "1":
            print("Feathers fluffed, Clucky restarts the adventure!")
            return True
        else:
            print("Clucky's still game, even without extra fluff!")
            return True
    elif play_again_choice == "2":
        print("Clucky retires to peck at corn in peace. Goodbye!")
        return False
    else:
        print("Invalid choice! Clucky assumes you're done.")
        input("\nPress Enter to continue...")
        return False

clear_screen()
print("Welcome to Chicken Escape! Help Clucky escape the farm.")
print("Choose options 1, 2, 3, or 4 to guide Clucky's adventure.")
print("One wrong move, and Clucky might meet a grim fate!\n")
input("Press Enter to start...")

# Main game loop
while True:
    game_over = False
    clear_screen()
    # Scenario 1: The Barnyard Dash
    print("Clucky is in the barnyard, eyeing the open gate.")
    print("1. Strut boldly through the gate, tail feathers high.")
    print("2. Hide in a haystack and wait for nightfall.")
    print("3. Challenge the guard dog to a staring contest.")
    print("4. Dig under the fence with a stolen spoon.")
    
    choice = input("\nEnter your choice (1-4): ")
    
    clear_screen()
    if choice == "1":
        print("Clucky struts out, but the farmer spots her! Dies of Dysentery!")
        game_over = True
    elif choice == "2":
        print("Clucky suffocates in the haystack. Dies of Dysentery!")
        game_over = True
    elif choice == "3":
        print("Clucky stares down the dog, who whimpers and flees. Success!")
    elif choice == "4":
        print("Clucky's spoon breaks, trapping her. Dies of Dysentery!")
        game_over = True
    else:
        print("Invalid choice! Pick 1, 2, 3, or 4.")
        input("\nPress Enter to try again...")
        continue
    
    if game_over:
        input("\nPress Enter to continue...")
    elif choice == "3":
        input("\nPress Enter to continue...")
        clear_screen()
        # Scenario 2: The Cornfield Maze
        print("Clucky reaches a cornfield maze under moonlight.")
        print("1. Sing a chicken lullaby to charm the crows for directions.")
        print("2. Sprint straight through, trusting chicken instincts.")
        print("3. Peck at corn kernels to bribe a field mouse for help.")
        print("4. Flap over the maze for a bird's-eye view.")
        
        choice = input("\nEnter your choice (1-4): ")
        
        clear_screen()
        if choice == "1":
            print("The crows love Clucky's song and guide her out. Success!")
        elif choice == "2":
            print("Clucky gets lost forever. Dies of Dysentery!")
            game_over = True
        elif choice == "3":
            print("The mouse steals the corn and runs. Dies of Dysentery!")
            game_over = True
        elif choice == "4":
            print("Clucky's wings fail, crashing into corn. Dies of Dysentery!")
            game_over = True
        else:
            print("Invalid choice! Pick 1, 2, 3, or 4.")
            input("\nPress Enter to try again...")
            continue
        
        if game_over:
            input("\nPress Enter to continue...")
        elif choice == "1":
            input("\nPress Enter to continue...")
            clear_screen()
            # Scenario 3: The Farmer's Picnic
            print("Clucky stumbles upon a farmer's picnic with a buffet of scraps.")
            print("1. Disguise as a picnic guest by wearing a tiny straw hat.")
            print("2. Steal a sandwich and run for it.")
            print("3. Cluck loudly to start a chicken conga line distraction.")
            print("4. Hide under the picnic table until everyone leaves.")
            
            choice = input("\nEnter your choice (1-4): ")
            
            clear_screen()
            if choice == "1":
                print("Clucky dons a tiny straw hat. The farmers are amused, but...")
                print("Does Clucky cluck politely (1) or squawk rudely (2)?")
                hat_choice = input("\nEnter your choice (1-2): ")
                clear_screen()
                if hat_choice == "1":
                    print("Clucky's polite cluck wins the farmers' hearts. She sneaks away!")
                else:
                    print("Clucky's rude squawk angers the farmers. Dies of Dysentery!")
                    game_over = True
            elif choice == "2":
                print("Clucky grabs the sandwich, but the farmers chase her. Dies of Dysentery!")
                game_over = True
            elif choice == "3":
                print("The conga line fails; the farmers catch Clucky. Dies of Dysentery!")
                game_over = True
            elif choice == "4":
                print("Clucky gets stepped on under the table. Dies of Dysentery!")
                game_over = True
            else:
                print("Invalid choice! Pick 1, 2, 3, or 4.")
                input("\nPress Enter to try again...")
                continue
            
            if game_over:
                input("\nPress Enter to continue...")
            elif choice == "1" and hat_choice == "1":
                input("\nPress Enter to continue...")
                clear_screen()
                # Scenario 4: The Road to Freedom
                print("Clucky sees the road beyond the farm, freedom so close!")
                print("1. Disguise as a tumbleweed with stray feathers.")
                print("2. Hitch a ride in a farmer's truck bed.")
                print("3. Sprint across the road in a wild chicken dash.")
                print("4. Wait for a parade to blend into the chaos.")
                
                choice = input("\nEnter your choice (1-4): ")
                
                clear_screen()
                if choice == "1":
                    print("Clucky rolls across as a tumbleweed, fooling everyone!")
                    print("\nClucky escapes the farm and crosses the road!")
                    print("But... a car zooms by! Clucky is hit. Game Over!")
                    game_over = True
                elif choice == "2":
                    print("The farmer spots Clucky in the truck. Dies of Dysentery!")
                    game_over = True
                elif choice == "3":
                    print("Clucky's dash is too slow. Dies of Dysentery!")
                    game_over = True
                elif choice == "4":
                    print("No parade comes. Clucky waits forever. Dies of Dysentery!")
                    game_over = True
                else:
                    print("Invalid choice! Pick 1, 2, 3, or 4.")
                    input("\nPress Enter to try again...")
                    continue
                
                input("\nPress Enter to continue...")
    
    # Check if player wants to play again
    if not play_again():
        break