import decimal


class Flowers:
    def __init__(self, species, length, color, amount, price):
        self.species = species
        self.length = length
        self.color = color
        self.amount = amount
        self.price = price
        self._price_check()
        self._amount_check()

    def _price_check(self):
        try:
            if type(self.price) != float:
                raise ValueError
            if abs(decimal.Decimal(str(self.price).rstrip('0')).as_tuple().exponent) != 2:
                raise Exception

        except ValueError:
            return 'Error: It should be "float". Try again.'
        except Exception:
            return 'Error: It should be in the format 0.00. Try again'
        return self.price

    def _amount_check(self):
        try:
            if type(self.amount) != list:
                raise ValueError
            for i in list(self.amount):
                if type(i) == str:
                    raise TypeError
            if len(self.amount) != 3:
                raise Exception

        except ValueError:
            return 'Error: It should be "list". Try again.'
        except TypeError:
            return 'Error: Values should be "int" or "float". Try again.'
        except Exception:
            return 'Error: List must contain 3 values. Try again.'
        return self.amount


class Rose(Flowers):

    def result(self):
        if self._amount_check() == self.amount and self._price_check() == self.price:
            print(f'Price of different number of {self.color} roses {self.length} cm:')
            for i in self.amount:
                cost = i * self.price
                print(f'{i}: {round(cost,2)} rub')
        elif self._amount_check() == self.amount:
            print(self._price_check())
        else:
            print(self._amount_check())


order_one = Rose('rose', 60, 'red', [1, 51, 101], 2.55)
order_one.result()