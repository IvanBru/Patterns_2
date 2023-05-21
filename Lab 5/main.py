from order_updater import OrderUpdater
from user_updater import UserUpdater
from product_updater import ProductUpdater

product_updater = ProductUpdater()
user_updater = UserUpdater()
order_updater = OrderUpdater()

#Update a Product entity
product_id = 123
product_response = product_updater.update_entity(product_id)
print(product_response)

#Update a User entity
user_id = 456
user_response = user_updater.update_entity(user_id)
print(user_response)

#Update an Order entity
order_id = 789
order_response = order_updater.update_entity(order_id)
print(order_response)