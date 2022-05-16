import time

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

st = False

#=========================================================================
#=========================================================================
#=========================================================================

class player():
    
    def __init__(self, name, score, tick):
        self.name = name
        self.score = score
        self.tick = tick

    def add_score(self):
        self.score += 1
        
    def reset_score(self):
        self.score = 0
        
    def value(self):
        return self.name, self.score, self.tick

#=========================================================================
#=========================================================================
#=========================================================================
class cell():
    
    def __init__(self, x, y, s, tick):
        self.x = x
        self.y = y
        self.s = s
        self.tick = tick
        
    def show(self):
        rect(self.x, self.y, self.s, self.s)
        if self.tick != 0:
            self.tick.resize(100,100)
            image(self.tick, self.x, self.y)
        
    def tick_update(self, new_tick):
        if self.tick == 0:
            self.tick = new_tick
            return 1
        else:
            return 0
        
    def value(self):
        return self.x, self.y, self.s
    
    def get_tick(self):
        return self.tick
    
#=========================================================================
#=========================================================================
#=========================================================================
    
class button():
    
    def __init__(self, txt, action, x, y, w, h, state):
        self.txt = txt
        self.action = action
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = state
        
    def show(self):

        noFill()
        textSize(24)
        stroke(234,234,235)
        strokeWeight(3)
        textAlign(CENTER)
        
        rect(self.x, self.y, self.w, self.h, 5)
        fill(255)
        text(self.txt,self.x + (self.w/2), self.y + (self.h / 2) + 7.5)
        
    def clicked(self):
        if (mouseX > self.x and mouseY > self.y) and (mouseX < self.x + self.w and mouseY < self.y + self.h):
            fill(255, 30)
            noStroke()
            
            rect(self.x, self.y, self.w, self.h, 5)

            if mousePressed == True and self.state == False:
                return self.action
            
        return None
    
#=========================================================================
#=========================================================================
#=========================================================================

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

def render_frame(f_list):
    
    # elapsed = (time.time() + 0.0) % 1.3 
    # frame = elapsed/0.05
    # image(f_list[int(frame)], 0, 0)
    
    image(f_list[int(((time.time() + 0.0) % 1.3)/0.05 )], 0, 0)

#=========================================================================
#=========================================================================
#=========================================================================

def add_tick(tick, mx, my):
    v = False
    for y in range(len(board)):
        for x in range(len(board[y])):
            bx, by, bs = board[y][x].value()
            if (mx > bx  and my > by) and (mx < bx + bs and my < by + bs): 
                v = board[y][x].tick_update(tick)
                break
    return v                
#=========================================================================
#=========================================================================
#=========================================================================

def check_win():
    for y in range(len(board)):
        if board[y][0].get_tick() != 0:
            if board[y][0].get_tick() == board[y][1].get_tick() and board[y][1].get_tick() == board[y][2].get_tick():
                return True
                    
    for x in range(len(board[y])):  
        if board[0][x].get_tick() != 0:  
            if board[0][x].get_tick() == board[1][x].get_tick() and board[1][x].get_tick() == board[2][x].get_tick():
                return True
            
    if board[1][1].get_tick() != 0:
        if board[0][2].get_tick() == board[1][1].get_tick() and board[1][1].get_tick() == board[2][0].get_tick():
                return True
        if board[0][0].get_tick() == board[1][1].get_tick() and board[1][1].get_tick() == board[2][2].get_tick():
                return True
            
#=========================================================================
#=========================================================================
#=========================================================================

def check_tie():
    occupied = 0
    for y in range(len(board)):
        for x in range(len(board[y])):  
            if board[y][x].get_tick() != 0:
                occupied += 1
                
    if occupied == 9:
        return True
        
#=========================================================================
#=========================================================================
#=========================================================================

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

def play_scene(b):
    background(12,76,100)
    
    stroke(234,234,235)
    strokeWeight(4)
    noFill()
    textAlign(LEFT)
    
    score = str(player1.value()[1]) + " : " + str(player2.value()[1])
    textSize(48)
    text(score, 292.5, 470)
    
    textSize(24)
    text("TIC-TAC-TOE", 267.5, 60)
    
    textSize(14)
    
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
        
    for y in range(len(b)):
        for x in range(len(b[y])):
            b[y][x].show()

#=========================================================================
#=========================================================================
#=========================================================================

def start_scene():
    global logo
    
    background(12,76,100)
    
    image(logo, 400, 120)
    
    play = button("play", "play", 100, 120, 200, 50, st)
    play.show()
    action_manager(play.clicked())
    
    help = button("help", "help", 100, 190, 200, 50, st)
    help.show()
    action_manager(help.clicked())
    
    setting = button("settings", "settings", 100, 260, 200, 50, st)
    setting.show()
    setting.clicked()
    
    quit = button("quit", "quit", 100, 330, 200, 50, st)
    quit.show()
    action_manager(quit.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

def setting_scene():
    background(12,76,100)
    
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

def help_scene():
    background(12,76,100)
    textAlign(LEFT)
    
    fill(255)
    textSize(24)
    text("how to play:", 75, 100)
    
    textSize(18)
    text("1. The game is played on a grid that's 3 squares by 3 squares.", 90, 150)
    text("2. You are X, your friend is O. Players take turns putting their" , 90, 190) 
    text("marks in empty squares.", 115, 210)
    text("3. The first player to get 3 of her marks in a row (up, down,", 90, 250)    
    text("across, or diagonally) is the winner.", 115, 270) 
    text("4. When all 9 squares are full, the game is over. If no player", 90, 310)
    text("has 3 marks in a row, the game ends in a tie.", 115, 330)
        
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def end_scene():
    background(12,76,100)
    image(trophy, 265, 230)
    
    fill(255,215,0)
    textSize(32)
    textAlign(CENTER)
        
    render_frame(win_animation)
    
    if player1.value()[1] == total_score:
        winner = "Player X"
        
    elif player2.value()[1] == total_score:
        winner = "Player O"
    
    text(winner + " has won!", 350, 150)
    
    menu = button("return", "menu", 50, 420, 120, 50, st)
    menu.show()
    action_manager(menu.clicked())
    
#=========================================================================
#=========================================================================
#=========================================================================

def action_manager(action):
    global gameon, settingon, helpon, starton, playon, endon, scd
    
    if action == "play":
        starton = False
        playon = True
        scd = 50
        
    if action == "help":
        starton = False
        helpon = True
        
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
    
    size(700, 500)
    frameRate(120)
    
    logo = loadImage("sample_design.png")
    logo.resize(200, 256)
    trophy = loadImage("trophy.png")
    trophy.resize(170,177)
    X_tick = loadImage("tick_X.png")
    X_tick.resize(100,100)
    O_tick = loadImage("tick_O.png")
    O_tick.resize(100,100)
    
    global win_animation
    
    win_animation = init_animation()
    
    global player1, player2
    
    player1 = player("bot1", 0, X_tick)
    player2 = player("bot2", 0, O_tick)
    
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
    
    if starton == True:
        start_scene()
        
    if settingon == True:
        setting_scene()
            
    if helpon == True:
        help_scene()
    
    if playon == True:
        
        if player1.value()[1] == total_score or player2.value()[1] == total_score:
            playon = False
            endon = True
        
        play_scene(board)
        if check_win() == True and cd < 0:
            
            if turn % 2 == 0:
                player1.add_score()
                
            elif turn % 2 != 0:
                player2.add_score() 
                
            turn = 1
            board = reset_board()
            
        if check_tie() == True and cd < 0:
            
            turn = 1
            board = reset_board()
        
        if cd > -1:    
            cd -= 1 
            
        if scd > -1:
            scd -= 1
            
        
    if endon == True:
        end_scene()
    
    if gameon == False:
        exit()
        
    st = mousePressed
        
#=========================================================================
#=========================================================================
#=========================================================================

def mouseClicked():
    global turn, cd, scd
    
    if check_win() == None and playon == True:
        if scd < 0:
            if turn % 2 != 0:
                tick = X_tick
                c = add_tick(tick, mouseX, mouseY)
                cd = 200
    
            elif turn % 2 == 0:
                tick = O_tick
                c = add_tick(tick, mouseX, mouseY)
                cd = 200
                
            turn += c
        
    
    
