import random
from abc import ABC, abstractmethod
from enum import Enum


class BirdState(Enum):
    """Класс в котором собраны все состояния."""
    ON_GROUND = 0
    IN_AIR = 1
    IN_DEATH = 2
    ON_WATER = 3


class State(ABC):
    """Абстрактный класс содержащий все обязательные методы для каждого состояния."""
    @abstractmethod
    def eat(self, bird) -> None:
        pass

    @abstractmethod
    def sleep(self, bird) -> None:
        pass

    @abstractmethod
    def sing(self, bird) -> None:
        pass

    @abstractmethod
    def fly(self, bird) -> None:
        pass

    @abstractmethod
    def swim(self, bird) -> None:
        pass


class InAirState(State):
    """Класс состояния"""
    def eat(self, bird) -> None:
        print('Заглатывая зерно в полете, птица подавилась и свалилась в отрытый люк :(')
        bird.set_state(BirdState.IN_DEATH)

    def sleep(self, bird) -> None:
        print('Пролетая над оживленной автострадой, птица уснула и упала на асфальт :(')
        bird.set_state(BirdState.IN_DEATH)

    def sing(self, bird) -> None:
        print('Птичка летает вокруг дерева и напевает утреннюю песенку :)')

    def fly(self, bird) -> None:
        print('Птица рождена для полета, как человек для велосипеда :)')

    def swim(self, bird) -> None:
        print('Птица аккуратно приводнилась.')
        bird.set_state(BirdState.ON_WATER)


class OnGroundState(State):
    """Класс состояния"""
    def eat(self, bird) -> None:
        print('Птица любит полакомиться насекомыми которые ползают по земле.')

    def sleep(self, bird) -> None:
        print('Птица уснула на земле.')

    def sing(self, bird) -> None:
        print('Птица стоит на камешке и поет песню прошедшему дню.')

    def fly(self, bird) -> None:
        print('Птица решила размять крылья и взлетела.')
        bird.set_state(BirdState.IN_AIR)

    def swim(self, bird) -> None:
        print('Птица плюхнулась в воду.')
        bird.set_state(BirdState.ON_WATER)


class OnWaterState(State):
    """Класс состояния"""
    def eat(self, bird) -> None:
        print('Птица любит полакомиться насекомыми которые водятся на поверхности воды.')

    def sleep(self, bird) -> None:
        print('Птица уснула и булькнула.')
        bird.set_state(BirdState.IN_DEATH)

    def sing(self, bird) -> None:
        print('Птицу несет к водопаду и она поет песню прошедшему дню.')

    def fly(self, bird) -> None:
        print('Птица решила размять крылья и взлетела.')
        bird.set_state(BirdState.IN_AIR)

    def swim(self, bird) -> None:
        print('Птица поплыла брасом.')


class InDeath(State):
    """Класс состояния"""
    def eat(self, bird) -> None:
        print('Птица не живая, ей незачем кушать.')
        bird.next_state = 1

    def sleep(self, bird) -> None:
        print('Птица не живая, и так спит уже.')
        bird.next_state = 1

    def sing(self, bird) -> None:
        print('Птица не живая и не споет более.')
        bird.next_state = 1

    def fly(self, bird) -> None:
        print('Птица не живая и летать не в состоянии.')
        bird.next_state = 1

    def swim(self, bird) -> None:
        print('Птица не живая и плавать не хочет.')
        bird.next_state = 1


class Bird:
    """Класс принимающий состояния"""
    def __init__(self) -> None:
        self.__states = {
            BirdState.ON_GROUND: OnGroundState(),
            BirdState.IN_AIR: InAirState(),
            BirdState.ON_WATER: OnWaterState(),
            BirdState.IN_DEATH: InDeath(),
        }
        self.__state = self.__states[BirdState.ON_GROUND]
        self.next_state = None

    def set_state(self, state):
        self.__state = self.__states[state]

    def eat(self) -> None:
        self.__state.eat(self)

    def sleep(self) -> None:
        self.__state.sleep(self)

    def sing(self) -> None:
        self.__state.sing(self)

    def fly(self) -> None:
        self.__state.fly(self)

    def swim(self) -> None:
        self.__state.swim(self)


if __name__ == '__main__':
    bird = Bird()
    days = 0
    while days < 10:
        dice = random.randint(1, 5)
        days += 1
        print(f'----------------Действие {days}-----------------')
        if dice == 1:
            bird.eat()
        if dice == 2:
            bird.swim()
        if dice == 3:
            bird.fly()
        if dice == 4:
            bird.sleep()
        if dice == 5:
            bird.sing()
        if bird.next_state == 1:
            print('Конец сказки.')
            break