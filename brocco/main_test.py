import pygame
from sys import exit
 
def display_score():
    current_time = pygame.time.get_ticks()
    score = font.render(f'{current_time}', False, (64,64,64))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)
    
#loads images to python readable form
def loadImage(image, alpha=False):
    image = pygame.image.load(image)
    return image.convert_alpha() if alpha else image.convert()


pygame.init()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Brocco!')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

#retrieve miscellaneous images
screenIcon = loadImage('images/idleL1-.png', True)
petIdleR1 = loadImage('images/idleR1-.png', True)
petIdleR2 = loadImage('images/idleR2-.png', True)
background_img = loadImage('images/city_bg.jpg', True)
foreground_img = loadImage('images/ground.png', True)

#sets icon on window
pygame.display.set_icon(screenIcon)

health_bar = pygame.Rect(10, 20, 100, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    health_bar.width += -0.00000000000005

  # Check if the pet is dead
    if health_bar.width <= 0:
        print('Your pet has died!')
        break

  # Draw the game state
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(background_img,(0,-80))
    screen.blit(foreground_img, (0, 300))
    pygame.draw.rect(screen, (255, 0, 0), health_bar)  # Draw the health bar

    pygame.display.update()
    clock.tick(24)