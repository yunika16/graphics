import pygame
import sys

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Ellipse Algorithm")
screen.fill((0, 0, 0))
white = (255, 255, 255)

def plot_ellipse_points(xc, yc, x, y):
    # Plot points using 4-way symmetry
    screen.set_at((xc + x, yc + y), white)
    screen.set_at((xc - x, yc + y), white)
    screen.set_at((xc + x, yc - y), white)
    screen.set_at((xc - x, yc - y), white)

def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    # Initial decision parameter of region 1
    ry_sq = ry * ry
    rx_sq = rx * rx
    two_ry_sq = 2 * ry_sq
    two_rx_sq = 2 * rx_sq

    # Region 1
    p1 = ry_sq - (rx_sq * ry) + (0.25 * rx_sq)
    dx = two_ry_sq * x
    dy = two_rx_sq * y

    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx += two_ry_sq
        if p1 < 0:
            p1 += ry_sq + dx
        else:
            y -= 1
            dy -= two_rx_sq
            p1 += ry_sq + dx - dy
        pygame.display.update()
        pygame.time.delay(10)

    # Region 2
    p2 = (ry_sq) * ((x + 0.5) ** 2) + (rx_sq) * ((y - 1) ** 2) - (rx_sq * ry_sq)
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy -= two_rx_sq
        if p2 > 0:
            p2 += rx_sq - dy
        else:
            x += 1
            dx += two_ry_sq
            p2 += rx_sq - dy + dx
        pygame.display.update()
        pygame.time.delay(10)

# Example usage:
midpoint_ellipse(300, 300, 150, 100)

# Keep window open until closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
