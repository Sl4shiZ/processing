def setup():
    colorMode(RGB)
    size(500, 500)
    
def draw():
    background(0, 0, 0)
    noStroke()
    
    
    
        
    if mouseX >= 100 and mouseX <= 300 and mouseY >= 100 and mouseY <= 300:
        if mouseX >= width / 2 and mouseY >= height / 2:
            circle(250, 250, 150)
            fill(68, 218, 115)
        
            circle(250, 250, 75)
            fill(186, 296, 68)
        elif mouseX <= width / 2 and mouseY >= height / 2:
            circle(250, 250, 150)
            fill(68, 134, 195)
        
            circle(250, 250, 75)
            fill(195, 56, 186)
        elif mouseX >= width / 2 and mouseY <= height / 2:
            circle(250, 250, 150)
            fill(195, 56, 186)
        
            circle(250, 250, 75)
            fill(68, 134, 195)
        elif mouseX <= width / 2 and mouseY <= height / 2:
            circle(250, 250, 150)
            fill(186, 296, 68)
        
            circle(250, 250, 75)
            fill(68, 218, 115)
        
    if mouseX > width / 2 and mouseY > height / 2:
        rect(255, 255, width / 2, height / 2)
    elif mouseX > width / 2 and mouseY < height / 2:
        rect(255, 0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY < height / 2:
        rect(0, 0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY > height / 2:
        rect(0, 255, width / 2, height / 2)
    
    
    
