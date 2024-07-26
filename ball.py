import pygame
import math
import random
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, sim_settings, screen, i):
        super().__init__()
        self.screen = screen
        self.color = (255, 255, 255)
        self.radius = sim_settings.ball_radius
        self.x = sim_settings.start_position[0]
        self.y = sim_settings.start_position[1]
        if i >= 12:
            self.y += 75
            self.x -= 300
        elif i >= 8:
            self.y += 50
            self.x -= 200
        elif i >= 4:
            self.y += 25
            self.x -= 100

        self.x += i * 25

        self.xv = 50
        self.yv = 0
        self.xa = 0
        self.ya = 9.8  # Gravity acceleration

        # Create an image of the ball, and set its rect attribute.
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, dt, sim_settings, balls):
        """Move ball according to physics and handle bouncing off edges."""
        # Update velocity with acceleration
        self.xv += self.xa * dt
        self.yv += self.ya * dt

        # Check for collisions with the screen edges and bounce
        if (self.x - self.radius <= 0 and self.xv < 0) or (
                self.x + self.radius >= sim_settings.screen_width and self.xv > 0):
            self.xv = -self.xv * 0.9  # Reverse the horizontal velocity

        if (self.y - self.radius <= 0 and self.xv < 0) or (
                self.y + self.radius >= sim_settings.screen_height and self.yv > 0):
            self.yv = -self.yv * 0.9  # Reverse the horizontal velocity

        # Update position with velocity
        self.x += self.xv * dt
        self.y += self.yv * dt

        # Update the rect position
        self.rect.center = (self.x, self.y)

        for ball in balls:
            if ball != self:
                dx = self.x - ball.x
                dy = self.y - ball.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                force = 10 / distance ** 2
                if distance < sim_settings.ball_radius * 4:
                    self.xv += force*(dx/distance)
                    self.yv += force*(dx/distance)
