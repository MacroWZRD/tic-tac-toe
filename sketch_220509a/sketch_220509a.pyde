board = [
         [],
         [],
         []
    ]

O_player = None
X_player = None

turn = 0

#=========================================================================
#=========================================================================
#=========================================================================

class player():
    
    def __init__(self, name, action, score, tick, b):
        self.name = name
        self.action = action
        self.score = score
        self.tick = tick
        self.b = b

    def add_score():
        self.score += 1
        
    def add_tick():
        if mousePressed == True:
            for y in range(len(board)):
                for x in range(len(board[y])):
                    x1, y1, w1, h1 = self.b[y][x].value()
                    if (mouseX > x1 and mouseY > y1) and (mouseX < x1 + w1 and mouseY < y1 + h1):
                        return x1, y1
        
    def show_profile():
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
        if self.tick != 0:
            image(self.tick, self.x, self.y)
        rect(self.x, self.y, self.w, self.h)
        
        
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
    O_tick = loadImage("tick_O.png")


    #board setup
    box_y = 100
    box_size = 100
    
    for i in range(3):
        box_x = 200
        for j in range(3):
            board[i].append(draw_box(box_x, box_y, box_size, box_size, X_tick))
            box_x += box_size
        box_y += box_size
            
    print(board)
    
def draw():
    draw_board(board, mono)
    
#=========================================================================
#=========================================================================
#=========================================================================

def keyPressed():
    pass
