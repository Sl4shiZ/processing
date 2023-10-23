def setup():
    global cx, cy
    global px, py
    size(500, 500)
    # fullScreen()
    colorMode(RGB)
    cx = width / 2
    cy = height /2
    px = cx
    py = cy
    
cx = 0
cy = 0
r = 150
angle2 = 0

px = 0
py = 0
    
def draw():                           
    global cx, cy
    global px, py
    num = 16
    theta = TWO_PI / num
    
    background(0)
    stroke(255)
    strokeWeight(5)
    translate(cx, cy)
    
    

        
    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        c = (i / float(num)) * 255
        c = (c + mouseX) % 256
        ellipse(0, 100, 20, 100)
        fill(155, 42, 122)
        
        
        
        # line(0, 0, 0, 100)            
    
        popMatrix()
        
    
    
    fill(188, 140, 56)     
    circle(0,0,125)
    
    fill(14, 103, 41)     
    circle(0,0,853)
    
    
    
        
