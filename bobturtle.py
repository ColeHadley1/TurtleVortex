import turtle

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

    multi = int(ts.numinput("Multiplier", "Enter Multiplier: "))
    modulus = int(ts.numinput("Modulus", "Enter Modulus: "))
    print(multi)
    print(modulus)
    #multi = int(input("Enter Multiplier: ")) 97
    #modulus = int(input("Enter Modulus: ")) 168

    r = 300
    dots = modulus
    arcAngle = 360 / dots
    dictX = {}
    dictY = {}

    bob.speed(0)
    bob.penup()
    bob.setpos(0, r)
    bob.pendown()
    bob.setheading(180)

    for i in range(dots):
        bob.circle(r, -arcAngle)
        #bob.dot()
        dictX[i+1] = float(bob.xcor())
        dictY[i+1] = float(bob.ycor())

    start = 1
    usedlist = []
    path = vortexV2(multi, modulus, start, usedlist)
    numlist = []

    for i in range(len(path)):
        usedlist.append(path[i])
    for i in range(modulus - 1):
        numlist.append(i + 1)

    bob.penup()
    bob.setpos(dictX[path[0]], dictY[path[0]])
    bob.pendown()
    for i in range(1, len(path) + 1):
        bob.setpos(dictX[path[i - 1]], dictY[path[i - 1]])

    while len(numlist) != 0:
        numlist = listshort(path, numlist)
        if len(numlist) == 0:
            break
        start = numlist[0]
        path = vortexV2(multi, modulus, start, usedlist)
        for i in range(len(path)):
            usedlist.append(path[i])
        bob.penup()
        bob.setpos(dictX[path[0]], dictY[path[0]])
        bob.pendown()
        for i in range(1, len(path) + 1):
            bob.setpos(dictX[path[i - 1]], dictY[path[i - 1]])

    bob.hideturtle()
    #ts.getcanvas().postscript(file="vortex.eps")
    turtle.done()

main()