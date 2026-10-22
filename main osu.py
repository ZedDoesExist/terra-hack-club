import pygame
import pygame_widgets
import random
import time
import sys

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
clickvalue = 1000
pluscost = 3000
#initialize pygame screen
pygame.init()
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("stupid stupid")
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
#arguments     (screen, x, y, width, height, min, max, step)
slider = Slider(screen, 650, 650, 500, 40, min=100, max=1200, step=50)
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
    700, 575,          # X and Y coordinates
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
    global clickvalue
    score = score + clickvalue * multi * diffx
    print(score)
    # Center position for the button's top-left corner.
    # Your button is 200 pixels wide and 100 pixels tall.
    center_x = CENTER_X - 100
    center_y = CENTER_Y - 50
    # Slider controls how far the button can move from the center.
    # Subtracting 100 makes the minimum slider value mean no movement.
    spread = int(slider.getValue()) - 100
    min_x = max(0, center_x - spread)
    max_x = min(WIDTH - 200, center_x + spread)
    min_y = max(50, center_y - spread // 2)
    max_y = min(575 - 100, center_y + spread // 2)
    button.setX(random.randint(min_x, max_x))
    button.setY(random.randint(min_y, max_y))

def plus():
    global score
    global clickvalue
    global pluscost
    if score >= pluscost:
        clickvalue += 500
        score -= pluscost
        pluscost *= 1.1
        pluscost = round(pluscost)
        buttonplus.setText(f'score per click {pluscost}')
#shop
def open_shop():
    global state
    state = "shop"
    button.hide()           # hide everything from the game screen
    slider.hide()
    slidertext.hide()
    shopbutton.hide()
    buttonplus.show()       # show everything from the shop screen
    buttonmulti.show()
    backbutton.show()

def close_shop():
    global state
    state = "game"
    buttonplus.hide()       # hide the shop
    buttonmulti.hide()
    backbutton.hide()
    button.show()           # bring the game back
    slider.show()
    slidertext.show()
    shopbutton.show()
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
shopbutton = Button(
    screen, 1250, 20, 220, 70,
    text='SHOP',
    fontSize=30,
    margin=20,
    inactiveColour=(60, 120, 220),
    hoverColour=(90, 150, 255),
    pressedColour=(50, 200, 50),
    onClick=open_shop
)

#buttons in shop
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
buttonplus = Button(
    screen,             # The surface to draw the button onto
    300, 600,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'score per click {pluscost}'),    # Text displayed inside the button
    fontSize=35,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=plus  # Function to trigger on click
)
backbutton = Button(
    screen, 600, 560, 300, 80,
    text='BACK',
    fontSize=30,
    margin=20,
    inactiveColour=(60, 120, 220),
    hoverColour=(90, 150, 255),
    pressedColour=(50, 200, 50),
    onClick=close_shop
)

close_shop()
#Main Game Loop
running = True

while running:
    #gather all system events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    diff = slider.getValue()
    diffx = slider.getValue() / 400
    scoretext.setText(f"Current Score: {score}")
    slidertext.setText(f"slider value: {diffx}")
    if score >= multicost:
        buttonmulti.inactiveColour=(50, 200, 50)
    else:
        buttonmulti.inactiveColour=(200, 50, 50)
    if score >= pluscost:
        buttonplus.inactiveColour=(50, 200, 50)
    else:
        buttonplus.inactiveColour=(200, 50, 50)
    #backround color
    screen.fill((255, 255, 255))

    #pass the events list to pygame_widgets to manage the button
    pygame_widgets.update(events)

    #updates the display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
