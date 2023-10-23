def setup():
    global cx
    global cy
    global r
    global theta
    global px
    global py
    global c
    global x 
    global y
    size(1000,1000)
    cx = width / 2
    cy = height / 2
    px = cx
    py = cy
    background(0)
    colorMode(HSB)
    
x = 0
y = 0
cx = 0
cy = 0
r = 100
theta = 0
px = 0
py = 0
c = 0



def draw():
    global cx
    global cy
    global r
    global theta
    global px
    global py
    global c
    global x
    global y
    
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    stroke(c, 255, c * 2)
    strokeWeight(10)
    line(px, py, x, y)

    r = r + 1
    

    c = (c + 1) % 256

    theta = theta + mouseX + mouseY
    
    
    px = x
    py = y
    
    
