# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

# Define some colours
WHITE = (230, 230, 230)
YELLOW = (233, 215, 88)
BLACK = (57, 57, 58)
ORANGE = (255, 133, 82)
BLUE = (41, 115, 115)

SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

background = pygame.image.load("background.jpg")

fontTitle = pygame.font.Font('freesansbold.ttf', 55)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400, 100)   # place the centre of the text

fontSetting = pygame.font.Font('freesansbold.ttf', 55)
textSurfaceSetting = fontSetting.render('Settings', True, BLACK) 
textRectSetting = textSurfaceSetting.get_rect()
textRectSetting.center = (400, 100)   # place the centre of the text

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('2-Best-Elevator-Music-Royalty-Free.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)

class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=background, fg=BLACK, size=(175, 75), font_name="Gothic", font_size=35):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BLACK  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Hello!')

def my_shell_function2():
    """A generic function that prints something in the shell"""
    print('sound is ON')
    pygame.mixer.music.unpause()

def my_shell_function3():
    """A generic function that prints something in the shell"""
    print('sound is OFF')
    pygame.mixer.music.pause()

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_hello = Button("Hello", (SCREENWIDTH/2, SCREENHEIGHT*2/5), my_shell_function, bg=YELLOW)
button_back = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT*4/5), my_previous_function, bg=WHITE)
button_quit = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*4/5), my_quit_function, bg=ORANGE)
button_settings = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT*3/5), my_next_function, bg=BLUE)
button_soundOn = Button("Sound On", (SCREENWIDTH/2, SCREENHEIGHT*2/5), my_shell_function2, bg = YELLOW)
button_soundOff = Button("Sound Off", (SCREENWIDTH/2, SCREENHEIGHT*3/5), my_shell_function3, bg = ORANGE)

#arrange button groups depending on level
level1_buttons = [button_hello, button_quit, button_settings]
level2_buttons = [button_back,button_soundOn,button_soundOff ]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here


    # --- Draw code goes here

    # Clear the screen to white
    screen.blit(background, (0, 0))

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        screen.blit(textSurfaceTitle, textRectTitle)
    elif level == 2:
        for button in level2_buttons:
            button.draw()
        screen.blit(textSurfaceSetting, textRectSetting)

#Text

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

