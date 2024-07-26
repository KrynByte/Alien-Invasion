class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings.
        self.screen_width = 300
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.speed = 500

        # Ball settings.
        self.amount = 256
        self.ball_color = (255, 255, 255)
        self.ball_radius = 5
        self.start_position = [10, 10]