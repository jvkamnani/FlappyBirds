import pygame
from Bird import Bird
from PipePair import PipePair
import random

pygame.init()

display_width = 512
display_height = 288
FPS = 60
background_scroll = 0
ground_scroll = 0
background_scroll_speed = 30
ground_scroll_speed = 60
background_looping_point = 413
ground_looping_point = 500
spawn_timer = 0
scrolling = True
not_play = True
score = 0
not_quit = True

bird = Bird(display_width, display_height)
pipe_pairs = []
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Birds')

background = pygame.image.load('D:/Flappy Birds/assets/sprites/background.png')
ground = pygame.image.load('D:/Flappy Birds/assets/sprites/ground.png')
crashed = False


def draw():
    pygame.display.update()
    gameDisplay.blit(background, (-background_scroll, 0))
    for pipe in pipe_pairs:
        pipe.render(gameDisplay)
    gameDisplay.blit(ground, (-ground_scroll, display_height - 16))
    bird.render(gameDisplay)
    score_surface = score_font.render(str(score), True, (255, 255, 255))
    score_x = display_width/2 - score_surface.get_width()/2
    score_y = display_height/4 - score_surface.get_height()/2
    gameDisplay.blit(score_surface, (score_x, score_y))

def update_background(dt):
    global background_scroll
    background_scroll = (background_scroll + dt * background_scroll_speed) % background_looping_point
0
    

def check_collision():
    global crashed
    for pipe_pair in pipe_pairs:
        
        if bird.x + bird.width > pipe_pair.lower_pipe.x and bird.x < pipe_pair.lower_pipe.x + pipe_pair.lower_pipe.width:
            if bird.y < pipe_pair.upper_pipe.y + pipe_pair.upper_pipe.height or bird.y + bird.height > pipe_pair.lower_pipe.y:
                crashed = True
    if bird.y + bird.height >= (display_height -16):
        crashed = True
            

def update_ground(dt):
    global ground_scroll
    ground_scroll = ground_scroll + dt * ground_scroll_speed
    if ground_scroll >= ground_looping_point:
        ground_scroll = 0

def pipe_update(dt):
    global spawn_timer
    spawn_timer += dt
    if spawn_timer > random.uniform(2.25, 50):
        pipe_pairs.append(PipePair(display_width, display_height, random.randint(-256, -134))) 
        spawn_timer = 0
    for pipe in pipe_pairs:
        pipe.update(dt)
    if pipe_pairs:
        if pipe_pairs[0].check_out_of_bounds():
            pipe_pairs.pop(0)
    
    
def update_score():
    global score
    for p in pipe_pairs:
            if p.upper_pipe.x + p.upper_pipe.width < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True
    

def update(dt):
    check_collision()
    update_ground(dt)
    update_background(dt)
    bird.update(dt)
    pipe_update(dt)
    update_score()
    
score_font = pygame.font.SysFont(None, 32, bold=True)

while not_play:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            not_play = False
            break
    draw()

bird.jump()

clock = pygame.time.Clock()

while not crashed:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if scrolling:
        update(dt)
    draw()
   
while not_quit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            not_quit = False
            break
    draw()    


pygame.quit()
quit()