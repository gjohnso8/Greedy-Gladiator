import pygame
import sys

def settings():
    '''
    Sets all game parameters.

    Input:
    None

    Output:
    width (int)
    height (int)
    screen
    caption

    :return:
    '''
    width = 1800
    height = 1000
    screen = pygame.display.set_mode((width, height))
    caption = pygame.display.set_caption("Greedy Gladiator")
    return width, height, screen, caption

width, height, screen, caption = settings()
pygame.init()

def running():
    '''
    This function runs the game in active time.

    Input:
    None

    Output:
    None
    '''
    #setting variables to be changed
    done = 1

    circ_x_loc = (width / 2)
    circ_y_loc = (height / 2)

    while done == 1:
        events = pygame.event.get()
        w,a,s,d = movement()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done = 0



        #speed = dist that circle moves each frame when wasd used
        speed = 0.5
        horiz = 0
        vert = 0
        #sets new location of circle based on key input
        if w:
            vert = -speed
        if a:
            horiz = -speed
        if s:
            vert = speed
        if d:
            horiz = speed

        circ_x_loc += horiz
        circ_y_loc += vert

        #this section does the pacman thing where it goes to the other side of the screen
        if circ_x_loc == 0:
            circ_x_loc = width-1
        if circ_x_loc == width:
            circ_x_loc = 1
        if circ_y_loc == 0:
            circ_y_loc = height-1
        if circ_y_loc == height:
            circ_y_loc = 1

        screen.fill("salmon")
        pygame.draw.circle(screen, "black", (circ_x_loc, circ_y_loc), 25)

        pygame.display.update()

def movement():
    '''
    This function checks to see if the user is actively pressing any wasd keys or not.
    Input:
    None

    Output:
    active_w (boolean)
    active_a (boolean)
    active_s (boolean)
    active_d (boolean)
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        active_w = True
    else:
        active_w = False
    if keys[pygame.K_a]:
        active_a = True
    else:
        active_a = False
    if keys[pygame.K_s]:
        active_s = True
    else:
        active_s = False
    if keys[pygame.K_d]:
        active_d = True
    else:
        active_d = False
    return active_w, active_a, active_s, active_d

running()