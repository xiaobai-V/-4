import pygame
import hammer
import sys


class Whack_a_mole():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Whack a mole")

        self.background = pygame.image.load("bg.png")

        def run_game(self):
            while True:
                self._check_events()
                self._update_screen()

        def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        def _update_screen(self):
            self.screen.fill(self.background)
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    whack_a_mole = Whack_a_mole()
    whack_a_mole.run_game()
