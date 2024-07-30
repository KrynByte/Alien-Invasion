import pygame
import math
from pygame.sprite import Sprite


class Particle(Sprite):
    def __init__(self, sim_settings, screen, i):
        super().__init__()
        self.screen = screen
        self.color = (255, 255, 255)
        self.radius = sim_settings.ball_radius
        self.position = sim_settings.start_position
        self.velocity = [0, 0]
        self.prediction = [0, 0]
        self.pressureF = [0, 0]

        dim = math.floor(i / 8)
        for n in range(0, dim):
            self.position[0] += sim_settings.ball_radius * 3

        self.position[0] += (i - (dim * 8)) * sim_settings.ball_radius * 3

        # Create an image of the ball, and set its rect attribute.
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        # Update the rect position
        print(self.position)
        self.rect.center = self.position

