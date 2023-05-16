from user_settings_memento import UserSettingsMemento

class UserSettings:
    def __init__(self):
        self.notification_settings = {}

    def set_notification_setting(self, notification_type, is_enabled):
        self.notification_settings[notification_type] = is_enabled

    def create_memento(self):
        return UserSettingsMemento(self.notification_settings)

    def restore_from_memento(self, memento):
        self.notification_settings = memento.get_notification_settings()