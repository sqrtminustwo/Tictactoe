import pygame 

class Game():
    def __init__(self):
        self.placed = [0] * 9
        self.left_mouse_down = False
        self.right_mouse_down = False
        self.running = True

    def reset(self):
        self.placed = [0] * 9
        self.left_mouse_down = False
        self.right_mouse_down = False
        self.running = True

#constants
background_colour = (0, 0, 0) 
WHITE = (255, 255, 255)
game = Game()

#variables declaration
width, height = 800, 800
infowidth = 300
margin = 20

#array declarations
coords1 = [0] * 9
y, index = 0, 0
for i in range(3):
    x = 0
    for j in range(3):
        coords1[index] = [x,y]
        x += (width)/3
        index += 1
    y += height/3

coords2= [0] * 9
y, w, index = margin, (height/3)-margin, 0
for i in range(3):
    x, z = margin, (width/3)-margin
    for j in range(3):
        coords2[index] = [[[x, y], [z, w]], [[z, y], [x, w]]]
        x += (width)/3
        z += (width)/3
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

#game logic
def drawGame():
    pygame.draw.line(screen, WHITE, (width/3, 0), (width/3, height))
    pygame.draw.line(screen, WHITE, ((width/3)*2, 0), ((width/3)*2, height))
    pygame.draw.line(screen, WHITE, (0, height/3), (width, height/3))
    pygame.draw.line(screen, WHITE, (0, (height/3)*2), (width, (height/3)*2))

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def reset():
    screen.fill(background_colour)
    drawGame()
    pygame.display.flip()
    game.reset()


def won():
    # left upper to right bottom corner
    if game.placed[0] != 0 and game.placed[0] == game.placed[4] == game.placed[8]:
        return True
    # right upper to left bottom corner
    if game.placed[2] != 0 and game.placed[2] == game.placed[4] == game.placed[6]:
        return True
    #vertical lines check
    vert = 0
    while vert <= len(game.placed)-3:
        if game.placed[vert] != 0 and game.placed[vert] == game.placed[vert+1] == game.placed[vert+2]:
            return True
        vert += 3
    #horizontal lines check
    for i in range(0, 3):
        if game.placed[i] != 0 and game.placed[i] == game.placed[i+3] == game.placed[i+6]:
            return True
    return False

def drawFigure(figure, check=False):
    pos=getPos()
    for i in range(len(limits)):
        if (limits[i][0][0] < pos[0] < limits[i][0][1]) and (limits[i][1][0] < pos[1] < limits[i][1][1]) and (game.placed[i] == 0 or check):
            holder = game.placed[i]
            if figure:
                game.placed[i] = 1
                if not check:
                    pygame.draw.ellipse(screen, WHITE, (coords1[i][0]+margin, coords1[i][1]+margin, width/3-margin*2, height/3-margin*2), width=1)
            else:
                game.placed[i] = 2
                if not check:
                    pygame.draw.line(screen, WHITE, coords2[i][0][0], coords2[i][0][1])
                    pygame.draw.line(screen, WHITE, coords2[i][1][0], coords2[i][1][1])
            break
    print(game.placed)
    if won():
        if check:
            game.placed[i] = holder
            return True
        reset()
    else:
        if not check:
            if drawFigure(not figure, True):
                print("Blocked a win")
        else:
            game.placed[i] = holder if check else game.placed[i]
    return False

#game declaration
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('Fortnite') 
reset()

#game loop
while game.running:
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.left_mouse_down = True
                drawFigure(True)
                pygame.display.update()
            if event.button == 3:
                game.right_mouse_down = True
                drawFigure(False)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                game.left_mouse_down = False
            if event.button == 3:
                 game.right_mouse_down = False

        if event.type == pygame.QUIT: 
            game.running = False