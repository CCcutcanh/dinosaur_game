import pygame, sys
from pygame.locals import *

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('dinosaur')
run = True
pause = False
jump = False
clock = pygame.time.Clock()
#back ground cho game
bg = pygame.image.load('image/background.jpg')
bg_x = 0 
bg_y = 0 
#khủng long
dino = pygame.image.load('image/dinosaur.png')
dino_x = 0
dino_y = 227
velocity = 5
#cây
tree = pygame.image.load('image/tree.png')
tree_x = 550
tree_y = 227
#pause game
restart = pygame.image.load('image/reload.png') 
#text
font = pygame.font.SysFont('san', 25)
font1 = pygame.font.SysFont('san', 40)
font2 = pygame.font.Font('image/BigShouldersText-VariableFont_wght.ttf', 25)
score = 0
#sound
sound1 = pygame.mixer.Sound('image/te.wav')
sound = pygame.mixer.Sound('image/tick.wav')
while run:
    clock.tick(60)
    screen.fill(WHITE)
    bg_rect = screen.blit(bg, (bg_x, bg_y))
    bg2 = screen.blit(bg, (bg_x+600, bg_y)) 
    dino_rect = screen.blit(dino, (dino_x, dino_y))
    tree_rect = screen.blit(tree, (tree_x, tree_y))
    score_text = font.render(str(score), True, BLACK)
    screen.blit(score_text, (0, 0))
    if dino_rect.colliderect(tree_rect):
        pause = True
        pygame.mixer.Sound.play(sound1)
        pause_rect = screen.blit(restart, (275, 125))
        gameover_text = font1.render("GAME OVER", True, BLACK)
        screen.blit(gameover_text, (225, 200))
        text_gameover = font2.render("bấm space để chơi lại game", True, BLACK)
        screen.blit(text_gameover, (210, 230))
    if jump == True:
        dino_y -= velocity
    if 80 > dino_y:
        jump = False
    if jump == False and dino_y < 227:
        dino_y += velocity
    if bg_x+600 <= 0:
        bg_x = 0
    if tree_x <= 0:
        tree_x = 550
        score += 1
    #dino_x += velocity
    if pause == False:
        tree_x -= velocity
        bg_x -= velocity
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y == 227 and pause == False:
                jump = True
                pygame.mixer.Sound.play(sound)
            if event.key == K_SPACE and pause == True:
                bg_x = 0
                tree_x = 550
                tree_y = 227
                bg_x = 0
                bg_y = 0
                pause = False
    pygame.display.flip()