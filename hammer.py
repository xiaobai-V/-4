import pygame
import random
import PCF8591 as ADC


class Hammer():
    def __init__(self, game):

        ADC.setup(0x48)  # PCF8591模块地址设置
        # 从game中获取屏幕对象
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # 加载锤子图片,并转换为合适大小
        self.image = pygame.image.load('./images/hammer.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        # 接收模拟输入
        self.VRX = 0
        self.VRY = 0
        self.SW = 1
        self.hit = False
        self.hitted = False
        # 计算锤子坐标
        self.x = int(self.screen_rect.width * self.VRX / 255)
        self.y = int(self.screen_rect.height * self.VRY / 255)
        # 锤子位置
        self.position = (self.x, self.y)

    def blitme(self):
        self.screen.blit(self.image, self.position)  # 绘制锤子

    def update(self):
        # 读取模拟输入
        self.VRX = ADC.read(0)
        self.VRY = ADC.read(1)
        # 计算锤子坐标，-25是为了让锤子的中心点与摇杆的位置重合
        self.x = int(self.screen_rect.width * self.VRX / 255)-25
        self.y = int(self.screen_rect.height * self.VRY / 255)-25
        # 限制锤子的移动范围在屏幕内
        if (self.x < 0):
            self.x = 0
        if (self.y < 0):
            self.y = 0
        if (self.x > self.screen_rect.width-50):
            self.x = self.screen_rect.width-50
        if (self.y > self.screen_rect.height-50):
            self.y = self.screen_rect.height-50
        self.position = (self.x, self.y)

    def is_hitted(self):
        # 锤子击中
        SW = ADC.read(2)
        if (SW < 5):
            self.hit = True
        else:
            self.hit = False
        if (self.hit):
            # 根据坐标判断是否击中,如果两个矩形相交，返回True
            pass
