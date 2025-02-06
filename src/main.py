import pygame 

#constants
background_colour = (0, 0, 0) 
WHITE = (255, 255, 255)

#main game
width, height = 900, 1050
margin = 20
placed = [0] * 9

coords1 = [0] * 9
y, index = (height/3)/2, 0
for i in range(3):
    x = (width/3)/2
    for j in range(3):
        coords1[index] = [x,y]
        x += ((width/3)/2)*2
        index += 1
    y += ((height/3)/2)*2

coords2= [0] * 9
y, w, index = margin, (height/3)-margin, 0
for i in range(3):
    x, z = margin, (width/3)-margin
    for j in range(3):
        coords2[index] = [[[x, y], [z, w]], [[z, y], [x, w]]]
        x += (width/3)
        z += (width/3)
        index += 1
    y += (height/3)
    w += (height/3)

limits = [0] * 9
z, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        limits[index] = [[x, x + (height/3)], [z, z + (height/3)]]
        x += (width/3)
        index += 1
    z += (height/3)

screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('Fortnite') 
screen.fill(background_colour) 

pygame.draw.line(screen, WHITE, (width/3,0), (width/3,height))
pygame.draw.line(screen, WHITE, ((width/3)*2,0), ((width/3)*2,height))
pygame.draw.line(screen, WHITE, (0,height/3), (width,height/3))
pygame.draw.line(screen, WHITE, (0,(height/3)*2), (width,(height/3)*2))

pygame.display.flip() 

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle(figure):
    pos=getPos()
    print(pos)
    for i in range(len(limits)):
        if (limits[i][0][0] < pos[0] < limits[i][0][1]) and (limits[i][1][0] < pos[1] < limits[i][1][1]) and (placed[i] == 0):
            if figure:
                pygame.draw.circle(screen, WHITE, coords1[i], (width/3-2*margin)/2, width=1)
                placed[i] = 1;
            else:
                pygame.draw.line(screen, WHITE, coords2[i][0][0], coords2[i][0][1])
                pygame.draw.line(screen, WHITE, coords2[i][1][0], coords2[i][1][1])
                placed[i] = 2;
            break

left_mouse_down = False
right_mouse_down = False
running = True

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_mouse_down = True
                drawCircle(True)
                pygame.display.update()
            if event.button == 3:
                right_mouse_down = True
                drawCircle(False)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_mouse_down = False
            if event.button == 3:
                 right_mouse_down = False

        if event.type == pygame.QUIT: 
            running = False