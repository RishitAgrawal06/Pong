import pygame, sys, random

# function for the ball animation
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# function for the player (left side) animation
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.top >= screen_height:
        player.bottom = screen_height

# function for the opponent (right side) animation to move by itself
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.top >= screen_height:
        opponent.bottom = screen_height

# function for ball to restart when it touches one of the left/right side barriers
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# color scheme
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Game Variables
ball_speed_x = 2 * random.choice((1,-1))
ball_speed_y = 2 * random.choice((1,-1))
player_speed = 0
opponent_speed = 5

while True:
    # Handling the input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=5
            if event.key == pygame.K_UP:
                player_speed -=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=5
            if event.key == pygame.K_UP:
                player_speed +=5

    # Calling all the methods
    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen,light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))


    # Updating the window
    pygame.display.flip()
    clock.tick(300)