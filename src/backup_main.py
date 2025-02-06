import pygame 

#constants
background_colour = (0, 0, 0) 
WHITE = (255, 255, 255)

#variables declaration
width, height = 1200, 800
infowidth = 300
showinfo = True
showrf = True #r - ranks, f - files
rfmargin = 50
margin = 20

def drawInfo(showinfo, width, infowidth):
    if showinfo:
        return width - infowidth
    else:
        return width

def drawRF(showrf, gwidth, height, rfmargin):
    if showrf:
        return gwidth - rfmargin, height-rfmargin, rfmargin
    else:
        return gwidth,  height, 0

gwidth = drawInfo(showinfo, width, infowidth)
gwidth, gheight, rfmargin = drawRF(showrf, gwidth, height, rfmargin)

#array declarations
placed = [0] * 9

coords1 = [0] * 9
y, index = rfmargin, 0
for i in range(3):
    x = rfmargin
    for j in range(3):
        coords1[index] = [x,y]
        x += (gwidth-rfmargin)/3
        index += 1
    y += gheight/3

coords2= [0] * 9
y, w, index = margin+rfmargin, (gheight/3)-margin, 0
for i in range(3):
    x, z = margin+rfmargin, (gwidth/3)-margin
    for j in range(3):
        coords2[index] = [[[x, y], [z, w]], [[z, y], [x, w]]]
        x += (gwidth-rfmargin)/3
        z += (gwidth-rfmargin)/3
        index += 1
    y += (gheight/3)
    w += (gheight/3)

limits = [0] * 9
z, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        limits[index] = [[x, x + (gheight/3)], [z, z + (gheight/3)]]
        x += (gwidth/3)
        index += 1
    z += (gheight/3)

#game logic
def drawGame():
    pygame.draw.line(screen, WHITE, (gwidth/3, rfmargin), (gwidth/3, height))
    pygame.draw.line(screen, WHITE, ((gwidth/3)*2, rfmargin), ((gwidth/3)*2, height))
    pygame.draw.line(screen, WHITE, (rfmargin, height/3), (gwidth, height/3))
    pygame.draw.line(screen, WHITE, (rfmargin, (height/3)*2), (gwidth, (height/3)*2))
    if showinfo:
        pygame.draw.line(screen, WHITE, (gwidth, rfmargin), (gwidth, height))
    if showrf:
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        ranks = ["A", "B", "C"]
        files = ["1", "2", "3"]
        x = rfmargin + (gwidth/3)/2
        for i in range(len(ranks)):
            text_surface = my_font.render(ranks[i], False, WHITE)
            screen.blit(text_surface, (x, rfmargin/2))
            x += (gwidth/3)/2
        pygame.draw.line(screen, WHITE, (rfmargin, rfmargin), (gwidth, rfmargin))
        pygame.draw.line(screen, WHITE, (rfmargin, rfmargin), (rfmargin, height))

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawFigure(figure):
    pos=getPos()
    print(pos)
    for i in range(len(limits)):
        if (limits[i][0][0] < pos[0] < limits[i][0][1]) and (limits[i][1][0] < pos[1] < limits[i][1][1]) and (placed[i] == 0):
            if figure:
                pygame.draw.ellipse(screen, WHITE, (coords1[i][0]+margin, coords1[i][1]+margin, gwidth/3-margin*2-rfmargin, height/3-margin*2-rfmargin), width=1)
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