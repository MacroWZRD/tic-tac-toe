board = [
         [],
         [],
         []
    ]

turn = 1
cd = 0

gameon = True
starton = True
playon = False
endon = False

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

def add_tick(tick, mx, my):
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
    
    for y in range(len(b)):
        for x in range(len(b[y])):
            b[y][x].show()

#=========================================================================
#=========================================================================
#=========================================================================

def start_scene():
    background(0)
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def end_scene():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def setup():
    global X_tick, O_tick
    
    size(700, 500)
    frameRate(120)
    
    X_tick = loadImage("tick_X.png")
    X_tick.resize(100,100)
    O_tick = loadImage("tick_O.png")
    O_tick.resize(100,100)
    
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
    
    if starton == True:
        start_scene()
        if mousePressed == True:
            starton = False
            playon = True
            cd = 100
    
    if playon == True:
        play_scene(board)
        
        if check_win() == True and cd < 0:
            turn = 1
            board = reset_board()
        cd -= 1 
    
    
#=========================================================================
#=========================================================================
#=========================================================================

def mouseClicked():
    global turn, cd
    
    if check_win() == None and playon == True and cd < 0:
        if turn % 2 != 0:
            tick = X_tick
            c = add_tick(tick, mouseX, mouseY)
            cd = 200
            
        elif turn % 2 == 0:
            tick = O_tick
            c = add_tick(tick, mouseX, mouseY)
            cd = 200
        
        turn += c
    
    
