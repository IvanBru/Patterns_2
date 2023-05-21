class EntityUpdater:
    def update_entity(self, entity_id):
        entity = self.get_entity(entity_id)
        if not self.validate_entity(entity):
            self.send_validation_notification()
            return self.create_response(400, "Validation Failed")

        request_data = self.get_request_data(entity)
        response = self.save_entity(entity_id, request_data)

        if isinstance(entity, Order):
            return self.create_order_response(response)
        else:
            return self.create_response(response.status_code, response.text)

    def get_entity(self, entity_id):
        raise NotImplementedError()

    def validate_entity(self, entity):
        raise NotImplementedError()

    def send_validation_notification(self):
        raise NotImplementedError()

    def get_request_data(self, entity):
        raise NotImplementedError()

    def save_entity(self, entity_id, request_data):
        raise NotImplementedError()

    def create_response(self, status_code, message):
        raise NotImplementedError()

    def create_order_response(self, response):
        raise NotImplementedError()

    def before_update(self):
        pass

    def after_update(self):
        pass