def setup():
    size(500, 500)
    colorMode(HSB)


def draw():
    background(0)
    noStroke()
    #x1, y1, w, h

    num_cols = 25
    gap = width / float(num_cols)
    cgap = 255 / float(num_cols)
    noStroke()
    for i in range(num_cols):
        x = gap * i
        c = cgap * i
        fill(c, 90, c)
        rect(x, 0, gap, height)

    num_circles = 10
    gap = width / float(num_circles)
    rad = gap / 2
    rad = gap / 2
    cgap = 50
    start_c = 1
    for i in range(num_circles):
        x = rad + (gap * i)
        c = start_c + (i * cgap) % 256
        fill(c, 255, 255)
        circle(x, height / 2, gap)
