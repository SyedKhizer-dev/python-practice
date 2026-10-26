from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


l1 = Lion()
l1.make_sound()

c1 = Cow()
c1.make_sound()
