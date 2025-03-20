class My_class():
    def __init__(self, a, c, r, b, t):
       self.name = a
       self.clothes = c
       self.health = r
       self.weapon = b
       self.impact = t


    def print_info(self):
        print("Ваше имя:", self.name)
        print("Ваша одежда:", self.clothes)
        print("Ваше здоровье:", self.health)
        print("Ваше оружие:", self.weapon )
        print("Ваша сила:",self.impact)

me = My_class("Rita", "shorts,vest", "100", "stick", "50")
me.print_info()
