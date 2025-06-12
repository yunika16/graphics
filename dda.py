import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("DDA Line Drawing Algorithm")
screen.fill((0, 0, 0))  # Fill screen with black
white = (255, 255, 255)

def draw_line_DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x0
    y = y0

    for _ in range(steps):
        pygame.draw.circle(screen, white, (round(x), round(y)), 1)
        x += x_inc
        y += y_inc
        pygame.display.update()
        pygame.time.delay(50)

# Example coordinates
draw_line_DDA(100, 100, 500, 300)

# Keep window open until closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
