import pygame # импортируем библиотеку pygame

pygame.init() # обязательная команда

window_size=(300, 300) # создание размера окна
screen=pygame.display.set_mode(window_size) # создание окна, screen - окно
pygame.display.set_caption("Моя игра") # создание названия окна
background_color = (0, 0, 255) # создание цвета
screen.fill(background_color) # заливка окна цветом
clock = pygame.time.Clock() # создание игрового таймера (фпс)
r = pygame.Rect(120, 20, 100, 50) # создание прямоугольника, 120, 20 - координаты, а 100, 50 - ширина и высота
font = pygame.font.SysFont("Arial", 20) # создание шрифтф, 14 - размер
text = font.render("Ваня", True, (193, 177, 240))

while True: # игровой цикл
    clock.tick(40) # частота обновления сцены (40 кдр/сек)
    pygame.display.update() # обновление содержимого экрана
    pygame.draw.rect(screen, (255, 0, 0), r) # адресовка прямоугольника
    for event in pygame. event.get(): # проходимся по событиям
        if event.type == pygame.QUIT: # если нажали на крестик
            pygame.QUIT() # выход из игры
    screen.blit(text,(r.x, r.y))
