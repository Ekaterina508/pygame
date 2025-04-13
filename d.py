import turtle

import pygame # импортируем библиотеку pygame


class Food():
    def __init__(self, name_image, x, y):  # конструктор, создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect()  # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x  # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y  # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self):  # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_plate(self):
        keys = pygame.key.get_pressed() # получение списка нажатых клавиш
        if keys[pygame.K_LEFT] == True: # если нажата клавиша влево
            self.rect.x -= 5
        if keys [pygame.K_RIGHT]: # если нажата клавиша вниз
            self.rect.x += 5

    def move_food(self):
        self.rect.y += 5



fon = Food ("кухня.jpg", 0, 0)# создание фона
pygame.init()  # обязательная команда
window_size = (1000, 750)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
plate = Food("plate.png", 400, 650)  # создание объекта класса Food
marmalade = Food( "food1.png", 150, 0) # создание объекта класса Food
dumplings = Food("food2.png", 230, 0) # создание объекта класса Food
barbecue = Food("food3.png", 370, 0) # создание объекта класса Food
cake = Food("food4.png", 540, 0) # создание объекта класса Food
chicken = Food("food5.png", 690, 0) # создание объекта класса Food
Food_list = [marmalade,dumplings,barbecue,cake,chicken]

clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    fon.draw_image()  # применение метода отрисовки к объекту класса Food
    clock.tick(40)  # 40фпс\с
    for i in Food_list:
        i.draw_image()
        i.move_food()
    plate.draw_image()  # применение метода отрисовки к объекту класса Food
    plate.move_plate()
    pygame.display.update()  # обновление содержимого экрана
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выход из игры
    pygame.display.update()