#pygame is imported primarily for visual aspects,
import pygame
import sys
#pymunk is for the pyhsics
import pymunk

pygame.init()

width = 1800
height = 1000
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("Greedy Gladiator")
fps = 60

clock = pygame.time.Clock()

def running():
    """
    This function runs the game in active time.

    Input:
    None

    Output:
    None
    """
    #setting variables to be changed
    circ_x_loc = (width / 2)
    circ_y_loc = (height / 2)

    while True:
        events = pygame.event.get()
        w,a,s,d = movement()
        #this sets  the framerate at whatever fps is set to
        clock.tick(fps)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        #speed = dist that circle moves each frame when wasd is used
        speed = 3
        horiz = 0
        vert = 0
        radius = 25

        body_position = physics(radius, circ_x_loc, circ_y_loc)
        #sets new location of circle based on key input
        if w:
            vert = speed
        if a:
            horiz = -speed
        if s:
            vert = -speed
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

        body_x, body_y = coordinate_conversion(body_position)

        screen.fill("salmon")
        pygame.draw.circle(screen, "black", (int(body_x), int(body_y)), radius)

        pygame.display.update()

def physics(radius, circ_x_loc, circ_y_loc):
    """
    Gives us the stuff needed for physics.

    Input:
    None

    Output:
    body_position (tuple)
    """
    # this holds any objects that are wanted in the physics simulation
    space = pymunk.Space()

    # velocities depend on step size to update position of object
    space.step(1 / fps)

    body = pymunk.Body()
    body_position = circ_x_loc, circ_y_loc
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)

    #setting attributes...
    shape.density = 1
    space.gravity = 0, -1000
    return body_position

def coordinate_conversion(point):
    """
    Returns a version of a point on a 2D plane so that the y-value is the opposite.
    This is done because pygame defines (0,0) at the top left of the screen,
    while pymunk defines it at the bottom left. This will fix this mismatch.

    Input:
    point (tuple)

    Output:
    new_x (float)
    new_y (float)
    """
    new_x = point[0]
    new_y = height-point[1]
    return new_x, new_y

def movement():
    """
    This function checks to see if the user is actively pressing any wasd keys or not.
    Input:
    None

    Output:
    active_w (boolean)
    active_a (boolean)
    active_s (boolean)
    active_d (boolean)
    """
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