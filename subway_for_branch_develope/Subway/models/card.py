from Subway.exceptions import *
from datetime import datetime
from Subway.models.logger import logger

logger.name = 'CARD'


# Card class for creating card to travel
class Card:
    CARDS = ('single_trip', 'credit', 'term')

    def __init__(self, name: str, charge: int | float | str = '') -> None:
        self.name = name
        self.charge = charge
        if self.name == 'term':
            self.expiration_date = self.create_expiration_date()
        logger.info(f"{self.name} card has created")

    def __repr__(self):
        return f"{self.name} card - charge: {self.charge}"

    def __getattr__(self, item):
        logger.error(f"AttributeError:{item} attribute doesn't exist")
        return f"'{item}' attribute does not exist!"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            logger.error("TypeError: name of the card must be a string")
            raise TypeError("Name must be str")
        if value not in self.__class__.CARDS:
            logger.error("CardError: Invalid card. card only can be one of ('single_trip', 'credit', 'term')")
            raise CardError("Invalid card.")
        self._name = value

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        if self.name != 'single_trip':
            if isinstance(value, int):
                if value < 0:
                    logger.error("ChargeError: charge can't be negative")
                    raise ChargeError("charge can't be negative")
                self._charge = value
                logger.info(f"{self.name} card's charge is {value}")
            else:
                logger.error("ChargeError: charge must an int number")
                raise ChargeError("charge must be an int number")
        else:
            self._charge = 10  # price for only one trip
            logger.info("single_trip card's charge is 10")

    @staticmethod
    def create_expiration_date():
        today = datetime.today().date()
        return datetime(today.year + 1, today.month, today.day).date()

    def charge_increase(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            logger.error("ChargeError: you should enter a float or an int number")
            raise ChargeError("you should enter a float or an int number")
        if value <= 10:
            logger.error("ChargeError: minimum price for charging your card is 10")
            raise ChargeError("minimum price for charging your card is 10")
        self.charge += value
        logger.info(f"{self.name} card has charged {value}")

    def pay(self, cost=10):
        if self.name == 'term':
            self.check_date(self.expiration_date)
        if self.name == 'single_trip':
            if self.charge >= cost:
                self._charge -= cost
                logger.info(f"you paid {cost} for the trip, by {self.name} card")
            else:
                logger.error("ChargeError: this card has been used before")
                raise ChargeError("This card has been used before")
        else:
            if self.charge >= cost:
                self.charge -= cost
                logger.info(f"you paid {cost} for the trip, by {self.name} card")
            else:
                logger.error("ChargeError: you don't have enough charge to pay cost of the trip, sorry")
                raise ChargeError("you don't have enough charge to pay cost of the trip, sorry")

    @staticmethod
    def check_date(date):
        y, m, d = datetime.today().year, datetime.today().month, datetime.today().day
        if date < datetime(y, m, d):
            logger.error("DateError: your card has expired")
            raise DateError("Your card has expired")
        return True

# card1 = Card('single_trip')
# print(card1.name)
# print(card1.charge)
# print(card1.expiration_date)

# card1.pay()

# card2 = Card('credit', 1000)
# print(card2.name)
# print(card2.charge)
# card2.charge_increase(20)
# card2.pay(1020)
# print(card2.charge)
# print(card2.expiration_date)

# card3 = Card('term', 100)
# print(card3.name)
# print(card3.charge)
# print(card3.expiration_date)
# card3.charge_increase(20)
# print(card3.charge)
# card3.pay(30)
