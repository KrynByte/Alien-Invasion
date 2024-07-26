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

        dim = math.floor(i / 8)
        for n in range(0, dim):
            self.y += sim_settings.ball_radius * 3

        self.x += (i - (dim * 8)) * sim_settings.ball_radius * 3

        self.xv = 0
        self.yv = 0
        self.xa = 0
        self.ya = 20  # Gravity acceleration

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
        if self.x - self.radius <= 0 and self.xv < 0:
            self.x = self.radius  # Adjust position to boundary
            self.xv = -self.xv * 0.7  # Reverse and dampen velocity

        if self.x + self.radius >= sim_settings.screen_width and self.xv > 0:
            self.x = sim_settings.screen_width - self.radius  # Adjust position to boundary
            self.xv = -self.xv * 0.7  # Reverse and dampen velocity

        if self.y - self.radius <= 0 and self.yv < 0:
            self.y = self.radius  # Adjust position to boundary
            self.yv = -self.yv * 0.8  # Reverse and dampen velocity

        if self.y + self.radius >= sim_settings.screen_height and self.yv > 0:
            self.y = sim_settings.screen_height - self.radius  # Adjust position to boundary
            self.yv = -self.yv * 0.8  # Reverse and dampen velocity

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

                if distance < 1:  # Avoid division by zero
                    distance = 1

                if distance < sim_settings.ball_radius ** 2:
                    force = min(10 / distance, sim_settings.ball_radius * 50)  # Cap the force
                    fx = force * (dx / distance)
                    fy = force * (dy / distance)

                    self.xv += fx
                    self.yv += fy

