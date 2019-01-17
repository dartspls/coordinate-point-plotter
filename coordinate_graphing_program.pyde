 # this class lets us make coordinate objects and store them in a list
class Coordinate:
    # coordinate point config variables
    rad = 10 # point radius
    topMargin = 20 # how far above the point text is drawn
    lrMargin = 60 # minimum distance from edge before text alignment is changed
    
    def __init__(self, x, y):
        # could use PVectors here too, be more to type though
        self.x = x
        self.y = y
        
    # method to draw a small circle with a label above it containing the xy coordinates as well as the # the point is (optional, 0 = disabled)
    def drawDot(self, dotNum = 0):
        stroke(0)
        fill(255)
        ellipse(self.x, self.y, self.rad, self.rad) # drawing the point
        
        textY = self.y - self.topMargin
            
        word = "X: " + str(int(self.x)) + ", " + "Y: " + str(int(self.y)) # creating the string we will draw above the point
        textAlign(CENTER, CENTER)
        fill(0)
        stroke(255)
        
        # check if the text would be off screen and move accordingly
        if self.y - self.topMargin < 0:
            textY = self.y + self.topMargin
        if self.x + self.lrMargin > width:
            textAlign(RIGHT, CENTER)
        elif self.x - self.lrMargin < 0:
            textAlign(LEFT, CENTER)

        # the dotNum argument is optional, if none is given it will default to 0 and we won't draw a number next to the points
        if dotNum == 0:
            text(word, self.x, textY)
        else: # else draw the point's number
            word += ", #" + str(dotNum) # join dotNum with the existing string.
            text(word, self.x, textY)

points = [] # list of points
# app config variables that can be changed in-app
mode = True # mode True means clicking adds a point to the coordinate graph, False means clicking a point will remove it
drawLine = False # draw lines between points
snap = False # when enabled, points snap to nearest 10
drawGraph = True # draw graph lines
buttonTextPos = None
buttonYPos = None

def setup():
    size(800, 650) # buttons take up a 50 pixel area at the bottom of the screen, so add 50 pixels to your desired screen height
    background(255)
    frameRate(30)
    global buttonYPos, buttonTextPos
    # height is defined here so need to define vars based on it here too
    buttonYPos = height - 50 
    buttonTextPos = height - 25
    



def draw():
    background(255)
    if drawGraph:
        # draw verticle lines
        for i in range(0, width, 10):
            stroke(190)
            line(i, 0, i, height - 50)
    
        # draw horizontal lines
        for i in range(0, height - 49, 10): # -49 so it draws the last line at the bottom
            stroke(190)
            line(0, i, width, i)
    
    # loop through our array and call the drawDot method on each, we pass in in the index + 1 (index starts from 0, and remember 0 = disabled in the method) to number each point
    for i in range(len(points)):
        points[i].drawDot(i + 1)

    if drawLine:
        stroke(0)
        for i in range(1, len(points)):
            line(points[i -1].x, points[i - 1].y, points[i].x, points[i].y)
    
    drawButtons()
    

def mousePressed():
    # whenever the mouse is pressed, first check if we clicked on the button    
    checkButtons(mouseX, mouseY)
    
    # if the program is in Add mode and we clicked within the coordinate graph, add an entry to the array
    if mode == True and mouseY < height - 50:
        x = mouseX
        y = mouseY
        if snap:
            x = round(x * 2, -1) / 2
            y = round(y * 2, -1) / 2
        points.append(Coordinate(x, y))
    else:
        for i in range(len(points)): # if in remove mode then loop through array and check if we clicked inside one of the points
            if dist(mouseX, mouseY, points[i].x, points[i].y) < 5:
                points.pop(i) # remove entry at the given index (position)
                return
            

    
def drawButtons():
    # draw a gray rectangle at the bottom margin of the screen to place buttons on
    fill(150)
    noStroke()
    rect(0, buttonYPos, width, 50)
    textAlign(LEFT)
    
    # draw "toggle add/remove" button
    if mode:
        fill(0, 255, 0)
        text("Mode: Add", 55, buttonTextPos)
    else:
        fill(255, 0, 0)
        text("Mode: Remove", 55, buttonTextPos)
    rect(0, buttonYPos, 50, 50)
    
    # draw "remove all" button
    fill(255, 0, 0)
    rect(150, buttonYPos, 50, 50)
    text("Remove all", 205, buttonTextPos)
    
    # draw "toggle lines" button
    if drawLine:
        fill(0, 255, 0)
    text("Draw lines", 355, buttonTextPos)
    rect(300, buttonYPos, 50, 50)
    
    # draw "toggle snap" button
    if snap:
        fill(0, 255, 0)
    else:
        fill(255, 0, 0)
    text("Snap points", 505, buttonTextPos)
    rect(450, buttonYPos, 50, 50)
    
    # draw "toggle graph" button
    if drawGraph:
        fill(0, 255, 0)
    else:
        fill(255, 0, 0)
    text("Graph paper mode", 655, buttonTextPos)
    rect(600, buttonYPos, 50, 50)
    
def checkButtons(x, y):
    if x < 50 and y > buttonYPos:
        # toggle mode
        global mode
        mode = not mode
        return
    elif x > 150 and x < 200 and y > buttonYPos:
        del points[:] # delete all objects in array (list.clear() isn't in this version of python)
        return
    elif x > 300 and x < 350 and y > buttonYPos:
        global drawLine
        drawLine = not drawLine
    elif x > 450 and x < 500 and y > buttonYPos:
        global snap
        snap = not snap
    elif x > 600 and x < 650 and y > buttonYPos:
        global drawGraph
        drawGraph = not drawGraph
    
    
    
    
    
    
