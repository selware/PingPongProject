import sys
import pygame
from pygame.locals import *
from pong.logic import Logic
from pong.gui import Gui


class Pong(object):
    """
    The main class of the pong game. The main loop is located here.
    """
    def __init__(self):
        self._logic = Logic()
        self._gui = Gui()
        self._clock = pygame.time.Clock()

    def run(self):
        """
        This is the main loop
        """
        while True:

            # Check which keys were pressed and if the player ended the game
            pressed_key = self._process_key_events()

            # Send the pressed keys to the logic
            self._logic.get_update(pressed_key)

            # Receive the current game state from the logic
            (player_rects, opponent_rects,
             ball, player_score,
             opponent_score) = self._logic.get_state()

            # Render the current state to the screen
            self._gui.render_screen(player_rects, opponent_rects, ball,
                                    player_score, opponent_score)

            self._clock.tick(60)

    @staticmethod
    def _process_key_events():
        """
        checks if the player wants to quit the game and what key is pressed and returns it or None if no key is pressed
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        key = pygame.key.get_pressed()

        if key[K_UP]:
            return "UP"

        elif key[K_DOWN]:
            return "DOWN"

        else:
            return None


if __name__ == "__main__":
    game = Pong()
    game.run()
