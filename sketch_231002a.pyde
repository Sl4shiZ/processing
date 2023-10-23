def setup():
    size(500, 500)
    
def draw():

    circle(mouseX, mouseY, 100)
    fill(mouseX, mouseY, (mouseX / 2) + (mouseY / 2))

    noStroke()
