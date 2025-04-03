import pygame

class Food():
    def __init__(self, a, c, d):
        self.image = pygame.image.load(a) # загрузка картинки
        self.rect = self.image.get_rect() # получение прямоугольника от картинки
        self.x = c
        self.y = d

    def draw_image(self): # метод адресовки картинки
        screen.blit(self.image, (self.x, self.y))

fon = Food("кухня.jpg", 0, 0) # создание объекта класса
fon1 = Food("R.png", 0, 0)
pygame.init()# обязательная программа
window_size=(600,600)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
clock = pygame.time.Clock()#фпс


while True:#игровой цикл
    fon.draw_image() # применение метода адресовки картинки к объекту картинки
    fon1.draw_image()
    clock.tick(40)#40фпс\с
    for event in pygame.event.get(): # события
        if event.type == pygame.QUIT: # усли нажали крест
            pygame.QUIT() # выход из игры
    pygame.display.update()#обновление содержимого экрана

