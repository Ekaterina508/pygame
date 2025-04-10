import pygame  # импортируем библиотеку pygame


class Food():
    def __init__(self, name_image, x, y):  # конструктор, создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect()  # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x  # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y  # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self):  # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

fon = Food ("кухня.jpg", 0, 0)# создание фона
pygame.init()  # обязательная команда
window_size = (1000, 750)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
plate = Food("plate.png", 400, 650)  # создание объекта класса Food

clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    clock.tick(40)  # 40фпс\с
    fon.draw_image()  # применение метода отрисовки к объекту класса Food
    plate.draw_image()  # применение метода отрисовки к объекту класса Food
    pygame.display.update()  # обновление содержимого экрана
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выход из игры
    pygame.display.update()

