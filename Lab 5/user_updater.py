from entity_updater import EntityUpdater

class UserUpdater(EntityUpdater):
    def get_entity(self, entity_id):
        # Retrieve the User entity using the REST API
        pass

    def validate_entity(self, entity):
        # Validate the User entity
        pass

    def send_validation_notification(self):
        # Send a notification to the administrator about validation failure
        pass

    def get_request_data(self, entity):
        # Get the request data for updating the User entity
        pass

    def save_entity(self, entity_id, request_data):
        # Save the updated User entity using the REST API
        pass

    def create_response(self, status_code, message):
        # Create a response object for User update
        pass

    def before_update(self):
        # Custom logic before updating the User entity
        pass

    def after_update(self):
        # Custom logic after updating the User entity
        pass
