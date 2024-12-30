class Animal:
    def __init__(self, name,food):
        self._food = food
        self.name = name

    def speak(self):
        print(f"{self.name} Speak ..")

class Dog(Animal):
    def __init__(self, name,food, race):
        super().__init__(name, food)
        self.race = race
    def get_food(self):
        return self._food 

dog = Dog("Plug G","Mehhhh")
dog.speak()