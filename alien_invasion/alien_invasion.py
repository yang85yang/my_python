# -*- coding:utf-8 -*-

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建飞船
    ship = Ship(ai_settings, screen)

    #设置背景
    bg_color = (230, 230, 230)


    #开始游戏
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #每次循环都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship)

run_game()
