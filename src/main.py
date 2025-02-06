import pygame 

#constants
background_colour = (0, 0, 0) 
WHITE = (255, 255, 255)

#variables declaration
width, height = 1400, 900
infowidth = 300
showinfo = False
margin = 20

def drawInfo(showinfo):
    if showinfo:
        return width - infowidth
    else:
        return width

gwidth = drawInfo(showinfo)

#array declarations
placed = [0] * 9

coords1 = [0] * 9
y, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        coords1[index] = [x,y]
        x += gwidth/3
        index += 1
    y += height/3

print(coords1)

coords2= [0] * 9
y, w, index = margin, (height/3)-margin, 0
for i in range(3):
    x, z = margin, (gwidth/3)-margin
    for j in range(3):
        coords2[index] = [[[x, y], [z, w]], [[z, y], [x, w]]]
        x += (gwidth/3)
        z += (gwidth/3)
        index += 1
    y += (height/3)
    w += (height/3)

limits = [0] * 9
z, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        limits[index] = [[x, x + (height/3)], [z, z + (height/3)]]
        x += (gwidth/3)
        index += 1
    z += (height/3)

#game logic
def drawGame():
    pygame.draw.line(screen, WHITE, (gwidth/3,0), (gwidth/3,height))
    pygame.draw.line(screen, WHITE, ((gwidth/3)*2,0), ((gwidth/3)*2,height))
    pygame.draw.line(screen, WHITE, (0,height/3), (gwidth,height/3))
    pygame.draw.line(screen, WHITE, (0,(height/3)*2), (gwidth,(height/3)*2))
    if showinfo:
        pygame.draw.line(screen, WHITE, (gwidth, 0), (gwidth, height))

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawFigure(figure):
    pos=getPos()
    print(pos)
    for i in range(len(limits)):
        if (limits[i][0][0] < pos[0] < limits[i][0][1]) and (limits[i][1][0] < pos[1] < limits[i][1][1]) and (placed[i] == 0):
            if figure:
                pygame.draw.ellipse(screen, WHITE, (coords1[i][0]+margin, coords1[i][1]+margin, gwidth/3-margin*2, height/3-margin*2), width=1)
                placed[i] = 1;
            else:
                pygame.draw.line(screen, WHITE, coords2[i][0][0], coords2[i][0][1])
                pygame.draw.line(screen, WHITE, coords2[i][1][0], coords2[i][1][1])
                placed[i] = 2;
            break

#game declaration
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('Fortnite') 
screen.fill(background_colour) 
drawGame()
pygame.display.flip() 

#game loop
left_mouse_down = False
right_mouse_down = False
running = True

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_mouse_down = True
                drawFigure(True)
                pygame.display.update()
            if event.button == 3:
                right_mouse_down = True
                drawFigure(False)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_mouse_down = False
            if event.button == 3:
                 right_mouse_down = False

        if event.type == pygame.QUIT: 
            running = False