from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass


class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y


class Multi(BaseStrategy):
    def do_work(self, x, y):
        return x * y


class Calculator:
    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print(f'Result is: {self.strategy.do_work(x, y)}')


calc = Calculator()
print(calc)
calc.set_strategy(Adder())
calc.calculate(10, 10)
