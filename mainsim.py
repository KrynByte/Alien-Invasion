import pygame
import sys
from pygame.sprite import Group

from settings import Settings
from ball import Ball


def run_sim():
    pygame.init()
    sim_settings = Settings()
    screen = pygame.display.set_mode(
        (sim_settings.screen_width, sim_settings.screen_height))
    pygame.display.set_caption("Ball Simulation")

    bg_color = (0, 0, 0)

    # Create a Group to hold Ball objects
    balls = Group()

    # Create Ball objects and add it to the group
    for i in range(0,10):
        ball = Ball(sim_settings, screen)
        balls.add(ball)

    clock = pygame.time.Clock()
    fps = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all balls in the group
        dt = clock.tick(fps) / 100.0  # deltaTime in seconds
        for ball in balls:
            ball.update(dt, sim_settings, balls)

        # Draw the screen with the background color
        screen.fill(bg_color)

        # Draw all balls in the group
        balls.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


run_sim()
