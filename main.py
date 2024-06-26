import pygame
import random
from startbutton import StartButton
from bakerybackgroundfile import Bakery
from counterbgfile import Counter
from closeupcounterfile import CloseCounter
from backbuttonfile import Back
from musicbuttonfile import MusicButton
from nomusicbuttonfile import NoMusicButton
from mixingbowlfile import Bowl
from butterfile import Butter
from buttermeltedfile import MeltedButter
from forwardarrowfile import ForwardArrow
from backwardsarrowfile import BackArrow
from speechbubblefile import SpeechBubble
from wholeeggfile import WholeEgg
from crackedeggfile import CrackedEgg
from comingsoonfile import ComingSoon
from flavormachinefile import FlavorMachine
from chocochipfile import ChocoChip
from coconutfile import Coconut
from strawberryfile import Strawberry
from sprinklesfile import Sprinkles
from finishmixedbowlfile import FinishedBowl
from bessiefile import Bessie

pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('elephant', 40)
fonts = pygame.font.get_fonts()
print(fonts)
pygame.display.set_caption("Bessie's Bakery!")





# set up variables for the display
SCREEN_HEIGHT = 597
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


bg_image = Bakery(0,0)
play_button = StartButton(400, 250)
counter_screen = Counter(0,0)
close_counter_screen = CloseCounter(0,0)
back_button = Back(895,20)
music_button = MusicButton(20, 20)
no_music_button = NoMusicButton(20,20)
mixing_bowl = Bowl(300, 250)
butter = Butter(700, 300)
meltedbutter = MeltedButter(520,250)
forwardarrow = ForwardArrow(895, 490)
backarrow = BackArrow(20,490)
bubble = SpeechBubble(150, 100)
wholeegg = WholeEgg(700, 300)
crackedegg = CrackedEgg(490, 200)
comingsoon = ComingSoon(400, 100)
flavormachine = FlavorMachine(100, 0)
strawberrytopping = Strawberry(200, 100)
coconuttopping = Coconut(200, 100)
sprinklestopping = Sprinkles(200, 100)
chocotopping = ChocoChip(200, 100)
mixedbowl = FinishedBowl(300, 300)
bessiebear = Bessie(400, 300)

music = pygame.mixer.music.load('BakerySoundtrack.mp3')
pygame.mixer.music.play(-1)

# Game Logic
randostrawberry = False
randosprinkles = False
randococonut = False
randochocochip = False
toppings = ["chocolate chips", "coconut", "sprinkles", "strawberries"]
selected_topping = random.choice(toppings)
print(selected_topping)
if selected_topping == "chocolate chips":
    randochocochip = True
elif selected_topping == "coconut":
    randococonut = True
elif selected_topping == "strawberries":
    randostrawberry = True
elif selected_topping == "sprinkles":
    randosprinkles = True



# Variables
scene = 0
# scene 0 = home screen
# scene 1 = order station
# scene 2 = ingredient mixing place
game_start = False
cooking = False
music = True
draggingbutter = False
draggingegg = False
butterin = False
eggin = False

# Main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            draggingbutter = False
            draggingegg = False
            if scene == 0 and play_button.rect.collidepoint(event.pos):
                scene += 1
            elif forwardarrow.rect.collidepoint(event.pos):
                scene += 1
                if scene >= 4:
                    scene = 4
            elif backarrow.rect.collidepoint(event.pos):
                scene -= 1
                if scene <= 0:
                    scene = 0
            elif back_button.rect.collidepoint(event.pos):
                scene = 0
            elif music_button.rect.collidepoint(event.pos):
                music = not music
            elif butter.rect.collidepoint(event.pos):
                butterin = True
            elif wholeegg.rect.collidepoint(event.pos):
                eggin = True  # Set eggin to True when the egg is added
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if butter.rect.collidepoint(event.pos):
                    draggingbutter = True
                elif wholeegg.rect.collidepoint(event.pos):
                    draggingegg = True
        elif event.type == pygame.MOUSEMOTION:
            if draggingbutter:
                butter.rect.move_ip(event.rel)
            elif draggingegg:
                wholeegg.rect.move_ip(event.rel)

    # Scene rendering
    screen.fill((176, 139, 120))
    if scene == 0:
        screen.blit(bg_image.image, (0, 0))
        screen.blit(play_button.image, (400, 250))
    elif scene == 1:
        screen.blit(counter_screen.image, (0, 0))
        screen.blit(bessiebear.image, (460, 180))
        screen.blit(bubble.image, (150, 100))
        if randostrawberry:
            screen.blit(strawberrytopping.image, (260, 170))
        elif randococonut:
            screen.blit(coconuttopping.image, (280, 180))
        elif randosprinkles:
            screen.blit(sprinklestopping.image, (240, 165))
        elif randochocochip:
            screen.blit(chocotopping.image, (260, 180))
    elif scene == 2:
        screen.blit(close_counter_screen.image, (0, 0))
        screen.blit(mixing_bowl.image, (230, 50))
        if not butterin:
            screen.blit(butter.image, butter.rect)
        else:
            screen.blit(meltedbutter.image, (250, 90))
        if not eggin and butterin:
            screen.blit(wholeegg.image, wholeegg.rect)
        elif eggin:
            screen.blit(crackedegg.image, (310, 110))
    elif scene == 3:
        screen.blit(counter_screen.image, (0, 0))
        screen.blit(flavormachine.image, (130, -50))
        screen.blit(mixedbowl.image, (390, 340))
    elif scene == 4:
        screen.fill((176, 139, 120))
        screen.blit(comingsoon.image, (250, 50))
    if scene != 0:
        screen.blit(back_button.image, (895, 20))
        screen.blit(forwardarrow.image, (895, 490))
        screen.blit(backarrow.image, (20, 490))
        screen.blit(music_button.image, (20, 20))

    # Music control
    if music:
        pygame.mixer.music.unpause()
        screen.blit(music_button.image, (20, 20))
    else:
        pygame.mixer.music.pause()
        screen.blit(no_music_button.image, (20, 20))

    pygame.display.update()
pygame.quit()
