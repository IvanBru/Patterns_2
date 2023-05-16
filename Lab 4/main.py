class DeliveryCostStrategy:
    def calculate_cost(self, order):
        raise NotImplementedError()


class SelfPickupCostStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order):
        return 0


class ExternalDeliveryCostStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order):
        return 10


class InHouseDeliveryCostStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order):
        return 5

class DeliveryApp:
    def __init__(self, delivery_cost_strategy):
        self.delivery_cost_strategy = delivery_cost_strategy

    def set_delivery_cost_strategy(self, delivery_cost_strategy):
        self.delivery_cost_strategy = delivery_cost_strategy

    def calculate_delivery_cost(self, order):
        return self.delivery_cost_strategy.calculate_cost(order)

order = {"items": ["Sup", "Burger", "Potato"], "total_amount": 22}

self_pickup_strategy = SelfPickupCostStrategy()
external_delivery_strategy = ExternalDeliveryCostStrategy()
in_house_delivery_strategy = InHouseDeliveryCostStrategy()

delivery_app = DeliveryApp(in_house_delivery_strategy)

delivery_cost = delivery_app.calculate_delivery_cost(order)
print("Delivery Cost:", delivery_cost)

delivery_app.set_delivery_cost_strategy(external_delivery_strategy)

delivery_cost = delivery_app.calculate_delivery_cost(order)
print("Delivery Cost:", delivery_cost)