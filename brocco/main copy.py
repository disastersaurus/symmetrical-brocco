import pygame
import sys
import random
import RPi.GPIO as GPIO
from time import sleep

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f'Score: {current_time}', False, 'Black')
    score_rect = score.get_rect(center = (320, 50))
    screen.blit(score, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(rock, obstacle_rect)
        
        return obstacle_list
    else:
        return []

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 16 as an input pin
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


pygame.init()
screen =pygame.display.set_mode((640, 400))
pygame.display.set_caption('Brocco!')
clock = pygame.time.Clock()
font = pygame.font.Font('font/ARCADECLASSIC.TTF', 50)
game_active = True
score = 0
start_time = 0


background_img = pygame.image.load('images/city_2.png').convert_alpha()
foreground_img = pygame.image.load('images/ground.png').convert_alpha()

rock = pygame.image.load('images/rock.png').convert_alpha()
rock_rect = rock.get_rect(bottomright = (400, 300))
rock_x_pos = 400

obstacle_rect_list = []

brocco = pygame.image.load('images/idleR1-.png').convert_alpha()
brocco_width = brocco.get_rect().width
brocco_height = brocco.get_rect().height
brocco = pygame.transform.scale(brocco, (brocco_width*3.5, brocco_height*3.5))
brocco_rect = brocco.get_rect(midbottom = (80,300))
brocco_gravity = 0

brocco_right = pygame.image.load('images/idleL1-.png').convert_alpha()
brocco_right_width = brocco_right.get_rect().width
brocco_right_height = brocco_right.get_rect().height
brocco_right = pygame.transform.scale(brocco_right, (brocco_right_width*5, brocco_right_height*5))
brocco_right_rect = brocco_right.get_rect(center = (320, 200))


game_name = font.render('Brocco!', False, 'Black')
game_name_rect = game_name.get_rect(center = (320, 120))

press_start = font.render('Press Button to Start', False, 'Black')
press_start_rect = press_start.get_rect(center = (320, 300))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            GPIO.cleanup()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and brocco_rect.bottom >= 300:
                    brocco_gravity = -20  
            if event.type == obstacle_timer:
                obstacle_rect_list.append(rock.get_rect(bottomright = (random.randint (650, 900), 300)))
           
        else:
            if event.type == pygame.KEYDOWN and event.key == (GPIO.input(16) == GPIO.LOW):
                game_active = True
                rock_rect.left = 640
                start_time = int(pygame.time.get_ticks() / 1000)

    
    if game_active:
        screen.blit(background_img, (0, -80))
        screen.blit(foreground_img, (0, 300))
        score = display_score()
 
        rock_rect.x -= 4
        if rock_rect.right <= 0:
            rock_rect.left = 640
        screen.blit(rock, rock_rect)

        brocco_gravity += 1
        brocco_rect.y += brocco_gravity
        if brocco_rect.bottom >= 300:
            brocco_rect.bottom = 300
        screen.blit(brocco, brocco_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        if rock_rect.colliderect(brocco_rect):
            game_active = False
    else:
        screen.fill((190, 229, 176))
        screen.blit(brocco_right, brocco_right_rect)

        score_message = font.render(f'Score! {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center = (320, 300))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(press_start, press_start_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)