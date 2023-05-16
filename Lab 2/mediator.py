from options import *

class OrderPageMediator:
    def __init__(self):
        self.date_picker = DatePicker()
        self.time_picker = TimePicker()
        self.recipient_checkbox = RecipientCheckbox()
        self.name_field = NameField()
        self.phone_field = PhoneField()
        self.pickup_option = PickupOption()

    def handle_date_selection(self, selected_date):
        self.time_picker.update_time_slots(selected_date)

    def handle_recipient_checkbox(self, is_checked):
        if is_checked:
            self.name_field.enable()
            self.phone_field.enable()
        else:
            self.name_field.disable()
            self.phone_field.disable()

    def handle_pickup_option(self, is_selected):
        if is_selected:
            self.date_picker.disable()
            self.time_picker.disable()
            self.recipient_checkbox.disable()
            self.name_field.disable()
            self.phone_field.disable()
        else:
            self.date_picker.enable()
            self.time_picker.enable()
            self.recipient_checkbox.enable()