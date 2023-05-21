from entity_updater import EntityUpdater

class OrderUpdater(EntityUpdater):
    def get_entity(self, entity_id):
        # Retrieve the Order entity using the REST API
        pass

    def validate_entity(self, entity):
        # Validate the Order entity
        pass

    def send_validation_notification(self):
        # Send a notification to the administrator about validation failure
        pass

    def get_request_data(self, entity):
        # Get the request data for updating the Order entity
        pass

    def save_entity(self, entity_id, request_data):
        # Save the updated Order entity using the REST API
        pass

    def create_response(self, status_code, message):
        #Create a response object for non-Order entities
        pass

    def create_order_response(self, response):
        # Create a response object for Order update with additional JSON representation
        pass

    def before_update(self):
        # Custom logic before updating the Order entity
        pass

    def after_update(self):
        # Custom logic after updating the Order entity
        pass