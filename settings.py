class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.speed_factor = 1.5
        self.ships_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settngs
        self.alien_speed_factor = 1
        self.drop_speed_factor = 100
        #rigth = 1, left = -1
        self.fleet_direction = 1
