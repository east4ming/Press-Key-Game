"""Press Key Game.

描述:在空屏幕上显示按下的各种键.
设计:
- 空屏幕
- 事件循环, 检测`KEYDOWN`事件
- 打印属性`event.key`
"""
import pygame
import sys
import random


if not pygame.font:
    print('Warning, fonts disabled')


def init():
    """() -> (screen, font)

    初始化: pygame, screen surface, font
    返回: screen, font
    """
    pygame.init()
    # create screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Press Key")
    screen.fill((250, 250, 250))
    # create font
    font = pygame.font.Font(None, 120)
    return screen, font


def show_pressed_key(event, font, screen):
    """(event, font, screen) -> None

    根据event.key生成文本并渲染, 确定位置, 并显示
    """
    if pygame.font:
        text = font.render(pygame.key.name(event.key), 1, (random.randint(0, 255),
                                                           random.randint(0, 255),
                                                           random.randint(0, 255)))
        textpos = text.get_rect(centerx=random.randint(0, screen.get_width()),
                                centery=random.randint(0, screen.get_height()))
        # 如果要显示所有按过的键, 注释掉下边一行
        screen.fill((250, 250, 250))
        # screen.fill((random.randint(0, 255),
        #              random.randint(0, 255),
        #              random.randint(0, 255)))
        screen.blit(text, textpos)


def main():
    """main func.

    - 初始化(调用`init()`函数)
    - 主循环
        - 捕获事件并判断
            - 如果是KEYDOWN就显示屏幕上(调用`show_pressed_key()`函数)
        - flip
    """
    screen, font = init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 在屏幕上显示对应的key
                show_pressed_key(event, font, screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
