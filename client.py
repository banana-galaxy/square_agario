#TODO       2D list for food and food, make square move directly & smoothly to mouse, make square loose size over time, add multiplayer

import pygame, random, numpy
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
food_color = (110, 158, 255)
previous_speed_x = 0.0
previous_speed_y = 0.0
window_size_x = 2000
window_size_y = 2000

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (window_size_x, window_size_y)
screen = pygame.display.set_mode(size)
square_x_size = 50
square_y_size = 50
food_x_size = 15
food_y_size = 15
 
pygame.display.set_caption("squareio")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# creating list of food locations
food = []
for i in range(20):
    food_x = random.randrange(window_size_x)
    food_y = random.randrange(window_size_y)
    food.append([food_x, food_y])

# objects class
class object():
    def __init__(self):
        self.x = 1
        self.y = 1
        self.length = 0
        self.height = 0

    def size_update(self, x, y):
        self.length = x
        self.height = y

    def position_update(self, x, y):
        self.x = x - (self.length / 2)
        self.y = y - (self.height / 2)

    def draw(self):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.length, self.height], 0)

    def position_return(self):
        return self.x, self.y

    def size_return(self):
        return self.length, self.height

    def center_return(self):
        x = self.x + (self.length / 2)
        y = self.y + (self.height / 2)
        return x, y

    def wall_collide(self):
        if self.x > window_size_x - self.length:
            self.x = window_size_x - self.length
        elif self.x < 0:
            self.x = 0
        if self.y > window_size_y - self.height:
            self.y = window_size_y - self.height
        elif self.y < 0:
            self.y = 0

    def food_collide(self):
        for i in range(len(food)):
            if self.x + self.length >= food[i][0] and self.x <= food[i][0] + food_x_size:
                if self.y + self.height >= food[i][1] and self.y <= food[i][1] + food_y_size:
                    food.remove(food[i])
                    self.height += 1
                    self.length += 1
                    fod_x = random.randrange(window_size_x)
                    fod_y = random.randrange(window_size_y)
                    food.append([fod_x, fod_y])



square = object()

square.size_update(50, 50)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    #pygame.mouse.set_visible(False)

    #print str(square.position_return())

    #updating square size
    '''if x > 600:
        square_x_size += 1
        square_y_size += 1
        square.size_update(square_x_size, square_y_size)
    else:
        square.size_update(square_x_size, square_y_size)'''

    #updating square position based 10% off mouse distance from square
    
    # F=ma A=f/m    speed = force    mass = whatever I assign

    distance_x = x - square.center_return()[0]
    distance_y = y - square.center_return()[1]
    new_speed_x = distance_x / 50.0
    new_speed_y = distance_y / 50.0
    speed_change_x = new_speed_x - previous_speed_x
    speed_change_y = new_speed_y - previous_speed_y
    speed_x = previous_speed_x + (speed_change_x * 0.02)
    speed_y = previous_speed_y + (speed_change_y * 0.02)

    if speed_y > 7:
        speed_y = 7.0
    elif speed_y < -7:
        speed_y = -7.0

    if speed_x > 7:
        speed_x = 7.0
    elif speed_x < -7:
        speed_x = -7.0

    #print (speed_x, speed_y)



    previous_speed_x = speed_x
    previous_speed_y = speed_y

    square_x = speed_x + square.center_return()[0]
    square_y = speed_y + square.center_return()[1]

    square.position_update(square_x, square_y)
    square.wall_collide()
    square.food_collide()
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    square.draw()
    for i in range(len(food)):
        pygame.draw.rect(screen, food_color, [food[i][0], food[i][1], food_x_size, food_y_size], 0)
    #pygame.draw.line(screen, GREEN, [square.center_return()[0], square.center_return()[1]], [square.center_return()[0] + (speed_x * 10), square.center_return()[1] + (speed_y * 10)], 5)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
