class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    def speak(self):
        print(f"{self.name} says hello to you")

dog = Animal("Yung money", "dog")
cat = Animal("blonedelle", "mehhh")
dog.speak()
cat.speak()
