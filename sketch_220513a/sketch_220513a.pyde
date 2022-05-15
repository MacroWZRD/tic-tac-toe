board = [
         [],
         [],
         []
    ]

turn = 1
cd = 0

gameon = True
starton = True
settingon = False
helpon = False
playon = False
endon = False
exiton = False

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
    
    def __init__(self, img, action, x, y, w, h, state):
        self.img = img
        self.action = action
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = state
        
    def show(self):
        
        tint(255)
        image(self.img, self.x, self.y)
        
    def clicked(self):
        if (mouseX > self.x and mouseY > self.y) and (mouseX < self.x + self.w and mouseY < self.y + self.h):
            tint(200)
            image(self.img, self.x, self.y)
            if mousePressed == True and self.state == False:
                return self.action
            
        return None
        
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
    background(12,76,100)
    
#=========================================================================
#=========================================================================
#=========================================================================

def setting_scene():
    background(12,76,100)
    
#=========================================================================
#=========================================================================
#=========================================================================

def help_scene():
    background(12,76,100)
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def end_scene():
    background(12,76,100)
    image(trophy, 265, 230)
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def setup():
    global X_tick, O_tick, trophy
    
    size(700, 500)
    frameRate(120)
    
    trophy = loadImage("trophy.png")
    trophy.resize(170,177)
    X_tick = loadImage("tick_X.png")
    X_tick.resize(100,100)
    O_tick = loadImage("tick_O.png")
    O_tick.resize(100,100)
    
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
    global gameon, starton, playon, endon, board, turn, cd
    
    # playon = True
    endon = True
    
    if playon == True:
        
        play_scene(board)
        if check_win() == True and cd < 0:
            
            if turn % 2 == 0:
                player1.add_score()
                
            elif turn % 2 != 0:
                player2.add_score() 
                
            print(player1.value()[1])
            print(player2.value()[1])
                
                
            turn = 1
            board = reset_board()
            
        if check_tie() == True and cd < 0:
            
            turn = 1
            board = reset_board()
            
        cd -= 1 
        
    if endon == True:
        end_scene()
    
    if exiton == True:
        exit()
        
#=========================================================================
#=========================================================================
#=========================================================================

def mouseClicked():
    global turn, cd
    
    if check_win() == None and playon == True:
        if turn % 2 != 0:
            tick = X_tick
            c = add_tick(tick, mouseX, mouseY)
            cd = 200

        elif turn % 2 == 0:
            tick = O_tick
            c = add_tick(tick, mouseX, mouseY)
            cd = 200
                
        turn += c
        
    
    
    
