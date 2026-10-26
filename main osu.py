import pygame
import pygame_widgets
import random
import time
import sys
#missed the first 2 days cause i was having a depressive episode
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.dropdown import Dropdown
#variables
scoredisplay = TextBox
clock = pygame.time.Clock()
button_size = 100
multibonus = 1
plusbonus = 1
spsbonus = 1
spsadd = 0
second = 0.0
score = 0
hold_time = 1000
multicost = 10000
multi = 1
pluscost = 3000
spscost = 3000
plusbonuscost = 1000000
spsbonuscost = 1000000
multibonuscost = 1000000
critbonusscore = 1000000
plusneeded = 25
multineeded = 25
spsneeded = 25
critrateneeded = 25
pluscount = 0
spscount = 0
multicount = 0
rngsize = False
rngsizevalue = 1
critrate = 0
critratecost = 10000
critratemulti = 1
crithit = 1
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
multiownedtext = TextBox(
    screen, 
    0, 50,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
critratetext = TextBox(
    screen, 
    400, 50,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
critratemultitext = TextBox(
    screen, 
    800, 50,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
plusownedtext = TextBox(
    screen, 
    400, 0,          # X and Y coordinates
    400, 50,           # Width and Height of the box
    fontSize=30,
    borderColour=(255, 255, 255),  # Hide the border by making it white
    textColour=(0, 0, 0)           # Black text color
)
spsownedtext = TextBox(
    screen, 
    800, 0,          # X and Y coordinates
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
spsownedtext.setText(f"score per second owned: {spscount}")
multiownedtext.setText(f"multiplier owned: {multicount}")
critratetext.setText(f"crit rate {critrate}/100")
critratemultitext.setText(f"multiplier owned: {multicount}")
scoretext.disable()
slidertext.disable()
plusownedtext.disable()
spsownedtext.disable()
multiownedtext.disable()
critratemultitext.disable()
critratetext.disable()
#functions on clicks
def click():
    global score
    global multi
    global scoretext
    global diff
    global diffx
    global clickvalue
    global plusbonus
    global button_size
    global button
    global rngsizevalue
    global critrate
    global crithit
    global critratemulti
    if rngsize == True:
        rngsizevalue = 2
    else:
        rngsizevalue = 1
    if random.randint(critrate,100) == 100:
        crithit = 1
    else:
        crithit = 0
    score = score + (clickvalue * plusbonus)* multi * diffx * rngsizevalue * (crithit * critratemulti + 1)
    center_x = CENTER_X - 100
    center_y = CENTER_Y - 50
    spread = int(slider.getValue()) - 100
    min_x = max(0, center_x - spread)
    max_x = min(WIDTH - 200, center_x + spread)
    min_y = max(50, center_y - spread // 2)
    max_y = min(575 - 100, center_y + spread // 2)
    button.setX(random.randint(min_x, max_x))
    button.setY(random.randint(min_y, max_y))
    if rngsize == True:
        button_size = random.randint(50, 200)
        button.radius = button_size // 2
        button.setWidth(button_size)
        button.setHeight(button_size)
def rngclick():
    global rngsize
    if rngsize == False:
        rngsize = True
    else:
        rngsize = False
    rngsizebutton.setText(f"random size: {rngsize}")
    if rngsize == True:
        rngsizebutton.inactiveColour=(50, 200, 50)
        rngsizebutton.hoverColour=(50, 200, 50)
    else:
        rngsizebutton.inactiveColour=(200, 50, 50)
        rngsizebutton.hoverColour=(255, 100, 100)
#shop
def open_shop():
    global state
    state = "shop"
    button.hide()           
    slider.hide()
    slidertext.hide()
    shopbutton.hide()
    buttoncritbonus.show()
    critratetext.show()
    critratemultitext.show()
    buttoncrit.show()
    buttonmultibonus.show()
    multiownedtext.show()
    buttonplusbonus.show()
    buttonspsbonus.show()
    spsownedtext.show()
    plusownedtext.show()
    buttonsps.show()
    buttonplus.show()       
    buttonmulti.show()
    backbutton.show()
def close_shop():
    global state
    state = "game"
    buttonplus.hide()       
    buttonmulti.hide()
    backbutton.hide()
    buttonsps.hide()
    buttonspsbonus.hide()
    plusownedtext.hide()
    buttonplusbonus.hide()
    spsownedtext.hide()
    buttonmultibonus.hide()
    multiownedtext.hide()
    buttoncrit.hide()
    buttoncritbonus.hide()
    critratemultitext.hide()
    critratetext.hide()
    button.show()           
    slider.show()
    slidertext.show()
    shopbutton.show()
def multiplier():
    global multi
    global score
    global multicost
    global buttonmulti
    global multicount
    if score >= multicost:
        multi += multibonus
        score -= multicost
        multicost *= 10
        multicount += 1
        buttonmulti.setText(f'multiply costs {multicost}')  
        multiownedtext.setText(f"multiplier owned: {multicount}")
def plus():
    global score
    global clickvalue
    global pluscost
    global pluscount
    if score >= pluscost:
        clickvalue += plusbonus
        score -= pluscost
        pluscost *= 1.1
        pluscost = round(pluscost)
        pluscount += 1
        buttonplus.setText(f'score per click {pluscost}')
def sps():
    global score
    global spscost
    global spsadd
    global spscount
    if score >= spscost:
        score -= spscost
        spscost * 1.1
        spsadd += 50
        spscount += 1
        spsownedtext.setText(f"sps owned {spscount}")
        buttonsps.setText(f'sps costs: {spscost}')
def clickcritrate():
    global score
    global critratecost
    global critrate
    if score >= critratecost:
        critratecost * 2
        critrate += 1
        critratetext.setText(f"crit rate {critrate}/100")
def clickratebonus():
    global score
    global critrate
    if score >= critratecost and critrate >= critrateneeded:
        critratemulti += 10
        critrate -= 25
        critrateneeded += 50

def clickplusbonus():
    global score
    global pluscount
    global plusbonuscost
    global plusneeded
    global plusbonus
    if score >= plusbonuscost and pluscount >= plusneeded:
        score -= plusbonuscost
        plusbonus += 1
        plusneeded += 25
def clickspsbonus():
    global score
    global spscount
    global spsbonus
    global spsbonuscost
    global spsneeded
    if score >= spsbonuscost and spscount >= spsneeded:
        score -= spsbonuscost
        spsbonuscost * 2
        spsbonus += 1
        spsneeded + 25
def clickmultibonus():
    global score
    global multicount
    global multineeded
    if score >= multibonuscost and multicount >= multineeded:
        score -= multibonuscost
        multibonuscost * 2
        multibonus += 1
        multineeded += 25
def debugmode():
    global score
    global multi
    score += 999999999
#buttons
debugbutton = Button(
    screen,
    300, 600,
    300, 100,
    text='INFMONEY',
    fontsize=35,
    margin=20,
    inactiveColour=(200, 50, 50),
    hoverColour=(255, 100, 100),
    pressedColour=(50, 200, 50),
    onClick=debugmode
)
button = Button(
    screen, 
    x=150, 
    y=150, 
    width=button_size, 
    height=button_size,
    radius=button_size // 2,  # Must be exactly half of width/height
    text='Click Me',
    onClick=click
)
shopbutton = Button(
    screen,    
    1250, 20, 
    220, 70,
    text='SHOP',
    fontSize=30,
    margin=20,
    inactiveColour=(60, 120, 220),
    hoverColour=(90, 150, 255),
    pressedColour=(50, 200, 50),
    onClick=open_shop
)
rngsizebutton = Button(
    screen,             # The surface to draw the button onto
    0, 600,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'random size: {rngsize}'),    # Text displayed inside the button
    fontSize=35,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=rngclick  # Function to trigger on click
)
#buttons in shop
buttoncrit = Button(
    screen,             # The surface to draw the button onto
    1200, 600,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'critrate costs {critratecost}'),    # Text displayed inside the button
    fontSize=35,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=clickcritrate  # Function to trigger on click
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
buttoncritbonus = Button(
    screen,             # The surface to draw the button onto
    1200, 500,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'crit x2: {critbonusscore} and {critrate} owned'),    # Text displayed inside the button
    fontSize=23,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=multiplier  # Function to trigger on click
)
buttonmultibonus = Button(
    screen,             # The surface to draw the button onto
    0, 500,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'multi x2:{multibonuscost} score + {multineeded} owned'),    # Text displayed inside the button
    fontSize=20,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=clickmultibonus # Function to trigger on click
)
buttonplusbonus = Button(
    screen,             # The surface to draw the button onto
    300, 500,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f'plus x2:{plusbonuscost} score + {plusneeded} owned'),    # Text displayed inside the button
    fontSize=22,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=clickplusbonus  # Function to trigger on click
)
buttonspsbonus = Button(
    screen,             # The surface to draw the button onto
    900, 500,           # X and Y coordinates (top-left corner)
    300, 100,           # Width and Height of the button
    text=(f"SPS x2: {spsneeded} SPS + {spsbonuscost} score"),    # Text displayed inside the button
    fontSize=24,        # Size of the font
    margin=20,          # Minimum distance between text and edge
    inactiveColour=(200, 50, 50),   # Red button when normal
    hoverColour=(255, 100, 100),    # Lighter red when hovered
    pressedColour=(50, 200, 50),    # Green when clicked
    onClick=clickspsbonus  # Function to trigger on click
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
buttonsps = Button(
    screen,
    900, 600,
    300, 100,
    text=(f"sps costs {spscost}"),
    fontSize=30,
    margin=20,
    inactiveColour=(200, 50, 50),
    hoverColour=(255, 100, 100),
    pressedColour=(50, 200, 50),
    onClick=sps
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
    scoretext.setText(f"Current Score: {score}")
    diff = slider.getValue()
    diffx = slider.getValue() / 400
    scoretext.setText(f"Current Score: {score}")
    slidertext.setText(f"difficulty multiplier: {diffx}")
    clickvalue = 100 + (plusbonus * pluscount)
    if score >= spscost:
        buttonsps.inactiveColour=(50, 200, 50)
    else:
        buttonsps.inactiveColour=(200, 50, 50)
    if score >= multicost:
        buttonmulti.inactiveColour=(50, 200, 50)
    else:
        buttonmulti.inactiveColour=(200, 50, 50)
    if score >= pluscost:
        buttonplus.inactiveColour=(50, 200, 50)
    else:
        buttonplus.inactiveColour=(200, 50, 50)
    if score >= plusbonuscost and pluscount >= plusneeded:
        buttonplusbonus.inactiveColour=(50, 200, 50)
    else:
        buttonplusbonus.inactiveColour=(200, 50, 50)
    if score >= spsbonuscost and spscount >= spsneeded:
        buttonspsbonus.inactiveColour=(50, 200, 50)
    else:
        buttonspsbonus.inactiveColour=(200, 50, 50)
    if score >= critratecost:
        buttoncrit.inactiveColour=(50, 200, 50)
    else:
        buttoncrit.inactiveColour=(200, 50, 50)

    plusownedtext.setText(f"plus owned: {pluscount}")
    dt = clock.tick(100) / 500
    second += dt
    #print(second)
    if second >= 1.0:
        score += spsadd * int(spsbonus)
        second -= 1.0
    #backround color
    screen.fill((255, 255, 255))

    #pass the events list to pygame_widgets to manage the button
    pygame_widgets.update(events)

    #updates the display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
