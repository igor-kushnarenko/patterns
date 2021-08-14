from abc import ABC, abstractmethod
from enum import Enum

from select_song import player


class JokeState(Enum):
    OFF = 0
    WITHOUT_COIN = 1
    PLAY_TRACK = 2


class State(ABC):

    @abstractmethod
    def on_off_button(self, joke) -> None:
        pass

    @abstractmethod
    def stop_button(self, joke) -> None:
        pass

    @abstractmethod
    def insert_coin(self, joke) -> None:
        pass


class OffState(State):
    def on_off_button(self, joke) -> None:
        print('Welcome! Joke-Box ready!')
        joke.set_state(JokeState.WITHOUT_COIN)

    def stop_button(self, joke) -> None:
        pass

    def insert_coin(self, joke) -> None:
        pass


class WithoutCoinState(State):
    def on_off_button(self, joke) -> None:
        print('Goodbye!')
        joke.set_state(JokeState.OFF)

    def stop_button(self, joke) -> None:
        pass

    def insert_coin(self, joke) -> None:
        print('Insert your coin.')
        print('Select song: ')
        joke.coins += 1
        player()
        # joke.set_state(JokeState.PLAY_TRACK)


# class SelectTrackState(State):
#     def on_off_button(self, joke) -> None:
#         print('Goodbye!')
#         joke.set_state(JokeState.OFF)
#
#     def stop_button(self, joke) -> None:
#         joke.coins -= 1
#         print('Eject your coin.')
#         print('Welcome! Joke-Box ready!')
#         joke.set_state(JokeState.WITHOUT_COIN)
#
#     def insert_coin(self, joke) -> None:
#         print('The coin is already inserted!')


class PlayTrackState(State):
    def on_off_button(self, joke) -> None:
        print('Goodbye!')
        joke.set_state(JokeState.OFF)

    def stop_button(self, joke) -> None:
        print('Welcome! Joke-Box ready!')
        joke.set_state(JokeState.WITHOUT_COIN)

    def insert_coin(self, joke) -> None:
        print('The coin is already inserted!')


class Joke:

    def __init__(self) -> None:
        self.coins = 0
        self.__states = {
            JokeState.OFF: OffState(),
            JokeState.WITHOUT_COIN: WithoutCoinState(),
            JokeState.PLAY_TRACK: PlayTrackState(),
        }
        self.next_state = None
        self.select_song = None
        self.__state = self.__states[JokeState.OFF]

    def set_state(self, state):
        self.__state = self.__states[state]

    def on_off_button(self) -> None:
        self.__state.on_off_button(self)

    def stop_button(self) -> None:
        self.__state.stop_button(self)

    def insert_coin(self) -> None:
        self.__state.insert_coin(self)


if __name__ == '__main__':
    joke = Joke()
    while True:
        user_input = int(input('| 1. ON/OFF | 2. INSERT COIN | 3. STOP |'))
        if user_input == 1:
            joke.on_off_button()
        if user_input == 2:
            joke.insert_coin()
        if user_input == 3:
            joke.stop_button()