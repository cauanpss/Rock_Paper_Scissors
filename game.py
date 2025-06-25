import random

moves = {0:"rock",
         1:"paper",
         2:"scissor"}



def user_move():
    while True:
        try:
            play = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.").strip())
            if play in moves:    
                return play 
            else: 
                print(f"Please enter 0, 1, or 2.")
        
        except ValueError:
            print(f"Invalid input. Please enter a number (0, 1, or 2).")

def pc_move():
    pc_play = random.choice(list(moves.keys()))
    return pc_play

def winner(user, pc):
    if user == pc:
        return f"Draw!"
    
    elif (pc == 2 and user == 1) or (pc ==1 and user == 0) or (pc == 0 and user == 2 ):
        return f"Pc Wins!"
    
    else:
        return f"User wins!"

def new_game():
    while True:
            keep_playing = input(f"Do you want to continue playing? [y/n] ").strip().lower()
            
            if keep_playing == 'y':
                return True
            
            elif keep_playing == 'n':
                 return False
            
            else:
                print(f"Insert a valid character.")

def run_game():
    print(f"Welcome to the Rock, Scissor Paper game!")
    playing = True
    while playing:
        pc = pc_move()
        user = user_move()
        print(f"You choose {moves[user]}!")
        print(f"Pc choose {moves[pc]}")
        print(f"{winner(user, pc)}")
        playing = new_game()
        
run_game()





