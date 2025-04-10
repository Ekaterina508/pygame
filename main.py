import pygame # импортируем библиотеку pygame

class Food():
    def __init__(self, name_image, x, y, width, height): # конструктор, создание свойств
        self.image = pygame.image.load(name_image) # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect() # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self): # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))


pygame.init()# обязательная команда
window_size=(600,540)# размеры окна
screen = pygame.display.set_mode(window_size)# создание экрана с размерами
plate = Food("plate.png", 250, 450, 191, 56) # создание объекта класса Food
kitchen = Food("kitchen.png", 0, 0, 814, 540) # создание объекта класса Food

clock = pygame.time.Clock()# создание игрового таймера


while True:# игровой цикл
    clock.tick(40)# 40фпс\с
    kitchen.draw_image() # применение метода отрисовки к объекту класса Food
    plate.draw_image()# применение метода отрисовки к объекту класса Food
    pygame.display.update() # обновление содержимого экрана
    
    for event in pygame.event.get(): # проходимся по событиям
        if event.type == pygame.QUIT: # если нажали на крестик
            pygame.QUIT() # выход из игры
    pygame.display.update()
 

