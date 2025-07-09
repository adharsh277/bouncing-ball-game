import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
ball = pygame.Rect(100, 100, 50, 50)
speed = [5, 5]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball = ball.move(speed)
    if ball.left < 0 or ball.right > 800:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > 600:
        speed[1] = -speed[1]
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    pygame.display.flip()
    clock.tick(60)
