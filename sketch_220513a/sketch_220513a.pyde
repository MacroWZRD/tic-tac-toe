#libraries
import time

#global variables
board = [
         [],
         [],
         []
    ]

turn = 1
cd = 0
scd = 0

total_score = 3

gameon = True
starton = True
settingon = False
helpon = False
playon = False
endon = False

num = [1,2,3,4,5,6,7,8,9]
st = False

#=========================================================================
#=========================================================================
#=========================================================================

#player object
class player():
    #store object name, score, tick
    def __init__(self, name, score, tick):
        self.name = name
        self.score = score
        self.tick = tick
    #add 1 to player score
    def add_score(self):
        self.score += 1
    #reset the player score
    def reset_score(self):
        self.score = 0
    #return the stored object values
    def value(self):
        return self.name, self.score, self.tick

#=========================================================================
#=========================================================================
#=========================================================================

#board box object
class cell():
    #store x coord, y coord, size, tick
    def __init__(self, x, y, s, tick):
        self.x = x
        self.y = y
        self.s = s
        self.tick = tick
    #render the box
    def show(self):
        rect(self.x, self.y, self.s, self.s)
        if self.tick != 0:
            self.tick.resize(100,100)
            image(self.tick, self.x, self.y)
    #add tick to box
    def tick_update(self, new_tick):
        #check if box is unoccupied
        if self.tick == 0:
            self.tick = new_tick
            return 1
        else:
            return 0
    #return dimensions of the box
    def value(self):
        return self.x, self.y, self.s
    #return the tick stored in the box
    def get_tick(self):
        return self.tick
    
#=========================================================================
#=========================================================================
#=========================================================================
    
#button object
class button():
    #store object text, action, x coord, y coord, widht, height, state
    def __init__(self, txt, action, x, y, w, h, state):
        self.txt = txt
        self.action = action
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = state
    #render the button and text
    def show(self):
        noFill()
        textSize(24)
        stroke(234,234,235)
        strokeWeight(3)
        textAlign(CENTER)
        
        rect(self.x, self.y, self.w, self.h, 5)
        fill(255)
        text(self.txt,self.x + (self.w/2), self.y + (self.h / 2) + 7.5)
    #check if the button is clicked and return an action    
    def clicked(self):
        if (mouseX > self.x and mouseY > self.y) and (mouseX < self.x + self.w and mouseY < self.y + self.h):
            fill(255, 30)
            noStroke()
            #hover effect for button
            rect(self.x, self.y, self.w, self.h, 5)

            if mousePressed == True and self.state == False:
                return self.action
            
        return None
    
#=========================================================================
#=========================================================================
#=========================================================================

#create a list to store animation frames from the "animation" folder
def init_animation():
    maxframe = 26
    framelist = []
    for i in range(maxframe):
        # frame = loadImage("animation/frame_" + ("0" if i < 10 else "") + str(i) + "_delay-0.05s.png")
        frame = loadImage("animation/(" + str(i) + ").png")
        frame.resize(1206,506)
        framelist.append(frame)
        
    return framelist

#=========================================================================
#=========================================================================
#=========================================================================

#render the frames stored inside a list containing frames
def render_frame(f_list):
    
    # elapsed = (time.time() + 0.0) % 1.3 
    # frame = elapsed/0.05
    # image(f_list[int(frame)], 0, 0)
    
    image(f_list[int(((time.time() + 0.0) % 1.3)/0.05 )], 0, 0)

#=========================================================================
#=========================================================================
#=========================================================================

#add a tick to the board
def add_tick(tick, mx, my):
    v = False
    #iterate through the board
    for y in range(len(board)):
        for x in range(len(board[y])):
            #store box coords and dimensions
            bx, by, bs = board[y][x].value()
            #check if mouse is within the box
            if (mx > bx  and my > by) and (mx < bx + bs and my < by + bs): 
                v = board[y][x].tick_update(tick)
                break
    return v                
#=========================================================================
#=========================================================================
#=========================================================================

#check if a player has won
def check_win():
    #check rows
    for y in range(len(board)):
        if board[y][0].get_tick() != 0:
            if board[y][0].get_tick() == board[y][1].get_tick() and board[y][1].get_tick() == board[y][2].get_tick():
                return True
    #check columns                
    for x in range(len(board[y])):  
        if board[0][x].get_tick() != 0:  
            if board[0][x].get_tick() == board[1][x].get_tick() and board[1][x].get_tick() == board[2][x].get_tick():
                return True
    #check diagonals        
    if board[1][1].get_tick() != 0:
        if board[0][2].get_tick() == board[1][1].get_tick() and board[1][1].get_tick() == board[2][0].get_tick():
                return True
        if board[0][0].get_tick() == board[1][1].get_tick() and board[1][1].get_tick() == board[2][2].get_tick():
                return True
            
#=========================================================================
#=========================================================================
#=========================================================================

#check if a tie has occured
def check_tie():
    occupied = 0
    for y in range(len(board)):
        for x in range(len(board[y])):  
            if board[y][x].get_tick() != 0:
                occupied += 1
    #check if all boxes are occupied            
    if occupied == 9:
        return True
        
#=========================================================================
#=========================================================================
#=========================================================================

#reset the values stored in the board
def reset_board():
    
    b = [
         [],
         [],
         []
    ]
    
    box_y = 100
    for i in range(3):
        box_x = 191
        for j in range(3):
            b[i].append(cell(box_x, box_y, 100, 0))
            box_x += 103
        box_y += 103
    
    return b

#=========================================================================
#=========================================================================
#=========================================================================

#display the play screen
def play_scene(b):
    background(12,76,100)
    
    #set default values
    stroke(234,234,235)
    strokeWeight(4)
    noFill()
    textAlign(LEFT)
    
    #show the current score
    score = str(player1.value()[1]) + " : " + str(player2.value()[1])
    textSize(48)
    text(score, 292.5, 470)
    
    #show the title
    textSize(24)
    text("TIC-TAC-TOE", 267.5, 60)
    
    textSize(14)
    #display player's turn with red highlight
    if turn % 2 != 0:
        fill(255,69,0)
        text("PLAYERX", 210, 460)
        fill(234,234,235)
        text("PLAYERO", 420, 460)
        
    elif turn % 2 == 0:
        fill(255,69,0)
        text("PLAYERO", 420, 460)
        fill(234,234,235)
        text("PLAYERX", 210, 460)
        
    noFill()  
    
    #display the board
    for y in range(len(b)):
        for x in range(len(b[y])):
            b[y][x].show()

#=========================================================================
#=========================================================================
#=========================================================================

#display the start/welcome screen
def start_scene():
    global logo
    
    background(12,76,100)
    #display the logo
    image(logo, 400, 120)
    
    #create a play button to start the game
    play = button("play", "play", 100, 120, 200, 50, st)
    play.show()
    action_manager(play.clicked())
    
    #create a help button to open the instructions screen
    help = button("help", "help", 100, 190, 200, 50, st)
    help.show()
    action_manager(help.clicked())
    
    #create a settings button to change aspects of the game
    setting = button("settings", "settings", 100, 260, 200, 50, st)
    setting.show()
    action_manager(setting.clicked())
    
    #create a quit button to exit the game
    quit = button("quit", "quit", 100, 330, 200, 50, st)
    quit.show()
    action_manager(quit.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

#display settings screen
def setting_scene():
    background(12,76,100)
    
    #set default values
    textAlign(LEFT)
    fill(255)
    
    #show the title
    textSize(24)
    text("settings:", 75, 100)
    
    #show the options
    textSize(18)    
    strokeWeight(2)
    text("number of games", 90, 150)
    rect(255, 134, 32, 18)
    text("(max: 9)", 300, 150)
    
    #show the changeable values
    fill(0)
    text(total_score, 265, 150)
    
    #create a return button that takes the user back to the start screen
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

#display help screen
def help_scene():
    background(12,76,100)
    #set default values
    textAlign(LEFT)
    fill(255)
    
    #show title
    textSize(24)
    text("how to play:", 75, 100)
    
    #show the intructions
    textSize(18)
    text("1. The game is played on a grid that's 3 squares by 3 squares.", 90, 150)
    text("2. You are X, your friend is O. Players take turns putting their" , 90, 190) 
    text("marks in empty squares.", 115, 210)
    text("3. The first player to get 3 of their marks in a row (up, down,", 90, 250)    
    text("across, or diagonally) is the winner.", 115, 270) 
    text("4. When all 9 squares are full, the game is over. If no player", 90, 310)
    text("has 3 marks in a row, the game ends in a tie.", 115, 330)
    
    #create a return button that takes the user back to the start screen    
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def end_scene():
    background(12,76,100)
    
    #render the trophy image
    image(trophy, 265, 230)
    
    #set default values
    fill(255,215,0)
    textSize(32)
    textAlign(CENTER)
    
    #render the confetti animation    
    render_frame(win_animation)
    
    #check if player X or player O won
    if player1.value()[1] == total_score:
        winner = "Player X"
    elif player2.value()[1] == total_score:
        winner = "Player O"
    
    #show the congratulatory message
    text(winner + " has won!", 350, 150)
    
    #create a return button that takes the user back to the start screen    
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

#manage button actions
def action_manager(action):
    global gameon, settingon, helpon, starton, playon, endon, scd
    
    if action == "play":
        starton = False
        playon = True
        scd = 50
        
    if action == "help":
        starton = False
        helpon = True
        
    if action == "settings":
        starton = False
        settingon = True
        
    if action == "menu":
        player1.reset_score()
        player2.reset_score()
        helpon = False
        settingon = False
        endon = False
        starton = True
        
    if action == "quit":
        gameon = False

#=========================================================================
#=========================================================================
#=========================================================================
    
def setup():
    global X_tick, O_tick, trophy, logo
    
    #set window propreties
    size(700, 500)
    frameRate(120)
    
    #initiate image variables
    logo = loadImage("sample_design.png")
    logo.resize(200, 256)
    trophy = loadImage("trophy.png")
    trophy.resize(170,177)
    X_tick = loadImage("tick_X.png")
    X_tick.resize(100,100)
    O_tick = loadImage("tick_O.png")
    O_tick.resize(100,100)
    
    global win_animation
    
    #initiate the animation list
    win_animation = init_animation()
    
    global player1, player2
    
    #create the players
    player1 = player("bot1", 0, X_tick)
    player2 = player("bot2", 0, O_tick)
    
    #initiate the board
    box_y = 100
    for i in range(3):
        box_x = 191
        for j in range(3):
            board[i].append(cell(box_x, box_y, 100, 0))
            box_x += 103
        box_y += 103
        
#=========================================================================
#=========================================================================
#=========================================================================
    
def draw():
    global gameon, starton, playon, endon, board, turn, total_score, cd, scd
    
    global st
    
    #show start screen
    if starton == True:
        start_scene()
    
    #show settings screen
    if settingon == True:
        setting_scene()
    
    #show help screen        
    if helpon == True:
        help_scene()
    
    #show play screen
    if playon == True:
        
        #check if either player has won
        if player1.value()[1] == total_score or player2.value()[1] == total_score:
            playon = False
            endon = True
        
        #display the board
        play_scene(board)
        #check if the player has won a game
        if check_win() == True and cd < 0:
            #check if x turn
            if turn % 2 == 0:
                player1.add_score()
            #check if o turn
            elif turn % 2 != 0:
                player2.add_score() 
            #reset values    
            turn = 1
            board = reset_board()
        #check if tie    
        if check_tie() == True and cd < 0:
            #reset values
            turn = 1
            board = reset_board()
        
        #decrease cooldown 
        if cd > -1:    
            cd -= 1 
            
        if scd > -1:
            scd -= 1
            
    #display end screen    
    if endon == True:
        end_scene()
    
    #exit the game
    if gameon == False:
        exit()
    
    #save mouse state    
    st = mousePressed
        
#=========================================================================
#=========================================================================
#=========================================================================

def mouseClicked():
    global turn, cd, scd
    
    #check if game is in progress
    if check_win() == None and playon == True:
        #start cooldown to avoid unintentional tick placement
        if scd < 0:
            #check if X turn
            if turn % 2 != 0:
                tick = X_tick
                c = add_tick(tick, mouseX, mouseY)
                cd = 200
            #check if O turn
            elif turn % 2 == 0:
                tick = O_tick
                c = add_tick(tick, mouseX, mouseY)
                cd = 200
            #increment turn if tick is added    
            turn += c
    
#=========================================================================
#=========================================================================
#=========================================================================

def keyPressed():
    global total_score
    
    #check if settings screen is on
    if settingon == True:
        #iterate through a list containing numbers
        for k in num:
            #set pressed key as win condition
            if key == str(k):
                total_score = k
