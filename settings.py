class Settings():
    def __init__(self):
        # Screen settings.
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.speed = 500
        self.gravity = [0, 20]

        # Ball settings.
        self.amount = 256
        self.ball_color = (255, 255, 255)
        self.ball_radius = 5
        self.start_position = [10, 10]
        self.smoothingRadius = 100
        self.targetDensity = 5
        self.pressureMultiplier = 10
