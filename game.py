# from random import randint
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.__ball_pos = (0, 0)
        # self.__ball_pos = (randint(-300, 300), randint(50, 300))
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 50, 0)
        self.paddle_height = self.height / 4
        self.paddle_width = 20

        self.paddle_b_pos = (self.width / 2 - 50, 0)
        self.paddle_height = self.height / 4
        self.paddle_width = 20

        self.points_a = 0
        self.points_b = 0

        self.game_over = False

    # start move of turtle
    def tick(self):
        self.__perform_border_checking()
        self.__perform_paddle_hit_checking()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    # return current position of turtle
    def ball_pos(self):
        return self.__ball_pos

    # check if border is reached
    def __perform_border_checking(self):
        x, y = self.__ball_pos
        if abs(y) >= (self.height / 2):
            self.__ball_delta_y *= -1
        if abs(x) >= (self.width / 2):
            self.__ball_delta_x *= -1

    def __perform_paddle_hit_checking(self):
        x, y = self.__ball_pos
        a_x, a_y = self.paddle_a_pos
        b_x, b_y = self.paddle_b_pos
        hit_paddle_a = a_x == x and ((a_y - self.paddle_height / 2) <= y <= (a_y + self.paddle_height / 2))
        if hit_paddle_a:
            self.__ball_delta_x *= -1
            self.points_a += 1
            self.__ball_pos = (0, 0)
        hit_paddle_b = b_x == x and ((b_y - self.paddle_height / 2) <= y <= (b_y + self.paddle_height / 2))
        if hit_paddle_b:
            self.__ball_delta_x *= -1
            self.points_b += 1
            self.__ball_pos = (0, 0)

        if self.points_a >= 3 or self.points_b >= 3:
            self.game_over = True

    # method to move paddle_a_pos
    def paddle_a_up(self):
        x, y = self.paddle_a_pos
        self.paddle_a_pos = (x, y + 20)

    def paddle_a_down(self):
        x, y = self.paddle_a_pos
        self.paddle_a_pos = (x, y - 20)

    # method to move paddle_b_pos
    def paddle_b_up(self):
        x, y = self.paddle_b_pos
        self.paddle_b_pos = (x, y + 20)

    def paddle_b_down(self):
        x, y = self.paddle_b_pos
        self.paddle_b_pos = (x, y - 20)

    # check if border is reached by paddles
    def __perform_border_checking_paddle_a(self):
        x, y = self.__ball_pos
        if abs(y) >= (self.height / 2):
            self.__ball_delta_y *= -1
        if abs(x) >= (self.width / 2):
            self.__ball_delta_x *= -1





