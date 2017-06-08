import pygame
import math


class Logic(object):
    """
    in this class all the calculations for the logic are done.

    it takes the player inputs and moves the player accordingly

    it processes the movement of the ball

    as there is no other player at the moment this class simulates the opponent

    this class returns the current player position, the opponent position, the ball position, the player score and
    the opponent score

    this class can be rewritten to represent your server
    """
    def __init__(self):
        self.playerRects = {
            -60: pygame.Rect(50, 380, 10, 20),  # Bottom of paddle
            -45: pygame.Rect(50, 360, 10, 20),
            -30: pygame.Rect(50, 340, 10, 20),
            -0: pygame.Rect(50, 320, 10, 20),
            30: pygame.Rect(50, 300, 10, 20),
            45: pygame.Rect(50, 280, 10, 20),
            60: pygame.Rect(50, 260, 10, 20),  # Top of paddle
        }

        self.opponentRects = {
            -60: pygame.Rect(750, 380, 10, 20),  # Bottom of paddle
            -45: pygame.Rect(750, 360, 10, 20),
            -30: pygame.Rect(750, 340, 10, 20),
            -0: pygame.Rect(750, 320, 10, 20),
            30: pygame.Rect(750, 300, 10, 20),
            45: pygame.Rect(750, 280, 10, 20),
            60: pygame.Rect(750, 260, 10, 20),  # Top of paddle
        }

        self.ball = pygame.Rect(400, 300, 5, 5)

        self.ballAngle = math.radians(0)
        self.ballSpeed = 10
        self.playerScore = 0
        self.opponentScore = 0
        self.direction = -1
        self.pause = 10

    def get_update(self, key):
        """
        takes the pressed key from the main loop
        """
        if key is None:
            pass
        elif key == "UP":
            self._move_player_up()
        elif key == "DOWN":
            self._move_player_down()

    def get_state(self):
        """
        Get the current game state.

        Returns:
            (player_rects, opponent_rects, ball, player_score, opponent_score)
        """

        self._update_opponent()

        if self.pause:
            self.pause -= 1
        else:
            self._update_ball()

        return self.playerRects, self.opponentRects, self.ball, self.playerScore, self.opponentScore

    def _move_player_up(self):
        if self.playerRects[60].y > 0:
            for pRect in self.playerRects:
                self.playerRects[pRect].y -= 5

    def _move_player_down(self):
        if self.playerRects[-60].y < 590:
            for pRect in self.playerRects:
                self.playerRects[pRect].y += 5

    def _update_opponent(self):
        if self.ball.y > self.opponentRects[0].y:
            if self.opponentRects[-60].y > 580:
                return
            for oRect in self.opponentRects:
                self.opponentRects[oRect].y += 6

        elif self.ball.y < self.opponentRects[0].y:
            if self.opponentRects[60].y <= 0:
                return
            for oRect in self.opponentRects:
                self.opponentRects[oRect].y -= 6

    def _update_ball(self):
        if self.ball.y <= 0 or self.ball.y > 595:
            self.ballAngle *= -1
        self.ball.x += self.direction * self.ballSpeed * math.cos(self.ballAngle)
        self.ball.y += self.direction * self.ballSpeed * -math.sin(self.ballAngle)
        if self.ball.x > 800 or self.ball.x < 0:
            if self.ball.x > 800:
                self.playerScore += 1

            elif self.ball.x < 0:
                self.opponentScore += 1
            self.ball.x = 400
            self.ball.y = 300
            self.ballAngle = math.radians(0)
            self.pause = 10
            if self.opponentScore >= 11 or self.playerScore >= 11:
                self.opponentScore = 0
                self.playerScore = 0
            return

        if self.direction < 0:
            for pRect in self.playerRects:
                if self.playerRects[pRect].colliderect(self.ball):
                    self.ballAngle = math.radians(pRect)
                    self.direction = 1
                    break

        else:
            for oRect in self.opponentRects:
                if self.opponentRects[oRect].colliderect(self.ball):
                    self.ballAngle = math.radians(oRect)
                    self.direction = -1