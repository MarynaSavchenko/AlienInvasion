class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ships_limit = 3

        #Bullet settings
        self.bullet_height = 15
        self.bullet_width = 300
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settngs
        self.drop_speed_factor = 100
        self.alien_points = 50
        self.speed_up_scale = 1.1
        self.score_scale = 1.5
        self.initiaze_dynamic()


    def initiaze_dynamic(self):
        self.speed_factor = 1.5
        self.alien_speed_factor = 1
        # rigth = 1, left = -1
        self.fleet_direction = 1
        self.bullet_speed_factor = 1
        self.alien_points = int(self.alien_points*self.score_scale)

    def increase_speed(self):
        """Increase speed after completing level"""
        self.speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale


