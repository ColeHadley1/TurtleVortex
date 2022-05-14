import turtle
#test1
#creates the path list
def vortexV2(multi, modulus, x, usedlist):
    path = [x]
    answer = 0
    i = 0
    while answer == 0:
        hold = path[i] * multi
        if hold > modulus:
            hold = hold % modulus
            if hold == 0:
                path.append(modulus)
                break
        if hold in path:
            path.append(hold)
            break
        path.append(hold)
        if hold in usedlist:
            break
        i += 1
    return path

#removes path positions that have been used
def listshort(path, numlist):
    functionlist = numlist.copy()
    for i in range(len(path)):
        if path[i] in functionlist:
            functionlist.remove(path[i])
    return functionlist

def main():
    bob = turtle.Turtle()
    ts = bob.getscreen()
    ts.bgcolor("#c0eaf2")

    #sets the multiplier, modulus, radius, and increments of the circle
    multi = int(ts.numinput("Multiplier", "Enter Multiplier: "))
    modulus = int(ts.numinput("Modulus", "Enter Modulus: "))
    radius = 300
    arcAngle = 360 / modulus
    #dictionary to store positions along the circle
    dictX = {}
    dictY = {}

    bob.speed(0)
    bob.penup()
    bob.setpos(0, radius)
    bob.pendown()
    bob.setheading(180)
    #draws circle and saves positons
    for i in range(modulus):
        bob.circle(radius, -arcAngle)
        dictX[i+1] = float(bob.xcor())
        dictY[i+1] = float(bob.ycor())

    usedlist = []   #keeps track of path values used
    numlist = []    #keep track of numbers not used yet
    for i in range(modulus - 1):
        numlist.append(i + 1)

    #creates all the loops in the vortex
    while len(numlist) != 0:
        start = numlist[0]
        path = vortexV2(multi, modulus, start, usedlist)
        for i in range(len(path)):
            usedlist.append(path[i])
        bob.penup()
        bob.setpos(dictX[path[0]], dictY[path[0]])
        bob.pendown()
        for i in range(1, len(path) + 1):
            bob.setpos(dictX[path[i - 1]], dictY[path[i - 1]])
        numlist = listshort(path, numlist)

    bob.hideturtle()
    #ts.getcanvas().postscript(file="vortex.eps")
    turtle.done()

main()
