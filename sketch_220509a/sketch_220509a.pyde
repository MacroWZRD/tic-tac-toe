board = [
         [],
         [],
         []
    ]

O_player = None
X_player = None

turn = 1
num = 1

#=========================================================================
#=========================================================================
#=========================================================================

class player():
    
    def __init__(self, name, action, score, tick, b):
        self.name = name
        self.action = action
        self.score = score
        self.b = b
        self.tick = tick

    def add_score(self):
        self.score += 1
        
    def add_tick(self):
        if mousePressed == True:
            for y in range(len(self.b)):
                for x in range(len(self.b[y])):
                    x1, y1, w1, h1 = self.b[y][x].value()
                    if (mouseX > x1 and mouseY > y1) and (mouseX < x1 + w1 and mouseY < y1 + h1):
                        return x1, y1, self.tick

        return 0, 0, 0

        
    def show_profile(self):
        pass
        
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
        
def start_scene():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def end_scene():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================

def draw_board(b, f):
    background(12,76,100)
    textFont(f)
    textSize(32)
    text("Tic-Tac-Toe", 242, 70)
    for y in range(len(board)):
        for x in range(len(board[y])):
            b[y][x].show()

   
def update_board(b, t, c_x, c_y):
    for y in range(len(b)):
        for x in range(len(b[y])):
            if c_x == b[y][x].value()[0] and c_y == b[y][x].value()[1]:
                b[y][x].update(t)
    
#=========================================================================
#=========================================================================
#=========================================================================

class draw_box():
    
    def __init__(self, x, y, w, h, tick):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tick = tick
        
    def show(self):
        noFill()
        stroke(234,234,235)
        strokeWeight(4)
        
        if self.tick == 1:
            image(X_tick, self.x, self.y)
        elif self.tick == 2:
            image(O_tick, self.x, self.y)
            
        rect(self.x, self.y, self.w, self.h)
        
    def update(self, new_tick):
        if self.tick == 0:
            self.tick = new_tick
        
    def value(self):
        return self.x, self.y, self.w, self.h
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def check_winner():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def score():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================
    
def setup():
    
    global mono, X_tick, O_tick
    
    size(700, 500)

    #load files
    mono = loadFont("OCRAExtended-48.vlw")
    X_tick = loadImage("tick_X.png")
    X_tick.resize(100,100)
    O_tick = loadImage("tick_O.png")
    O_tick.resize(100,100)
    
    
    global O_Player, X_Player
    X_Player = player("bot2", None, 0, 1, board)
    O_Player = player("bot1", None, 0, 2, board)


    #board setup
    box_y = 100
    box_size = 100
    
    for i in range(3):
        box_x = 200
        for j in range(3):
            board[i].append(draw_box(box_x, box_y, box_size, box_size, 0))
            box_x += box_size
        box_y += box_size
    
def draw():
    
    draw_board(board, mono)
    if turn % 2 != 0:
        check_x, check_y, num = X_Player.add_tick()
    elif turn % 2 == 0:
        check_x, check_y, num = O_Player.add_tick()
    
    update_board(board, num, check_x, check_y)
    
#=========================================================================
#=========================================================================
#=========================================================================

def keyPressed():
    pass
