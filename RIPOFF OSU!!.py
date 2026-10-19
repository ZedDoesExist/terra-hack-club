import pygame
import pygame_widgets
import random
import time

from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.dropdown import Dropdown
#variables
scoredisplay = TextBox
clock = pygame.time.Clock()
score = 0
hold_time = 1000
multicost = 10000
multi = 1
#initialize pygame screen
pygame.init()
screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("stupid stupid")
#arguments     (screen, x, y, width, height, min, max, step)
slider = Slider(screen, 100, 100, 500, 40, min=100, max=1200, step=50)
diff = slider.getValue()
diffy = int(diff / 2)
scoretext = TextBox(
    screen, 
    0, 0,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
slidertext = TextBox(
    screen, 
    200, 150,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
scoretext.setText(f"Current Score: {score}")
scoretext.disable()
slidertext.disable()
#functions on clicks
def multiplier():
    global multi
    global score
    global multicost
    global buttonmulti
    if score >= multicost:
        multi = multi + 1
        score = score - multicost
        multicost = multicost * 3
        buttonmulti.setText(f'multiply costs {multicost}')
        scoretext.setText(f"Current Score: {score}")        

def click():
    global score
    global multi
    global scoretext
    global diff
    global diffx
    score = score + 1000 * multi * diffx
    print(score)
    randomx = random.randint(100,diff)
    randomy = random.randint(0,diffy)
    button.setX(randomx)
    button.setY(randomy)

def sps():
    global score
#buttons
button = Button(
    screen,             # The surface to draw the button onto
    400, 250,           # X and Y coordinates (top-left corner)
    200, 100,           # Width and Height of the button
    fontSize=30,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=click    # Function to trigger on click
)
buttonmulti = Button(
    screen,             # The surface to draw the button onto
    0, 600,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'multiply costs {multicost}'),    # Text displayed inside the button
    fontSize=35,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=multiplier  # Function to trigger on click
)
'''buttonsps = Button(
    screen,             # The surface to draw the button onto
    50, 400,           # X and Y coordinates (top-left corner)
    200, 100,           # Width and Height of the button
    text='score per second',    # Text displayed inside the button
    fontSize=30,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=sps  # Function to trigger on click
)'''
#Main Game Loop
running = True

while running:
    #gather all system events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    diff = slider.getValue()
    diffx = slider.getValue() / 200
    scoretext.setText(f"Current Score: {score}")
    slidertext.setText(f"slider value: {diffx}")
    
    #backround color
    screen.fill((255, 255, 255))

    #pass the events list to pygame_widgets to manage the button
    pygame_widgets.update(events)

    #updates the display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
