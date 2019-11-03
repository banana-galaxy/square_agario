'''    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")'''

'''    def food_screen_range(self):
        for i in range(len(self.food)):
            if self.food[i][0] > self.screen_width:
                self.food.remove(self.food[i])
                fod_x = random.randrange(self.screen_width)
                fod_y = random.randrange(self.screen_height)
                self.food.append([fod_x, fod_y])
            if self.food[i][1] > self.screen_height:
                self.food.remove(self.food[i])
                fod_x = random.randrange(self.screen_width)
                fod_y = random.randrange(self.screen_height)
                self.food.append([fod_x, fod_y])'''

"""
Platformer Game
"""
import arcade, random

# Constants
screen_width = 1000
screen_height = 1000
SCREEN_TITLE = "squareio arcade"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (186, 186, 186)
food_color = (110, 158, 255)


# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(screen_width, screen_height, SCREEN_TITLE, resizable=True)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        self.x = 750
        self.y = 750
        self.square_width = 15
        self.square_height = 15
        self.square_color = BLACK
        self.previous_speed_x = 0.0
        self.previous_speed_y = 0.0
        self.mouse_x = 0
        self.mouse_y = 0
        self.speed_limit = 9.0
        self.food = []
        self.food_size = 10
        self.total_time = 0.0
        self.yes = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = 3000
        self.map_height = 3000
        self.map_location_x = 0
        self.map_location_y = 0
        self.border_thickness = 3000
        self.pause = False
        for i in range(50):
            food_x = random.randint(50, self.map_width-50)
            food_y = random.randint(50, self.map_height-50)
            self.food.append([food_x, food_y])

        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        pass

    def on_resize(self, width, height):
            """ This method is automatically called when the window is resized. """

            # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
            # edges being -1 to 1.
            super().on_resize(width, height)
            self.screen_width = width
            self.screen_height = height

            print(f"Window resized to: {width}, {height}")

    '''def food_screen_range(self):
            for i in range(len(self.food)):
                if self.food[i][0] > self.screen_width:
                    self.food.remove(self.food[i])
                    fod_x = random.randrange(self.screen_width)
                    fod_y = random.randrange(self.screen_height)
                    self.food.append([fod_x, fod_y])
                if self.food[i][1] > self.screen_height:
                    self.food.remove(self.food[i])
                    fod_x = random.randrange(self.screen_width)
                    fod_y = random.randrange(self.screen_height)
                    self.food.append([fod_x, fod_y])'''

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        arcade.draw_rectangle_filled(self.map_width / 2 - self.x, -self.border_thickness/2 - self.y, self.map_width*2, self.border_thickness, GREY)
        arcade.draw_rectangle_filled(self.map_width / 2 - self.x, self.map_height+self.border_thickness/2 - self.y, self.map_width*2, self.border_thickness, GREY)
        arcade.draw_rectangle_filled(-self.border_thickness/2 - self.x, self.map_height / 2 - self.y, self.border_thickness, self.map_height*2, GREY)
        arcade.draw_rectangle_filled(self.map_height+self.border_thickness/2 - self.x, self.map_height / 2 - self.y, self.border_thickness, self.map_height*2, GREY)

        arcade.draw_rectangle_filled(self.screen_width/2, self.screen_height/2, self.square_width, self.square_height, self.square_color)
        #print(self.x, self.y)
        #print(screen_width/2-self.x, screen_height/2-self.y)
        for i in range(len(self.food)):
            arcade.draw_rectangle_filled(self.food[i][0]-self.x, self.food[i][1]-self.y, self.food_size, self.food_size, food_color)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""

        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        #print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.square_color = GREEN

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.square_color = BLACK

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.P:
            if self.pause:
                self.pause = False
            else:
                self.pause = True

    def wall_collide(self):
        if self.x > (self.map_width - self.screen_width/2):
            self.x = self.map_width - self.screen_width/2
        elif self.x < 0 - self.screen_width/2:
            self.x = 0 - self.screen_width/2
        if self.y > self.map_height - self.screen_height/2:
            self.y = self.map_height - self.screen_height/2
        elif self.y < 0 - self.screen_height/2:
            self.y = 0 - self.screen_height/2

        '''if self.x > self.screen_width - self.square_width/2:
            self.x = self.screen_width - self.square_width/2
        elif self.x < 0 + self.square_width/2:
            self.x = 0 + self.square_width/2
        if self.y > self.screen_height - self.square_height/2:
            self.y = self.screen_height - self.square_height/2
        elif self.y < 0 + self.square_height/2:
            self.y = 0 + self.square_height/2'''

    def food_collide(self):
        square_right_edge = self.x + (self.square_width/2)
        square_left_edge = self.x - (self.square_width/2)
        square_bottom_edge = self.y + (self.square_height/2)
        square_top_edge = self.y - (self.square_height/2)

        for i in range(len(self.food)):
            food_right_edge = self.food[i][0] + (self.food_size/2)
            food_left_edge = self.food[i][0] - (self.food_size/2)
            food_bottom_edge = self.food[i][1] + (self.food_size/2)
            food_top_edge = self.food[i][1] - (self.food_size/2)

            if square_right_edge >= food_left_edge and square_left_edge <= food_right_edge:
                if square_bottom_edge >= food_top_edge and square_top_edge <= food_bottom_edge:
                    self.food.remove(self.food[i])
                    self.square_height += 1
                    self.square_width += 1
                    fod_x = random.randint(50, SCREEN_WIDTH-50)
                    fod_y = random.randint(50, SCREEN_HEIGHT-50)
                    self.food.append([fod_x, fod_y])

    def eat_food(self):
        collision = self.collide([[self.screen_width/2, self.screen_height/2]], self.square_height, self.food, self.food_size)
        if isinstance(collision, list):
            for i in range(len(collision)):
                self.food.remove(collision[i])
                self.square_height += 1
                self.square_width += 1
                while True:
                    fod_x = random.randint(50, self.map_width - 50)
                    fod_y = random.randint(50, self.map_height - 50)
                    collided = self.object_collide([self.screen_width/2, self.screen_height/2], self.square_height, [fod_x, fod_y], self.food_size)
                    if collided:
                        continue
                    else:
                        break
                self.food.append([fod_x, fod_y])

    def collide(self, coordinates1: list, coordinates1_size: int, coordinates2: list, coordinates2_size: int):
        collided_with = []
        collided = False
        for coord1 in range(len(coordinates1)):
            for coord2 in range(len(coordinates2)):
                if coordinates1[coord1][0] + coordinates1_size/2 >= (coordinates2[coord2][0]-self.x) - coordinates2_size/2 and coordinates1[coord1][0] - coordinates1_size/2 <= (coordinates2[coord2][0]-self.x) + coordinates2_size/2:
                    if coordinates1[coord1][1] + coordinates1_size/2 >= (coordinates2[coord2][1]-self.y) - coordinates2_size/2 and coordinates1[coord1][1] - coordinates1_size/2 <= (coordinates2[coord2][1]-self.y) + coordinates2_size/2:
                        collided_with.append(coordinates2[coord2])
                        collided = True
        if collided:
            return collided_with
        else:
            return False

    def object_collide(self, coordinates1: list, coordinates1_size: int, coordinates2: list, coordinates2_size: int):
        if coordinates1[0] + coordinates1_size / 2 >= (coordinates2[0]-self.x) - coordinates2_size / 2 and coordinates1[0] - coordinates1_size / 2 <= (coordinates2[0]-self.x) + coordinates2_size / 2:
            if coordinates1[1] + coordinates1_size / 2 >= (coordinates2[1]-self.y) - coordinates2_size / 2 and coordinates1[1] - coordinates1_size / 2 <= (coordinates2[1]-self.y) + coordinates2_size / 2:
                return True
            else:
                return False


    def on_update(self, delta_time: float):
        # square moving logic
        if not self.pause:
            distance_x = self.mouse_x - self.screen_width/2
            distance_y = self.mouse_y - self.screen_height/2
            new_speed_x = distance_x / 50.0
            new_speed_y = distance_y / 50.0
            speed_change_x = new_speed_x - self.previous_speed_x
            speed_change_y = new_speed_y - self.previous_speed_y
            speed_x = self.previous_speed_x + (speed_change_x * 0.03)
            speed_y = self.previous_speed_y + (speed_change_y * 0.03)

            if speed_y > self.speed_limit:
                speed_y = self.speed_limit
            elif speed_y < -self.speed_limit:
                speed_y = -self.speed_limit

            if speed_x > self.speed_limit:
                speed_x = self.speed_limit
            elif speed_x < -self.speed_limit:
                speed_x = -self.speed_limit

            #print (speed_x, speed_y)

            self.previous_speed_x = speed_x
            self.previous_speed_y = speed_y

            self.x = speed_x + self.x
            self.y = speed_y + self.y
            self.wall_collide()
            #self.food_screen_range()
            self.eat_food()
        '''self.total_time = self.total_time + delta_time
        print("time:", self.total_time)
        test = int(self.total_time%5)
        if test == 0:
            self.yes = True
        if self.yes:
            print("test equals 0")
        print("test:", test)
        print("square size:", self.square_width, self.square_height)'''


def main():
    """ Main method """
    window = Game()
    window.setup()
    arcade.run()

    '''window = arcade.Window()
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()'''


if __name__ == "__main__":
    main()
