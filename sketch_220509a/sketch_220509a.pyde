board = [
         [],
         [],
         []
    ]

O_player = None
X_player = None

#=========================================================================
#=========================================================================
#=========================================================================

class player():
    
    def __init__(self, name, action, score, tick_board):
        self.name = name
        self.action = action
        self.score = score
        self.tick_board = tick_board
    
    def get_name():
        pass
        
    def score():
        pass
        
    def add_tick():
        pass
        
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
        
class tick_box():
    
    def __init__(self):
        pass
        
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
        
def tick():
    pass
    
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
    size(700, 500)
    
def draw():
    pass
    
#=========================================================================
#=========================================================================
#=========================================================================

def keyPressed():
    pass