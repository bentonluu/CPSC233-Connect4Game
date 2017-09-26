import turtle
import random
import time


#Token constants
RED = 'R'
GREEN = 'G'
BLANK = 'B'

#Board constants
SIZEOFSQ = 50
PENSIZE = 2
COLUMN = 7
ROW = 6
ROW_COMBINATION_TWO = 3
HALF_BOARD_LENGTH = 175
SQ = 4
SPEED = 100

#Button constants
BUTTON_PENCOLOR = "orange"
BOARD_LENGTH = 350
SPACE_ABOVE_BOARD = 5
BUTTON_SIZE = 40
SPACE_BETWEEN_BUTTON = 50

#Text/Intro constants
TITLE_COLOR = "darkblue"
BUTTON_COLOR = "orange"
TEXT_COLOR = "purple"
SCREEN_FONT = "Arial"
BUTTON_FONT = "Arial"
MESSAGE_FONT = "Arial"
POSITON = "center"
MODE_BOLD = "bold"
MODE_NORMAL = "normal"
FSIZE_SCREEN = 40
FSIZE_BUTTON = 25
FSIZE_INFO = 13
FSIZE_MESSAGE = 16
TITLE_DIST = 235
COLUMN_NUM_HEIGHT = 187
COLUMN_NUM_CENTER = 157
SPACE_BETWEEN_BOARD_INFO = 240
SPACE_BETWEEN_TEXT = 20

#Winner message constants
FSIZE_WINNER = 18
GREEN_PLAYER = "lightgreen"
RED_PLAYER = "red"

#Message constants
MESSAGE_COLOR = "brown"
COLOR_SELECTED = "black"
STALEMATE_COLOR = "grey"
NEW_COLOR = "pink"
MESSAGE_DIST = 190
COLOR_DIST = 160
NEW_DIST = 215
WAIT_TIME = 2
EDGE_OF_TEXT = 500
ERASE_ALL_TEXT = 1000
ERASER = 40
ERASER_COLOR = "white"

#Keyboard fuctions infomation constants
KEYINFO_COLOR = "blue"
KEYTEXT_COLOR = "black"
KEY_FSIZE = 14
SPACE_BETWEEN_KEYINFO = 30
START_OF_BOX = 200
SIDE_OF_RECTANGLE  = 2
BOX_LENGTH = 125
BOX_WIDTH = 253
CENTER_BOX = 83

#Click constants
LEFTCLICKLIMIT = -170.0
RIGHTCLICKLIMIT = 172.0
BOTTOMCLICKLIMIT = -127.0
TOPCLICKLIMIT = 224.0

#Check win condition constant
COMBIN_HCHECK = 4

#Click constant
MOVE_TO_ZERO = 170

#This function draws the gameboard of Connect 4.
def draw_gameboard():

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Adjust pensize and speed of the pen.
    draw.pensize(PENSIZE)
    draw.speed(SPEED)

    #Initial placement of the pen to draw the gameboard (starts at the top
    #right corner of the gameboard).
    draw.up()
    draw.left(90)
    draw.forward(HALF_BOARD_LENGTH)
    draw.left(90)
    draw.forward(HALF_BOARD_LENGTH)
    draw.left(180)
    draw.down()

    #Draws the gameboard by first drawing a square then loops to generate
    #a row with the number of columns in the gameboard. The rows are drawn in
    #alternate directions, right then left. This is looped until the dimensions
    #of the Connect 4 gameboard, 7 columns and 6 rows, are created.
    for gameboard in range(ROW_COMBINATION_TWO):

        #Draws a row of the gameboard by looping the number of columns in the
        #gameboard (7) and is drawn going in the right direction.
        for gamerow in range(COLUMN):

            #Draws a square where a token will be placed.
            for sqaure in range(SQ):
                draw.forward(SIZEOFSQ)
                draw.right(90)

            #Allows the next square to be drawn to the right of the previous
            #square drawn.
            draw.forward(SIZEOFSQ)

        #Sets up the position of the pen in order to draw the next row below
        #the previous row which goes towards the left direction.
        draw.right(90)
        draw.forward(SIZEOFSQ)
        draw.right(90)

        #Draws a row of the gameboard by looping the number of columns of the
        #gameboard (7) and is drawn going in the left direction.
        for gamerow in range(COLUMN):

            #Draws a square where a token will be placed.
            for sqaure in range(SQ):
                draw.forward(SIZEOFSQ)
                draw.left(90)

            #Allows the next square to be drawn to the left of the previous
            #square drawn.
            draw.forward(SIZEOFSQ)

        #Sets up the position of the pen in order to draw the next row below
        #the previous row which goes towards the right direction.
        draw.left(90)
        draw.forward(SIZEOFSQ)
        draw.left(90)

#This function draws the buttons above the Connect 4 gameboard where a player
#clicks on it to play their token in the desired column.
def draw_button():

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Assigns the color for the buttons.
    draw.pencolor(BUTTON_PENCOLOR)

    #Initial placement of the pen to draw the buttons (above the gameboard).
    draw.up()
    draw.left(90)
    draw.forward(BOARD_LENGTH)
    draw.right(90)
    draw.forward(SPACE_ABOVE_BOARD)
    draw.down()

    #Draws a row of buttons (squares) that match the number of columns of the
    #gameboard (7) and each button is separated with space between them.
    for total_squares in range(COLUMN):

        #Draws a button.
        for square in range(SQ):
            draw.forward(BUTTON_SIZE)
            draw.right(90)

        #Spaces the button so that the next button is not directly beside the
        #previous button.
        draw.up()
        draw.forward(SPACE_BETWEEN_BUTTON)
        draw.down()

#This function writes the title of the game, the numbers in the buttons that
#correspond to the columns of the gameboard, and a information paragraph that
#informs the player about the general objectives/rules of the game.
def draw_intro():

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Initial placement of pen in order to write the title of the game (above
    #gameboard and buttons).
    draw.penup()
    draw.goto(0,0)
    draw.left(90)
    draw.forward(TITLE_DIST)

    #Assigns the color for the title of the game.
    draw.pencolor(TITLE_COLOR)

    #Write the title on the game on the screen.
    draw.write("Connect 4", align = POSITON, \
    font = (SCREEN_FONT, FSIZE_SCREEN, MODE_BOLD))

    #Initial placement of the pen in order to write the numbers in each of the
    #buttons that correspond to the column of the gameboard (above gameboard).
    draw.goto(0,0)
    draw.forward(COLUMN_NUM_HEIGHT)
    draw.left(90)
    draw.forward(COLUMN_NUM_CENTER)
    draw.left(180)

    #Assigns the color for the numbers in the buttons.
    draw.pencolor(BUTTON_COLOR)

    #Using an accumulation pattern, writes the numbers in each of the buttons.
    column_num = 0

    #Loops based on the number of columns in the game (7).
    for textcolumn in range(COLUMN):

        #Adds 1 to 'column_num' each time through the loop and writes that
        #number in the button.
        draw.write(str(column_num+1), font = (BUTTON_FONT, FSIZE_BUTTON, \
        MODE_BOLD))

        #Adds 1 to 'column_num' each time through the loop and updates it so
        #that is increments each time.
        column_num = column_num + 1

        #Space between the numbers.
        draw.forward(SIZEOFSQ)

    #Assigns the color for the information paragraph for Connect 4.
    draw.pencolor(TEXT_COLOR)

    #Initial placement of pen in order to write the information paragraph.
    draw.goto(0,0)
    draw.right(90)
    draw.forward(SPACE_BETWEEN_BOARD_INFO)
    draw.left(90)

    #The information paragraph that informs players about the objective of the
    #game, how to win and the result when the entire board is filled with
    #pieces.
    infostatement = ["~ The objective of the game is to have 4 of your",
    "pieces horizontally, vertically, or diagonally",
    "connected. In the case where there are no more ",
    "possible moves that can be made, (the entire board ",
    "is filled with pieces), the result will be a stalemate."]

    #Loops based on the number of sentences within the list 'infostatement'
    #and writes each sentences out, with space between each sentence.
    for infoparagraph in infostatement:

        #Writes the sentence in the list 'infostatement' at the current index
        #of the list.
        draw.write(infoparagraph, align = POSITON, font = (MESSAGE_FONT, \
        FSIZE_INFO, MODE_NORMAL))

        #Space between each of the sentences written out.
        draw.right(90)
        draw.forward(SPACE_BETWEEN_TEXT)
        draw.left(90)

#This function draws a box that contains information about the keyboard
#presses that correspond to different functions(saving, loading and new game)
def draw_keyinfo():

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Move turtle to the center of the screen.
    draw.goto(0,0)

    #Initial placement of the pen to draw the box that contains the keyboard
    #information (left of the gameboard).
    draw.left(90)
    draw.forward(HALF_BOARD_LENGTH)
    draw.left(90)
    draw.forward(START_OF_BOX)

    #Allows pen to draw and assigns color of the information box.
    draw.pendown()
    draw.pencolor(KEYINFO_COLOR)

    #Loops to draw the information box.
    for box in range(SIDE_OF_RECTANGLE):
        draw.forward(BOX_WIDTH)
        draw.right(90)
        draw.forward(BOX_LENGTH)
        draw.right(90)

    #Postions the pen to write out the keyboard information within the box.
    draw.penup()
    draw.forward(BOX_LENGTH)
    draw.right(90)
    draw.forward(CENTER_BOX)
    draw.right(90)

    #Assigns the color of the information text.
    draw.pencolor(KEYTEXT_COLOR)

    #The keyboard information paragraph that informs players about the
    #differnt key presses and the functions they perform.
    keyfunction = ["Press 'n' to start new game", "Press 's' to save the game",
    "Press 'l' to load the game"]

    #Loops based on the number of sentences within the list 'keyfunction'
    #and writes each sentences out, with space between each sentence.
    for keyinfo in keyfunction:

        #Writes the sentence in the list 'keyfunction' at the current index
        #of the list.
        draw.write(keyinfo, align = POSITON, \
        font = (MESSAGE_FONT, KEY_FSIZE, MODE_BOLD))

        #Space between each of the sentences written out.
        draw.right(90)
        draw.forward(SPACE_BETWEEN_KEYINFO)
        draw.left(90)

    #Stops the pen from drawing anymore.
    draw.penup()

#This function writes a message when the player or AI wins the game and also
#writes a message when there is a stalemate.
def draw_winner(winner):

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Move turtle to the center of the screen.
    draw.goto(0,0)

    #If the player or AI that is assigned the color green wins, it writes a
    #message that informs the player that the game is over and whoever is
    #assigned to the color green won.
    if winner == 1:

        #Initial placement of the pen to draw the buttons (below the gameboard).
        draw.right(90)
        draw.forward(MESSAGE_DIST)
        draw.left(90)

        #Allows pen to draw and assigns color for the pen.
        draw.pendown()
        draw.pencolor(GREEN_PLAYER)

        #Write a message that the game is over and that the green player won.
        draw.write("GAME OVER! Green Player Wins!", align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_WINNER, MODE_NORMAL))

        #Stops the pen from drawing anymore.
        draw.penup()

        #Writes a message that informs the player what to do next after someone
        #has won.
        newgame_message()

    #If the player or AI that is assigned the color red wins, it writes a
    #message that informs the player that the game is over and whoever is
    #assigned to the color red won.
    elif winner == 2:

        #Initial placement of the pen to draw the buttons (below the gameboard).
        draw.right(90)
        draw.forward(MESSAGE_DIST)
        draw.left(90)

        #Allows pen to draw and assigns color for the pen.
        draw.pendown()
        draw.pencolor(RED_PLAYER)

        #Write a message that the game is over and that the red player won.
        draw.write("GAME OVER! Red Player Wins!", align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_WINNER, MODE_NORMAL))

        #Stops the pen from drawing anymore.
        draw.penup()

        #Writes a message that informs the player what to do next after someone
        #has won.
        newgame_message()

    #If either the player or AI won the game, it results in a stalemate and it
    #will write a message that informs the player that it is a stalemate.
    elif winner == 3:

        #Initial placement of the pen to draw the buttons (below the gameboard).
        draw.right(90)
        draw.forward(MESSAGE_DIST)
        draw.left(90)

        #Allows pen to draw and assigns color for the pen.
        draw.pendown()
        draw.pencolor(STALEMATE_COLOR)

        #Write a message that the game is over and that it is a stalemate.
        draw.write("GAME OVER! Its a stalemate", align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_WINNER, MODE_NORMAL))

        #Stops the pen from drawing anymore.
        draw.penup()

        #Writes a message that informs the player what to do next after someone
        #has won.
        newgame_message()

#This function draws the AI and Player token moves
def draw_token(column,color,index):

    #Reference to the turtle named 'tokenmove'
    global tokenmove

    #Hides the turtle so it does not appear on the screen.
    tokenmove.hideturtle()

    #Move turtle to the center of the screen.
    tokenmove.home()

    #Changes the parameter of color to be used as a color for the turtle.
    if color == 'G':
        color = 'Green'
    elif color == 'R':
        color = 'Red'

    #Converts row and column into a interger.
    column = int(column)
    row = int(index)

    #defines the turtle shape as a size 2 circle.
    tokenmove.shape("circle")
    tokenmove.shapesize(2)
    tokenmove.speed(SPEED)

    #using the 'color' parameter, this determines the turtle color.
    tokenmove.color(color)

    #turns left 90 degrees and goes foward 3 boxes.
    tokenmove.penup()
    tokenmove.left(90)
    tokenmove.forward(SIZEOFSQ * 3)

    #turns left agian 90 degrees and goes forward 3 boxes it is now
    #sitting in the top left corner.
    tokenmove.left(90)
    tokenmove.forward(SIZEOFSQ * 3)


    tokenmove.right(180)

    #Turtle moves foward to the correct column, turns left and goes towards the
    #the correct row and stamps a colored circle.
    tokenmove.forward((column) * SIZEOFSQ)
    tokenmove.right(90)
    tokenmove.forward((row) * SIZEOFSQ)
    tokenmove.stamp()

#This function writes which color the player and AI are on the screen.
def draw_playercolor():

    #Reference to the color of the player and AI that are assigned for the
    #entire game.
    global color_player
    global color_ai

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Writes out the case when a player's color is green or when it is
    #red.
    if color_player == GREEN:
        screencolor = "Player Color: Green   /   AI Color: Red"
    else:
        screencolor = "Player Color: Red   /   AI Color: Green"

    #Assigns the color for the statement.
    draw.pencolor(COLOR_SELECTED)

    #Postions the pen to write out which color the player is assigned and which
    #color the AI is assigned.
    draw.goto(0,0)
    draw.right(90)
    draw.forward(COLOR_DIST)
    draw.left(90)

    #Writes which color the player is and which color the AI on the screen.
    draw.write(screencolor, align = POSITON, \
    font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

#This function creates the inital blank global gamestate used in the game. The
#global gamestate is created by making a list of 6 blanks which represent
#each row of a column and there are a total of 7 of these 'rowgamestate'
#representing each column in the game.
def creategamestate():

    #Empty list for a single column.
    rowgamestate = []

    #Empty list for the global gamestate.
    globalGamestate = []


    #Loops based on the number of rows in the game (6) and inserts "B" into the
    #list 'rowgamestate'.
    for gamerow in range(ROW):
        rowgamestate.append(BLANK)

    #Assigns a copy of 'rowgamestate' to 'clone' so that it does not reference
    #the same objects.
    clone = rowgamestate[:]

    #Loops based on the columns in the game (7), makes copies of 'clone' so
    #that it does not reference the same objects and inserts them in the list
    #'globalGamestate'.
    for gamecolumns in range(COLUMN):
        clone = clone[:]
        globalGamestate.append(clone)

    #Returns an emtry global gamestate of the game at the start of the game.
    return globalGamestate

#Randomly generates a number of either 1 or 2
def first_random():

    #Generates a random number of either 0 or 1
    number = random.randrange(0,2)

    return number

#This function determines the color of the player. Based on a randomly generated
#number.
def choose_color_player(number):

    #Generates a random number of either 0 or 1 and assigns it to "player"
    player = random.randrange(0,2)


    #If "player" was assigned to 0, the player is now assigned to the letter GREEN
    if number == 0:
        player = GREEN

    #If "player" was assigned to 1, the player is now assigned to the letter RED
    elif number == 1:
        player = RED

    #Returns player assigned to either GREEN or RED
    return player

#This function determines the color of the AI. Based on the "color_player"
#color_player is a global variable assigned to either RED or GREEN
def choose_color_ai():

    global color_ai

    #If color_player is GREEN, ai is now RED
    if color_player == GREEN:
        ai =RED

    #if color_player is RED, ai is now GREEN
    elif color_player == RED:
        ai = GREEN

    #returns AI assigned to either GREEN or RED
    return ai

#Green player goes first. If the AI was assigned to GREEN it will go first
def firstmove():

    global color_ai

    #If color_ai is assigned to GREEN, it will perform the first move by calling
    #the update_gamestateai function to perform a move.
    if color_ai == GREEN:

        #Updates the global gamestate with the AI move
        update_gamestateai()

#For Horizontal and Diagonal AI. Checks to see if it is a valid move. If there
#are BLANK spaces below where the AI wants to play, it will play there. If there
#are blank spaces it will continue on with the other AI functions
def valid_move(column, row):

    #Uses global gamestate list
    global globalGamestate

    gamestate = globalGamestate

    #with the parameter "column" it grabs a coloumn from the globalGamestate
    gamestate = gamestate[column]

    #Shortens the column to below the row on where the AI wants to play
    NewCol = gamestate[row:]

    #If a BLANK is found in the NewCol, the function will return as false and not play
    #that move. If no blank is found in the NewCoL, the function will return as True
    #and play that move
    if (BLANK) in NewCol:
        return False
    else:
        return True

#If there are no moves to block or win. The AI will play a random move as long
#as the column is not full
def ai_rand():

    #Uses global gamestate list
    global globalGamestate

    gamestate = globalGamestate

    #A randomly generated between 0 and 6 will be generated for the AI move
    AIMove = int(random.randrange(0,7))

    #If the Column is not full it will play there
    if (BLANK) in gamestate[AIMove]:
        return AIMove

    #If the Column is full it will keep recalling itself until it finds a non
    #full column
    elif (BLANK) not in gamestate[AIMove]:
        AIMove = ai_rand()
        return AIMove

#This function blocks the player from winning vertically
def ai_vert_block():

    global globalGamestate
    global color_player

    #Loops through the 7 columns
    for Col in range(COLUMN):
        gamestate = globalGamestate[Col]

        #This is where it cuts the column into 3 different 4 long columns.
        for CutCol in range(3):
            newV = gamestate[0 + CutCol:4 +CutCol]

            #Counts how many color_player tokens are in the newV
            Pcount = newV.count(color_player)

            #If there are 3 player tokens, and the first index is a BLANK
            #the AI will play on that BLANK to block the move. If not it
            #will contiune on with the sequence of possible AI moves
            if ((Pcount == 3) and (newV[0] == BLANK)):
                return Col

    #If no vertical blocks found it will do a random move
    aimove = ai_rand()
    return aimove

#This function blocks the player from winning horizontally
def ai_hort_block():

    global globalGamestate
    global color_player

    gamestate = globalGamestate

    #Loops 6 times, to create a new list for each horiozontal row
    for row in range(ROW):
        horizontal = (gamestate[0][row] + gamestate[1][row] + gamestate[2][row] \
                    + gamestate[3][row] + gamestate[4][row] + gamestate[5][row] \
                    + gamestate[6][row])

        #Cuts the horizontal rows into 4 differnet 4 long rows
        for cut in range(4):
            newH = horizontal[0 + cut:4 + cut]

            #Counts how many BLANK and color_player tokens there are in each newH
            PCount = newH.count(color_player)
            BCount = newH.count(BLANK)

            #Counts to see if there are 3 player tokens and 1 blank token
            if ((PCount == 3 and BCount == 1)):
                index = newH.index(BLANK)

                #Placement is where the AI move can block the win
                placement = index + cut

                #Checks to see if there are any blank spaces below the placement
                #If returned as true, the AI will play there, if false it will
                #continue on with the series of AI move functions
                if valid_move(placement, row + 1) == True:
                    return placement

    #If no horizontal block is found it will try and look for a vertical block
    aimove = ai_vert_block()
    return aimove

#This functions checks to see if the AI can win vertically
def ai_vert_win():

    global globalGamestate
    global color_ai

    #Loops through the 7 columns
    for Col in range(COLUMN):
        gamestate = globalGamestate[Col]

        #This is where it cuts the column into 3 different 4 long columns.
        for CutCol in range(3):
            newV = gamestate[0 + CutCol:4 + CutCol]

            #Counts how many AI tokens are in the newV
            Acount = newV.count(color_ai)

            #If there are 3 AI tokens, and the first index is a BLANK
            #the AI will play on that BLANK to win. If not it
            #will contiune on with the sequence of possible AI moves
            if ((Acount == 3) and (newV[0] == BLANK)):
                return Col

    #If no vertical win is found it will check for a hortizontal block
    aimove = ai_hort_block()
    return aimove

#This functions checks to see if the AI can win horizontally
def ai_hort_win():

    global globalGamestate
    global color_ai

    gamestate = globalGamestate

    #Loops 6 times, to create a new list for each horiozontal row
    for row in range(ROW):
        horizontal = (gamestate[0][row] + gamestate[1][row] + gamestate[2][row] \
                    + gamestate[3][row] + gamestate[4][row] + gamestate[5][row] \
                    + gamestate[6][row])

        #Cuts the horizontal rows into 4 differnet 4 long rows
        for cut in range(4):
            newH = horizontal[0 + cut:4 + cut]

            #Counts how many BLANK and AI tokens there are in each newH
            ACount = newH.count(color_ai)
            BCount = newH.count(BLANK)

            #Counts to see if there are 3 player tokens and 1 blank token
            if ((ACount == 3 and BCount == 1)):
                index = newH.index(BLANK)

                #Placement is where the AI move can block the win
                placement = index + cut

                #Checks to see if there are any blank spaces below the placement
                #If returned as true, the AI will play there, if false it will
                #continue on with the series of AI move functions
                if valid_move(placement, row + 1) == True:
                    return placement

    #If no horizontal win is found it will try and look for a vertical win
    aimove = ai_vert_win()
    return aimove

#Updates the globalGamestate after each AI move
def update_gamestateai():

    global globalGamestate
    global color_ai

    #The column where the AI places its move.
    #AI sequence is : Horizontal Win, Vertical Win, Horizontal
    #Block, Vertical Block. If there are no valid moves from any
    #of those 4 functions, it will play a random move in a non full column
    column = ai_hort_win()
    column = int(column)

    #Finds a column list from returned AI move
    gamestate = globalGamestate
    gamestate = gamestate[column]

    #Finds the botto most BLANK in the column and replaces it with the AI Color
    if (BLANK) in gamestate:
        row = gamestate.count(BLANK) - 1
        gamestate[row] = color_ai

        #Draws the token move
        draw_token(column,color_ai,row)

        #Checks to see if there are any wins or a stalemate after each move
        check_vert_win()
        check_hori_win()
        check_diag_win()
        check_stalemate()

    #Returns the updated globalGamestate
    return globalGamestate

#Updates the globalGamestate after each player move
def update_gamestateplayer(column):

    global globalGamestate
    global color_player

    column = int(column)

    #Finds a column list from returned player click
    gamestate = globalGamestate
    gamestate = gamestate[column]

    #Finds the botto most BLANK in the column and replaces it with the player
    #color.
    if (BLANK) in gamestate:
        row = gamestate.count(BLANK) - 1
        gamestate[row] = color_player

        #Checks to see if there are any wins or a stalemate after each move
        draw_token(column,color_player,row)
        check_vert_win()
        check_hori_win()
        check_diag_win()
        check_stalemate()

    #Returns the updated globalGamestate
    return globalGamestate

#This function allows the player to click on the screen to allow them to pick
#the column they want to drop their token in.
def click(x, y):

    #Reference to the global gamestate of the game.
    global globalGamestate

    #The clickable area that a player can click to play their token in the
    #desired column they want.(x-limit is from the top of the buttons to the
    #bottom of the gameboard/y-limit is from the edges of the gameboard).
    if (x >= LEFTCLICKLIMIT and x <= RIGHTCLICKLIMIT) \
    and (y >= BOTTOMCLICKLIMIT and y <= TOPCLICKLIMIT):

        #Based on the x-cordinate that the player clicked on the screen, it
        #calculates which column the player clicked. The calculation shifts
        #the x-cordinate so that left limit of the board is positive since the
        #turtle screen is a cartisian plane. By using integer division
        #dividing by the size of an individual square the outcome is the index
        #of that specific column in the global gamestate.
        column = (x + MOVE_TO_ZERO) // SIZEOFSQ
        column = int(column)

        #Selects the column from the global gamestate based on the column the
        #player selected.
        gamestatecolumn = globalGamestate[column]

        #If the game column is not full it will allow the player to play their
        #token in that column they select as it is a valid move and will
        #update the global gamestate with their move and allow the AI to make
        #it's move.
        if gamestatecolumn.count(BLANK) != 0:

            #Updates the global gamestate based on the column the player
            #selected.
            gamestate = update_gamestateplayer(column)

            #Calls the AI to make it's move and updates the global gamestate
            #based on the move of the AI.
            update_gamestateai()

        #If the game column is full it will not allow that player to play their
        #token in the column they selected as it is not a valid move and writes
        #a message to inform the player.
        else:

            #Writes a message that tells the player that the column they
            #selected is full and to selected a different column that is not
            #full.
            message = 1
            draw_message(message)

    #If the player does not click in the clickable area a message will be
    #written informing the player.
    else:

        #Writes a messages informing that player that they did not click in the
        #clickable area to make a move.
        message = 2
        draw_message(message)

#This function checks to see if there is a vertical win for either AI or player
def check_vert_win():

    global globalGamestate

    #Loops through each of the 7 coloumns and creates a new list for each column
    for newCol in range(COLUMN):
        gamestate = globalGamestate[newCol]

        #This is where it cuts the column into 3 different 4 long columns.
        for combination in range(3):
            newV = gamestate[0 + combination :4 +combination]

            #Counts the number of Green Tokens and Red Tokens
            Gcount = newV.count(GREEN)
            Rcount = newV.count(RED)

            #If either the green token or red token count is 4, winner is
            #assigned a value and draw_winner() is called
            if (Rcount == 4):

                #Writes a message that the red player won.
                winner = 2
                draw_winner(winner)
            elif (Gcount == 4):

                #Writes a message that the green player won.
                winner = 1
                draw_winner(winner)

#This function checks to see if there is a horizntal win for either AI or Player
def check_hori_win():

    #Reference to the global gamestate of the game.
    global globalGamestate

    #Loops based on the number of horizontial combinations there are in the
    #game and checks to see if there are 4 in a row.
    for column in range(COMBIN_HCHECK):

        #Loops through the specific column and row
        for index in range(ROW):

            #Checks to see if there are 4 GREEN in a row.
            if GREEN == globalGamestate[column][index] \
            == globalGamestate[column+1][index] \
            == globalGamestate[column+2][index] \
            == globalGamestate[column+3][index]:

                print("Green Player, You Win!")

                #Writes a message that the green player won.
                winner = 1
                draw_winner(winner)

            #Checks to see if there are 4 RED in a row.
            elif RED == globalGamestate[column][index] \
            == globalGamestate[column+1][index] \
            == globalGamestate[column+2][index] \
            == globalGamestate[column+3][index]:

                print("Red Player, You Win!")

                #Writes a message that the red player won.
                winner = 2
                draw_winner(winner)

#This function checks for the diagonal combination of 4 'G' or 'R' for a winner.
def check_diag_win():

    #Reference to the global gamestate of the game.
    global globalGamestate

    #This is the first part of the diagonal that is within row range of (3,6).
    for random_column in range(COLUMN -3):
        for random_row in range(ROW-3,ROW):

            #It's trying to find the combination for GREEN.
            if GREEN == globalGamestate[random_column][random_row] and\
               GREEN == globalGamestate[random_column+1][random_row-1] and\
               GREEN == globalGamestate[random_column+2][random_row-2] and\
               GREEN == globalGamestate[random_column+3][random_row-3]:

                print("GreenPlayer, You Win!")

                #Writes a message that the green player won.
                winner = 1
                draw_winner(winner)

            #It's trying to find the combination for RED.
            if RED == globalGamestate[random_column][random_row] and\
               RED == globalGamestate[random_column+1][random_row-1] and\
               RED == globalGamestate[random_column+2][random_row-2] and\
               RED == globalGamestate[random_column+3][random_row-3]:

                print("RedPlayer, You Win!")

                #Writes a message that the red player won.
                winner = 2
                draw_winner(winner)

    #This is the first part of the diagonal that is within row range of (3,6).
    for random_column in range(COLUMN-3):
        for random_row in range(ROW-3):

            #It's trying to find the combination for GREEN.
            if GREEN == globalGamestate[random_column][random_row] and\
               GREEN == globalGamestate[random_column+1][random_row+1] and\
               GREEN == globalGamestate[random_column+2][random_row+2] and\
               GREEN == globalGamestate[random_column+3][random_row+3]:
                print("GreenPlayer,  You Win!")

                #Writes a message that the green player won.
                winner = 1
                draw_winner(winner)

            #It's trying to find the combination for RED.
            if RED == globalGamestate[random_column][random_row] and\
               RED == globalGamestate[random_column+1][random_row+1] and\
               RED == globalGamestate[random_column+2][random_row+2] and\
               RED == globalGamestate[random_column+3][random_row+3]:

                print("RedPlayer,  You Win!")

                #Writes a message that the red player won.
                winner = 2
                draw_winner(winner)

#This function checks if the entire board is full of tokens which is a
#stalemate.
def check_stalemate():

    #Reference to the global gamestate of the game.
    global globalGamestate

    #Accumulation patterns, if 'fullcolumn' is equal to 7 then it is a
    #stalemate.
    fullcolumn = 0

    #Checks each column of the global gamestate to check to see if the column
    #is full. If all 7 columns are full it will write a message that informs
    #the player that it is a stalemate.
    for eachcolumn in range(COLUMN):

        #Selects the column from the global gamestate based on the current loop.
        gamestatecolumn = globalGamestate[eachcolumn]

        #If the are no blanks in the column then 1 is added to 'fullcolumn'.
        if gamestatecolumn.count(BLANK) == 0:
            print("full column")
            fullcolumn = fullcolumn + 1

        #If the are still blanks in the column then 'fullcolumn' does not
        #change.
        else:
            fullcolumn = fullcolumn

    #When 'fullcolumn; is 7 meaning that all 7 columns are full then the game
    #is over and the result is a stalemate. A message is written on the screen
    #to inform the player.
    if fullcolumn == 7:
        print("full game")
        winner = 3

        #Writes a message that informs the player that the game is over and
        #it is a stalemate.
        draw_winner(winner)

#This function writes a message on the screen that tells the player that when
#the game is over that they can press the keyboard key 'n' to start a new game.
def newgame_message():

    #Reference to the turtle named 'draw'
    global draw

    #Moves the pen to the center of the screen.
    draw.goto(0,0)

    #Moves the pen into position to write the message on the screen.
    draw.right(90)
    draw.forward(NEW_DIST)
    draw.left(90)

    #Puts the pen down in order to write on the screen and assigns a pen color.
    draw.pendown()
    draw.pencolor(NEW_COLOR)

    #Writes a message that tells the player that they can press the keyboard
    #key 'n' to start a new game.
    draw.write("Press 'n' on your keyboard to start a new game", \
    align = POSITON, font = (MESSAGE_FONT, FSIZE_WINNER, MODE_NORMAL))

    #Stops the pen from drawing anymore.
    draw.penup()

#This function is called when the player presses the the keyboard key 'n' and
#allows the player to start a new game.
def newgame():

    #Clears the screen with everything on it.
    turtle.resetscreen()

    #Starts the game from the beginning.
    main()

#This function writes a message when a player tries to click on a full column
#and not in the clickable area. Also writes an error message when there is a
#problem trying to save the game or loading the game.
def draw_message(message):

    #Reference to the global player color and ai color.
    global color_player
    global color_ai

    #Reference to the turtle named 'draw'
    global draw

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()

    #Move turtle to the center of the screen.
    draw.goto(0,0)

    #Moves the pen into position to write the message on the screen.
    draw.right(90)
    draw.forward(MESSAGE_DIST)
    draw.left(90)

    #Assigns a pen color.
    draw.pencolor(MESSAGE_COLOR)

    #Writes a message that tells the player that they need to click on a
    #different column that is not full.
    if message == 1:
        error_file_message = ("Invalid column! Please select a column that" \
        " is not full.")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message that tells the player that they did not click in the
    #clickable.
    elif message == 2:
        error_file_message = ("Invalid click! Please click on the buttons" \
        " or the gameboard to place your token")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message that tells the player that there was a error that
    #occured trying to save the game.
    elif message == 3:
        error_file_message = ("An error has occurred trying to save the game")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message that tells the player that there was a error that
    #occured trying to load the save file.
    elif message == 4:
        error_file_message = ("An error has occurred trying to open your" \
        " saved file!")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message that tells the player that the game is saved.
    elif message == 5:

        error_file_message = ("Game is saved")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message that tells the player that the game is saved.
    elif message == 6:

        error_file_message = ("Game is loading")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message if the player goes first.
    elif color_player == 'G':
        error_file_message = ("You go first")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Writes a message if the AI goes first.
    elif color_ai == 'G':
        error_file_message = ("AI goes first")
        draw.write(error_file_message, align = POSITON, \
        font = (MESSAGE_FONT, FSIZE_MESSAGE, MODE_NORMAL))

    #Delays the turtle so that the player can read the message.
    time.sleep(WAIT_TIME)

    #Erases the message from the screen.
    draw.forward(EDGE_OF_TEXT)
    draw.pendown()
    draw.pensize(ERASER)
    draw.left(180)
    draw.pencolor(ERASER_COLOR)
    draw.forward(ERASE_ALL_TEXT)
    draw.right(180)

    #Stops the pen from drawing anymore.
    draw.penup()

#This function will save the current 'color_player', 'color_ai', and
#'globalGamestate'.
def saving():

    #Reference to the global gamestate of the game, the color the player is
    #assigned and the ai color assigned.
    global globalGamestate
    global color_ai
    global color_player

    try:

        #This will make a file name call 'Connect4_Save_File.txt' and write
        #the current 'color_ai', 'color_player', and
        #'globalGamestate' in string.
        with open("Connect4_Save_File.txt", "w") as a_file:

            #Writes a message telling the player that the game has saved.
            message = 5
            draw_message(message)

            #'color_ai' will get saved then 'color_player' below it.
            a_file.write(color_ai + '\n')
            a_file.write(color_player +'\n')
            for column_index in range(COLUMN):
                for row_index in range (ROW):

                    a_file.write \
                    (globalGamestate[column_index][row_index].strip("',[]"))
                a_file.write('\n')

    #If anything goes wrong while saving the data a message will be written
    #informing the player there was a problem trying to save the game.
    except IOError:
        print("Encountered problem while reading data from the savefile")

        #Writes a message telling the player that there was a problem trying to
        #save the game.
        message = 3
        draw_message(message)

#This function will load the saved file.
def loading():

    #Reference to the global gamestate of the game, the color the player is
    #assigned and the ai color assigned.
    global globalGamestate
    global color_player
    global color_ai

    try:

        #This will search for a file name called 'Connect4_Save_File.txt'
        #and reads the saved 'color_ai', 'color_ai', and 'globalGamestate'.
        with open("Connect4_Save_File.txt", "r") as a_file:

            #Writes a message telling the player that the game is loading.
            message = 6
            draw_message(message)

            #Clears the screen with everything on it.
            turtle.resetscreen()

            #This process will remove all the whitespaces.
            color_ai = a_file.readline().strip()
            color_player = a_file.readline().strip()

            #This will convert the 'globalGamestate' from string to a list.
            globalGamestate = []
            for column_line in a_file:
                comp = column_line.strip()
                gamecolumn = []
                for row_index in range(len(comp)):
                    gamecolumn.append(comp[row_index])
                globalGamestate.append(gamecolumn)
            print(globalGamestate)

        #Redraws the tokens of the player and AI where they were saved.
        loading_redraw()

        #Redraws the entire game.
        loadmain()

    #If anthing happens wrong within loading process a message will be written
    #informing the player there was a problem trying to load the save file.
    except IOError:
        print("Encountered problem while reading data from the savefile")
        message = 4
        draw_message(message)

#This function will load the saved 'globalGamestate' and draw it the player and
#AI token.
def loading_redraw():

    #Reference to the global gamestate of the game.
    global globalGamestate

    gamestate = globalGamestate
    #This loop will locate every single GREEN and RED in saved 'globalGamestate'
    #and use draw_token() function to redraw.
    for i in range(COLUMN):
        for j in range(ROW):
            if gamestate[i][j] == GREEN:
                draw_token(i,GREEN,j)
            elif gamestate[i][j] == RED:
                draw_token(i,RED,j)

#This function is the main function that starts the game.
def main():

    #Assign the gamestate, player color, ai color and turtles as global variable.
    global globalGamestate
    global color_player
    global color_ai
    global draw
    global tokenmove

    #Creates the turtle screen and the turtle.
    wn = turtle.Screen()
    draw = turtle.Turtle()
    tokenmove = turtle.Turtle()

    #Hides the turtle so it does not appear on the screen.
    draw.hideturtle()
    tokenmove.hideturtle()

    #Random selects whether the player or AI goes first.
    number = first_random()

    #Makes the global variables of the gamestate, player color, ai color
    color_player = choose_color_player(number)
    color_ai = choose_color_ai()
    globalGamestate = creategamestate()

    #Draws the gameboard, buttons, starting information about the game,
    #keyboard key information, and which color the player and AI are.
    draw_gameboard()
    draw_button()
    draw_intro()
    draw_keyinfo()
    draw_playercolor()
    message = 0
    draw_message(message)

    #Green player will go first. If the AI was assigned to GREEN it will go
    #first.
    firstmove()

    #Allows the the player to click on a specific keyboard key and performs a
    #functions.
    wn.listen()
    wn.onkey(saving,'s')
    wn.onkey(loading,'l')
    wn.onkey(newgame,'n')

    #Allows the player to click on the screen pick the column that want to play.
    wn.onclick(click)

    #Loops the click.
    wn.mainloop()

#This function redraws the entire game based on the saved file and allows the
#player to continue playing where they saved.
def loadmain():
    draw_gameboard()
    draw_button()
    draw_intro()
    draw_keyinfo()
    draw_playercolor()
    wn.onclick(click)
    wn.mainloop()

#Calls the main function.
main()
