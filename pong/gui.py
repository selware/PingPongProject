import pygame


class Gui(object):
    """
    class to render the gui
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()
        self.font = pygame.font.SysFont("Times", 50)

    def render_screen(self, playerRects, opponentRects, ball, playerScore, opponentScore ):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), ball)
        self.screen.blit(self.font.render(str(playerScore), -1, (255, 255, 255)), (200, 25))
        self.screen.blit(self.font.render(str(opponentScore), -1, (255, 255, 255)), (600, 25))
        self._draw_players(playerRects, opponentRects)
        pygame.display.flip()

    def _draw_players(self, playerRects, opponentRects):
        for pRect in playerRects:
            pygame.draw.rect(self.screen, (255, 255, 255), playerRects[pRect])
        for oRect in opponentRects:
            pygame.draw.rect(self.screen, (255, 255, 255), opponentRects[oRect])