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
    for i in range(0, sim_settings.amount):
        ball = Ball(sim_settings, screen, i)
        balls.add(ball)

    clock = pygame.time.Clock()
    fps = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all balls in the group
        dt = clock.tick(fps) / sim_settings.speed  # deltaTime in seconds
        for ball in balls:
            ball.update(dt, sim_settings, balls)

        # Draw the screen with the background color
        screen.fill(bg_color)

        # Draw all balls in the group
        balls.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def step(dt, sim_settings, particles):
    # Apply Gravity
    for particle in particles:
        particle.velocity += sim_settings.gravity * dt
        particle.prediction = particle.position + particle.velocity * dt

    # Calculate density
    for particle in particles:
        particle.density = calcdensity(particle.prediction)

    # Calculate and apply pressure
    for particle in particles:
        particle.pressureF = calcpressureforce(particle)
        particle.pressureA = particle.pressureF / particle.density
        particle.velocity += particle.pressureA * dt

    # Collisions
    for particle in particles:
        particle.position +=velocity

def smoothingker(radius, distance):

# Update the rect position
self.rect.center = (self.x, self.y)

run_sim()
