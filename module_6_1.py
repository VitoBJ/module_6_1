class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True





rose = Flower("Роза")
apple = Fruit("Яблоко")


lion = Predator("Лев")
rabbit = Mammal("Кролик")


lion.eat(apple)


rabbit.eat(rose)


print(f"Состояние {lion.name}: alive={lion.alive}, fed={lion.fed}")
print(f"Состояние {rabbit.name}: alive={rabbit.alive}, fed={rabbit.fed}")
