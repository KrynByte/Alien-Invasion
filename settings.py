class Settings():
    def __init__(self):
        # Screen settings.
        self.screen_width = 200
        self.screen_height = 300
        self.bg_color = (0, 0, 0)
        self.speed = 500
        self.gravity = [0, 20]

        # Ball settings.
        self.amount = 16
        self.ball_color = (255, 255, 255)
        self.ball_radius = 5
        self.smoothingRadius = 100
        self.targetDensity = 50
        self.pressureMultiplier = 50
