import pygame
import sys
import time

from hammer import Hammer


class Whack_a_mole():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Whack a mole")

        self.background = pygame.image.load("bg.png")

        self.hammer = Hammer(self)

        self.VRX = 123
        self.VRY = 123

    def run_game(self):
        while True:
            self._check_joystick()
            self._check_events()
            self._update_screen()
            time.sleep(0.5)

    def _check_joystick(self):
        pass

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.hammer.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    whack_a_mole = Whack_a_mole()
    whack_a_mole.run_game()
