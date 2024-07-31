import pygame
import math
from pygame.sprite import Sprite


class Particle(Sprite):
    def __init__(self, sim_settings, screen, i):
        super().__init__()
        self.screen = screen
        self.color = (255, 255, 255)
        self.radius = sim_settings.ball_radius
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.prediction = [0, 0]
        self.pressureF = [0, 0]

        rowcount = sim_settings.screen_width // (sim_settings.ball_radius * 3)

        # Calculate row and column indices
        row = i // rowcount
        col = i % rowcount

        # Set position based on row and column
        self.position[0] = (col * sim_settings.ball_radius * 3) + 10
        self.position[1] = (row * sim_settings.ball_radius * 3) + 10

        # Create an image of the ball, and set its rect attribute.
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        # Update the rect position
        self.rect.center = self.position

