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


if not pygame.font: print ('Warning, fonts disabled')

def show_key(event, font, background):
    """根据event.key生成文本并渲染, 确定位置, 返回文本和位置"""
    if pygame.font:
        text = font.render(pygame.key.name(event.key), 1, (random.randint(0, 255),
                                                           random.randint(0, 255),
                                                           random.randint(0, 255)))
        textpos = text.get_rect(centerx=random.randint(0, background.get_width()),
                                centery=random.randint(0, background.get_height()))
        return (text, textpos)

def main():
    """main

    - 初始化
    - 主循环
        - 捕获事件并判断
            - 如果是KEYDOWN就显示屏幕上
        - screen.blit
        - flip
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Press Key")
    # Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    # font
    font = pygame.font.Font(None, 120)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 在屏幕上显示对应的key
                # print(event.key)
                # Put Text On The Background, Centered
                font_tuple = show_key(event, font, background)
                # 如果要显示所有按过的键, 注释掉下边一行
                background.fill((250, 250, 250))
                # background.fill((random.randint(0, 255),
                #                random.randint(0, 255),
                #                random.randint(0, 255)))
                background.blit(*font_tuple)


        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
