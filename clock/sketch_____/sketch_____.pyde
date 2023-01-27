def time_minute(x, y):
    fill(203, 33, 33)
    textSize(30)
    if minute() < 10:
        return text('0' + str(minute()), x, y)
    else:
        return text(str(minute()), x, y)


def time_year():
    a = str(year())
    b = a[2:]
    return b
    

def setup():
    size(400, 500)
    
    
def draw():
    background(0)
    
    noFill()
    strokeWeight(20)
    stroke(255, 255, 255, 50)
    ellipse(200, 250, 310, 310)
    
    strokeWeight(25)
    stroke(196, 36, 92, 150)
    ellipse(200, 250, 235, 235)
    stroke(196, 36, 92)
    arc(200, 250, 235, 235, 0, map(second(), 0, 59, 0, 2 * PI))
    
    strokeWeight(25)
    stroke(32, 227, 69, 150)
    ellipse(200, 250, 175, 175)
    stroke(32, 227, 69)
    arc(200, 250, 175, 175, 0, map(minute(), 0, 59, 0, 2 * PI))
    
    strokeWeight(25)
    stroke(46, 240, 238, 150)
    ellipse(200, 250, 115, 115)
    stroke(46, 240, 238)
    arc(200, 250, 115, 115, 0, map(hour(), 0, 23 , 0, PI * float(1.75)))
    
    strokeWeight(5)
    stroke(255)
    line(38, 250, 52, 250)
    line(362, 250, 348, 250)
    line(200, 88, 200, 102)
    line(200, 398, 200, 412)
    point(105, 127)
    point(57, 191)
    point(296, 127)
    point(343, 191)
    point(105, 373)
    point(57, 308)
    point(296, 373)
    point(343, 308)
    
    fill(180, 178, 178)
    noStroke()
    ellipse(70, 450, 40, 40)
    ellipse(330, 450, 40, 40)
    rect(70, 430, 260, 40)
    fill(225)
    ellipse(200, 250, 25, 25)
    fill(255, 5, 5)
    ellipse(200, 250, 15, 15)
    
    time_minute(130, 460) 
    text(str(hour()) + ":", 80, 460) 
    text(str(day()) + '.', 200, 460)
    text(str(month()) + '.', 250, 460)
    text(time_year(), 280, 460)
    
    
print(hour())
    
    
    
