bd = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]        #set the board as a list


def print_bd():
    print(bd[0] + " | " + bd[1] + " | " + bd[2])
    print(bd[3] + " | " + bd[4] + " | " + bd[5])     #define a func() to print the game board
    print(bd[6] + " | " + bd[7] + " | " + bd[8])


def take_turn(player):
    print(player + " s turn :- ")
    post = input("Choose A Position From 1-9 :-")                             #define a func() to handle players turn
    while post not in ["1","2","3","4","5","6","7","8","9"]:
        post = input("Invalid Position. Choose Position From 1-9 :-")
    post = int(post)-1
    while bd[post] != "-":
        post = int(input("Position Already Choose By The Player. Choose A Different Position :-"))-1
    bd[post] = player
    print_bd()


def end_game():
    if (bd[0] == bd[1] == bd[2] != "-") or \
    (bd[3] == bd[4] == bd[5] != "-") or \
    (bd[6] == bd[7] == bd[8] != "-") or \
    (bd[0] == bd[3] == bd[6] != "-") or \
    (bd[1] == bd[4] == bd[7] != "-") or \
    (bd[2] == bd[5] == bd[8] != "-") or \
    (bd[0] == bd[4] == bd[8] != "-") or \
    (bd[2] == bd[4] == bd[6] != "-"):
        return "win"                                   #check for winning the game 
    elif "-" not in bd:
        return "tie"                                   #check for tie of the game 
    else: 
        return "play"                                  #check  for the game is not over


def play_game():
    print_bd()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = end_game()
        if game_result == "win":
            print(current_player +  "  Win The Match!!")                  #define the main game position
            game_over = True
        elif game_result == "tie":
            print("The Match Is Tie!!1")
            game_over = True

        else:

                  current_player = "0"  if current_player == "X" else "X"                    #switch to the other player


play_game()                          #start the game   
