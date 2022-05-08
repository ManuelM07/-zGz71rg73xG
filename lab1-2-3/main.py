class ProjectileMotion:

    def __init__(self, pos_x, pos_y, vel_x, vel_y, delta_t) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.delta_t = delta_t


    def launch(self) -> str:
        t = 0

        print(f"t = {t} pos x: {self.pos_x} pos y: {self.pos_y}")
        while True:
            t += self.delta_t
            self.pos_x = self.vel_x*t
            self.pos_y = self.vel_y*t-9.8*(t**2)/2

            if self.pos_y <= 0:
                break
            print(f"t = {t} pos x: {self.pos_x} pos y: {self.pos_y}")

        return "Termina"


##### TESTS #####

### test 1
projectile1 = ProjectileMotion(0, 0, 16.38, 11.47, 0.39)
projectile1.launch()

### test 2
projectile2 = ProjectileMotion(0, 0, 9.03, 11.98, 0.305)
projectile2.launch()