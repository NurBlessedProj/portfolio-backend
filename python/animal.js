class Animal {
  constructor(name, specie) {
    this.name = name;
    this.specie = specie;
  }
  speak() {
    console.log(`${this.name} says hello to you`);

  }
}

class Dog extends Animal {
  bark() {
    console.log(`${this.name} barks loudly`);
  }
}
const dog = new Dog('Buddy', 'Canis familiaris');
 dog.speak();
dog.bark();
