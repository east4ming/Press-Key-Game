# PressKeyGame
按键小游戏: 在空屏幕上显示按下的各种键.

## 游戏设计

- 空屏幕
- 事件循环, 检测`KEYDOWN`事件
- 打印属性`event.key`

## 屏幕

- 创建一个screen
- 创建一个background
- 填充颜色

## 显示按键

## 字体

- 创建某一大小的字体

## 显示按键

### 按键

- `pygame.key.name(event.key)`获取按键int对应的name

### 渲染文本

- 渲染key.name文本
- 找一个显示的位置
- `blit`

## 主循环

1. 初始化
    - 屏幕
    - 背景
    - 字体
2. 主循环
    - 捕获事件并判断
        1. 如果是QUIT, 就退出
        2. 如果是KEYDOWN, 就根据`event.key`生成文本并渲染显示
3. `screen.blit()` 和 `pygame.display.flip()`
