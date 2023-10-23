def setup():
    size(500, 500)

def draw():
    background(0, 0, 255)
    noStroke()
    fill(0, 255, 255)
    
    if mouseX > width / 2 and mouseY > height / 2:
        rect(255, 255, width / 2, height / 2)
    elif mouseX > width / 2 and mouseY < height / 2:
        rect(255, 0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY < height / 2:
        rect(0, 0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY > height / 2:
        rect(0, 255, width / 2, height / 2)
