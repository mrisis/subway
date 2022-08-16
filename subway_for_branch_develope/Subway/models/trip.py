from time import sleep
from Subway.models.user import *
from Subway.exceptions import CostError
from Subway.models.logger import logger
logger.name = 'TRIP'


class Trip:
    list_of_trips = []

    def __init__(self, origin, destination, cost, passenger: User, card):
        if Trip.check_status(origin, destination):
            self.origin = origin
            self.destination = destination
            self.cost = cost
            self.passenger = passenger
            self.payment(card)
            self.travel()

    def __repr__(self):
        return f"origin: {self.origin}|destination: {self.destination}"

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            logger.error("CostError: Cost of the trip must be an int or a float value")
            raise CostError("Cost of the trip must be an int or a float number")
        if value <= 0:
            logger.error("CostError: Cost of the trip must be greater than zero")
            raise CostError("Cost of the trip must be greater than zero")
        self._cost = value

    @classmethod
    def check_status(cls, origin, destination):
        temp = f"origin: {origin}|destination: {destination}"
        if temp in list(map(str, cls.list_of_trips)):
            logger.error("TripError: This trip has done before, you can't do take that again")
            raise TripError("This trip has done before, you can't do take that again")
        logger.info("The Trip registered")
        return True

    def payment(self, card):
        if card not in self.passenger.wallet.keys():
            logger.error("CardError: You don't have such card")
            raise CardError("you don't have such card")
        self.passenger.wallet[card].pay(self.cost)
        logger.info(f"{self.passenger} payed the cost of the {self} trip with {card} card")

    def travel(self):
        print(f"Traveling from {self.origin} to {self.destination}")
        sleep(2)
        print(f'Welcome to {self.destination}')
        self.__class__.list_of_trips.append(self)
        logger.info(f"{self} trip has done")


# account1 = BankAccount('mehdi mirzaie', 23, 3242157397, 5000)
# mehdi = User('mehdi mirzaie', 23, account1)
# mehdi.buy_card('single_trip')
# mehdi.buy_card('credit', 230)
# print(mehdi.wallet['credit'].charge)
# trip1 = Trip('narmak', 'taleghani', 10, mehdi, 'credit')
# print(mehdi.wallet['credit'].charge)
#
# print(trip1.passenger)
# print(mehdi.wallet['credit'])

# trip2 = Trip('kermanshah', 'rasht', 200, 'mehdi')
# trip3 = Trip('kermanshah', 'tehran', 200, 'mehdi')
# trip2 = Trip('narmak', 'taleghani', 10, mehdi, 'credit')
# print(Trip.list_of_trips)
