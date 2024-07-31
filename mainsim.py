import pygame
import math
import random
import sys
from pygame.sprite import Group

from settings import Settings
from ball import Particle


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
        ball = Particle(sim_settings, screen, i)
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
        step(dt, balls, sim_settings)
        for ball in balls:
            ball.update()

        # Draw the screen with the background color
        screen.fill(bg_color)

        # Draw all balls in the group
        balls.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def step(dt, particles, sim_settings):
    # Apply Gravity
    for particle in particles:
        # Assuming gravity is a list like [gx, gy] for 2D space
        particle.velocity = [v + g * dt for v, g in zip(particle.velocity, sim_settings.gravity)]
        particle.prediction = [pos + vel * dt for pos, vel in zip(particle.position, particle.velocity)]

    # Calculate density
    for particle in particles:
        particle.density = calcDensity(particle, particles, sim_settings)

    # Calculate and apply pressure
    for particle in particles:
        particle.pressureF = calcPressure(particle, particles, sim_settings)
        if particle.density != 0:
            particle.pressureA = [x / particle.density for x in particle.pressureF]
        else:
            particle.pressureA = particle.pressureF
        particle.velocity = [v + pa * dt for v, pa in zip(particle.velocity, particle.pressureA)]

    # Collisions
    for particle in particles:
        collision(particle, sim_settings)

    # Update positions
    for particle in particles:
        particle.position = [p + v * dt for p, v in zip(particle.position, particle.velocity)]


def smoothingKer(smoothingRadius, distance):
    volume = math.pi * pow(smoothingRadius, 8) / 4
    value = max(0, smoothingRadius ** 2 - distance ** 2)
    return (value ** 3) / volume


def smoothingKerd(smoothingRadius, distance):
    if distance >= smoothingRadius:
        return 0;
    f = smoothingRadius ** 2 - smoothingRadius ** 2
    scale = -24 / (math.pi * pow(smoothingRadius, 8))
    return scale * distance * f * f


def calcDensity(thisParticle, particles, sim_settings):
    density = 0
    mass = 1

    for particle in particles:
        if particle != thisParticle:
            # Calculate the Euclidean distance between the particles
            distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(particle.position, thisParticle.position)))
            influence = smoothingKer(sim_settings.smoothingRadius, distance)
            density += mass * influence

    return density


def densityToPressure(density, sim_settings):
    densityError = density - sim_settings.targetDensity
    pressure = densityError * sim_settings.pressureMultiplier
    return pressure


def calcPressure(thisParticle, particles, sim_settings):
    mass = 1
    pressureForce = [0, 0]  # Assuming a 2D space

    for particle in particles:
        if particle != thisParticle:
            offset = [a - b for a, b in zip(particle.position, thisParticle.position)]
            distance = math.sqrt(sum(comp ** 2 for comp in offset))
            if distance != 0:
                direction = [comp / distance for comp in offset]
            else:
                direction = [random.uniform(-1, 1) for _ in offset]
                norm = math.sqrt(sum(comp ** 2 for comp in direction))
                direction = [comp / norm for comp in direction] if norm != 0 else [0, 0]

            slope = smoothingKerd(sim_settings.smoothingRadius, distance)
            otherdensity = particle.density
            particledensity = thisParticle.density
            pressure = densityToPressure(otherdensity, sim_settings) + densityToPressure(particledensity, sim_settings)
            force_contribution = [pressure * dir_comp * slope * mass / otherdensity for dir_comp in direction]
            pressureForce = [f + fc for f, fc in zip(pressureForce, force_contribution)]

    return pressureForce


def collision(particle, sim_settings):
    # Handle horizontal boundaries
    if particle.position[0] - particle.radius <= 0:
        particle.position[0] = particle.radius  # Adjust position to boundary
        particle.velocity[0] = -particle.velocity[0] * 0.5  # Reverse and dampen velocity
    elif particle.position[0] + particle.radius >= sim_settings.screen_width:
        particle.position[0] = sim_settings.screen_width - particle.radius  # Adjust position to boundary
        particle.velocity[0] = -particle.velocity[0] * 0.5  # Reverse and dampen velocity

    # Handle vertical boundaries
    if particle.position[1] - particle.radius <= 0:
        particle.position[1] = particle.radius  # Adjust position to boundary
        particle.velocity[1] = -particle.velocity[1] * 0.5  # Reverse and dampen velocity
    elif particle.position[1] + particle.radius >= sim_settings.screen_height:
        particle.position[1] = sim_settings.screen_height - particle.radius  # Adjust position to boundary
        particle.velocity[1] = -particle.velocity[1] * 0.5  # Reverse and dampen velocity

    # Return the updated particle (not necessary if you update in-place)
    return particle


run_sim()
