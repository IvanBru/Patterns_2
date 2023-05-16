class DatePicker:
    def __init__(self):
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

class TimePicker:
    def __init__(self):
        self.enabled = True
        self.time_slots = []

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def update_time_slots(self, selected_date):
        self.time_slots = []

class RecipientCheckbox:
    def __init__(self):
        self.enabled = True
        self.checked = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def set_checked(self, is_checked):
        self.checked = is_checked

class NameField:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

class PhoneField:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

class PickupOption:
    def __init__(self):
        self.selected = False

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False