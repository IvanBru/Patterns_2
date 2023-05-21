from entity_updater import EntityUpdater

class ProductUpdater(EntityUpdater):
    def get_entity(self, entity_id):
        # Retrieve the Product entity using the REST API
        pass

    def validate_entity(self, entity):
        # Validate the Product entity
        pass

    def send_validation_notification(self):
        # Send a notification to the administrator about validation failure
        pass

    def get_request_data(self, entity):
        # Get the request data for updating the Product entity
        pass

    def save_entity(self, entity_id, request_data):
        # Save the updated Product entity using the REST API
        pass

    def create_response(self, status_code, message):
        # Create a response object for Product update
        pass

    def before_update(self):
        # Custom logic before updating the Product entity
        pass

    def after_update(self):
        # Custom logic after updating the Product entity
        pass
