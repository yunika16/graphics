import pygame
import sys

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Algorithm")
screen.fill((0, 0, 0))
white = (255, 255, 255)

def plot_circle_points(xc, yc, x, y):
    # Plot all eight symmetric points
    screen.set_at((xc + x, yc + y), white)
    screen.set_at((xc - x, yc + y), white)
    screen.set_at((xc + x, yc - y), white)
    screen.set_at((xc - x, yc - y), white)
    screen.set_at((xc + y, yc + x), white)
    screen.set_at((xc - y, yc + x), white)
    screen.set_at((xc + y, yc - x), white)
    screen.set_at((xc - y, yc - x), white)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)
        pygame.display.update()
        pygame.time.delay(10)

# Example usage:
midpoint_circle(300, 300, 150)

# Keep window open until closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
