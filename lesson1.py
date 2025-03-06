import pygame # импортируем библиотеку pygame
pygame.init() # обязательная команда
window_size=(300, 300) # создание размера окна
screen=pygame.display.set_mode(window_size) # создание окна, screen - окно
pygame.display.set_caption("Моя игра") # создание названия окна
background_color = (0, 0, 255) # создание цвета
clock = pygame.time.Clock() # создание игрового таймера (фпс)
x = 100
y = 50
font = pygame.font.SysFont("Arial", 20) # создание шрифтф, 14 - размер
text = font.render("Ваня", True, (193, 177, 240))
while True: # игровой цикл
    screen.fill(background_color) # заливка окна цветом
    r = pygame.Rect(x, y, 100, 50) # создание прямоугольника, 120, 20 - координаты, а 100, 50 - ширина и высота

    pygame.draw.rect(screen, (255, 0, 0), r) # адресовка прямоугольника

    clock.tick(40) # частота обновления сцены (40 кдр/сек)
    pygame.display.update() # обновление содержимого экрана
    for event in pygame. event.get(): # проходимся по событиям
        if event.type == pygame.KEYDOWN: # тип события
            if event.key == pygame.K_a: # клавиша
                x = x - 5
            if event.key == pygame.K_w: # клавиша
                y = y - 5
            if event.key == pygame.K_d: # клавиша
                x = x + 5
            if event.key == pygame.K_s: # клавиша
                y = y + 5
            if event.type == pygame.QUIT: # если нажали на крестик
             pygame.QUIT() # выход из игры
             screen.blit(text,(r.x, r.y))