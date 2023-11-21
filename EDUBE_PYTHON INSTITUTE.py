from random import randrange

def draw_move(board):
    free_fields=make_list_of_free_fields(board)
    cpu_move=free_fields[(randrange(len(free_fields)))]
    row, col=cpu_move
    board[row][col]="X"
    print("I went. Your Turn")
    return(board)


board=[["1","2","3"],["4","5","6"],["7","8","9"]]


move_dict={
    "1":(0,0),
    "2":(0,1),
    "3":(0,2),
    "4":(1,0),
    "5":(1,1),
    "6":(1,2),
    "7":(2,0),
    "8":(2,1),
    "9":(2,2)
}
winning_positions=[(1,2,3),
                    (4,5,6),
                    (7,8,9),
                    (1,4,7),
                    (2,5,8),
                    (3,6,9),
                    (1,5,9),
                    (3,5,7)]

winning_positions = [[f"{num}" for num in pos] for pos in winning_positions]


def display_board(board):
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   {}  |   {}  |   {}  |".format(board[0][0],board[0][1],board[0][2]))
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   {}  |   {}  |   {}  |".format(board[1][0],board[1][1],board[1][2]))
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|   {}  |   {}  |   {}  |".format(board[2][0],board[2][1],board[2][2]))
    print("|      |      |      |")
    print("+------+------+------+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.



        
def enter_move(board):
    free_fields=make_list_of_free_fields(board)
    available_inputs=[str(i+1) for i in range(9)]
    user_move=input("Enter Your Move, what space do you want to go to:")
    if user_move in available_inputs:
        row, col=move_dict[user_move]
        if move_dict[user_move] in free_fields:
            board[row][col]="O"
        else:
            print("That space was occupied. Please try again")
            enter_move(board)
        return(board)
    else:
        print("Invalid input. Please try again.")
        enter_move(board)
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.




def make_list_of_free_fields(board):
    free_fields=[]
    for i in range(9):
        if board[i//3][i%3]=="O":
            continue
        elif board[i//3][i%3]=="X":
            continue
        else:
            location=((i//3),(i%3))
            free_fields.append(location)
    return free_fields
    
    #The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


winning_positions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
winning_positions = [[f"{num}" for num in pos] for pos in winning_positions]

def victory_for(board, sign):
    global keepPlaying
    filled_spot=[]
    for i in range (9):
        if board[i//3][i%3]==sign:
            filled_spot.append(str(i+1))
          
    for wins in winning_positions:
        if all(i in filled_spot for i in wins): 
            print("There's a Winner")
            keepPlaying="STOP"
            return keepPlaying
    return keepPlaying                    

            
free_fields=make_list_of_free_fields(board)

keepPlaying="Yes"
draw_move(board)
display_board(board)
while ((len(free_fields))>0):
    make_list_of_free_fields(board)
    enter_move(board)
    victory_for(board,"O")
    if keepPlaying=="STOP":
        print("Human Wins!")
        break
    make_list_of_free_fields(board)
    display_board(board)
    draw_move(board)
    victory_for(board,"X")
    display_board(board)
    if keepPlaying=="STOP":
        print("Computer Wins!")
        break
    free_fields=make_list_of_free_fields(board)
else:
    print("Cat's Game. Meow!!")

display_board(board)
print("That' all folks! Thanks for playing!")



