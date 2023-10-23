mouseX1 = 0 
poleHeight = 0
def setup():
    size(500, 500)
    
    f = createFont("Times New Roman", 16, True)
    textFont(f,28)




def draw():
    global mouseX1
    mouseX1 = mouseX
    if mouseX >= 400:
        mouseX1 = 400
    elif mouseX1 <= 100:
        mouseX1 = 100
    
    background(255)
    line(100, 400, 100, 100)
    line(100, 400, mouseX1, 400)
    line(100, 100, mouseX1, 400)
    
    rotate(radians(0))
    fill(0)
    text(mouseX, 250, 450)
    text("12", mouseX1-50, 390)
    text(poleHeight, 60, 250)
    
