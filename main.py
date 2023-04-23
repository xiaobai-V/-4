import pygame
import sys
import time

from hammer import Hammer


class Whack_a_mole():

    def __init__(self):
        # 游戏初始化
        pygame.init()  # pygame初始化
        self.screen = pygame.display.set_mode((800, 600))  # 设置窗口大小
        pygame.display.set_caption("Whack a mole")  # 设置窗口标题

        self.background = pygame.image.load("./images/bg.png")  # 加载背景图片

        self.hammer = Hammer(self)  # 创建锤子对象

    def run_game(self):
        while True:
            self._check_joystick()  # 检查摇杆
            self._check_events()  # 检查事件
            self._update_screen()  # 更新屏幕
            time.sleep(0.05)

    def _check_joystick(self):
        self.hammer.update()  # 更新锤子位置
        self.hammer.check_mole()  # 检查锤子是否击中地鼠

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.blit(self.background, (0, 0))  # 绘制背景
        self.hammer.blitme()  # 绘制锤子
        pygame.display.flip()  # 更新屏幕


if __name__ == '__main__':
    # Make a game instance, and run the game.
    whack_a_mole = Whack_a_mole()  # 创建游戏对象
    whack_a_mole.run_game()  # 运行游戏
