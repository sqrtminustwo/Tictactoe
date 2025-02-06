import pygame 

background_colour = (234, 212, 252) 
WHITE = (255, 255, 255)
placed = [0] * 9

#todo: function that returns coordinates
coords1 = [[133, 133], [399, 133], [665, 133],
          [133, 399], [399, 399], [665, 399], 
          [133, 665], [399, 665], [665, 665]] 

coords2 = [[[[20, 20], [246, 246]], [[246, 20], [20, 246]]], [[[286, 20], [512, 246]], [[512, 20], [286, 246]]], [[[552, 20], [778, 246]], [[778, 20], [552, 246]]],
           [[[20, 286], [246, 512]], [[246, 286], [20, 512]]], [[[286, 286], [512, 512]], [[512, 286], [286, 512]]], [[[552, 286], [778, 512]], [[778, 286], [552, 512]]],
           [[[20, 552], [246, 778]], [[246, 552], [20, 778]]], [[[286, 552], [512, 778]], [[512, 552], [286, 778]]], [[[552, 552], [778, 778]], [[778, 552], [552, 778]]]]

limits = [[[0, 266], [0, 266]], [[266, 532], [0, 266]], [[532, 800], [0, 266]],
          [[0, 266], [266, 532]], [[266, 532], [266, 532]], [[532, 800], [266, 532]],
          [[0, 266], [532, 800]], [[266, 532], [532, 800]], [[532, 800], [532, 800]]]

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