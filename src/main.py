import pygame 

background_colour = (0, 0, 0) 
WHITE = (255, 255, 255)
placed = [0] * 9

#main game
placed = [0] * 9

coords1 = [0] * 9
y, index = 133, 0
for i in range(3):
    x = 133
    for j in range(3):
        coords1[index] = [x,y]
        x += 133*2
        index += 1
    y += 133*2

coords2= [0] * 9
y, w, index = 20, 246, 0
for i in range(3):
    x, z = 20, 246
    for j in range(3):
        coords2[index] = [[[x, y], [z, w]], [[z, y], [x, w]]]
        x += 266
        z += 266
        index += 1
    y += 266
    w += 266

limits = [0] * 9
z, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        limits[index] = [[x, x + 266], [z, z + 266]]
        x += 266
        index += 1
    z += 266

screen = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('Fortnite') 
screen.fill(background_colour) 

pygame.draw.line(screen, WHITE, (266,0), (266,800))
pygame.draw.line(screen, WHITE, (532,0), (532,800))
pygame.draw.line(screen, WHITE, (0,266), (800,266))
pygame.draw.line(screen, WHITE, (0,532), (800,532))

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
                pygame.draw.circle(screen, WHITE, coords1[i], 125, width=1)
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